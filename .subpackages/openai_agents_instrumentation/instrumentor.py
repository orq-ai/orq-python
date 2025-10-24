from typing import Collection, Dict, Optional

# Try to import required dependencies
try:
    from agents import set_trace_processors
except ImportError:
    raise ImportError(
        "OpenAI Agents not available. Install with: pip install openai-agents"
    )

try:
    from opentelemetry import trace as trace_api
    from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
    from opentelemetry.trace import Tracer, TracerProvider
except ImportError:
    raise ImportError(
        "OpenTelemetry not available. Install with: pip install opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation"
    )

from .processor import EnhancedOpenAIAgentsProcessor

# Import version from the parent package
try:
    from orq_ai_sdk._version import __version__
except ImportError:
    __version__ = "unknown"


class OpenAIAgentsInstrumentor(BaseInstrumentor):
    """
    Orq simplified instrumentor for openai-agents with enhanced agent span support.
    
    This instrumentor provides:
    - Basic OpenTelemetry tracing for OpenAI agents
    - Enhanced agent spans with aggregated input/output from child spans
    """

    def instrumentation_dependencies(self) -> Collection[str]:
        """Return the dependencies required for this instrumentation."""
        return ["openai-agents"]

    def _instrument(self, **kwargs: Dict[str, object]) -> None:
        """Instrument the openai-agents library."""
        # Get tracer provider
        tracer_provider: Optional[TracerProvider] = kwargs.get("tracer_provider")
        if not tracer_provider:
            tracer_provider = trace_api.get_tracer_provider()

        # Create tracer with version from orq_ai_sdk package
        tracer: Tracer = tracer_provider.get_tracer(
            instrumenting_module_name=__name__,
            instrumenting_library_version=__version__
        )

        # Create our enhanced processor
        processor = EnhancedOpenAIAgentsProcessor(tracer)

        # Set our processor as the exclusive trace processor
        set_trace_processors([processor])

    def _uninstrument(self, **kwargs: Dict[str, object]) -> None:
        """Uninstrument the openai-agents library."""
        # Reset to no processors
        set_trace_processors([])