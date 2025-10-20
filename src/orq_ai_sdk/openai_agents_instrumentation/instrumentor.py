"""Simplified OpenAI Agents instrumentor."""

from typing import Any, Collection

from agents import set_trace_processors
from opentelemetry import trace as trace_api
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.trace import Tracer

from openai_agents_instrumentation.package import _instruments
from openai_agents_instrumentation.processor import EnhancedOpenAIAgentsProcessor
from openai_agents_instrumentation.version import __version__


class OpenAIAgentsInstrumentor(BaseInstrumentor):
    """
    A simplified instrumentor for openai-agents with enhanced agent span support.
    
    This instrumentor provides:
    - Basic OpenTelemetry tracing for OpenAI agents
    - Enhanced agent spans with aggregated input/output from child spans
    - Simplified configuration without complex dependencies
    """

    def instrumentation_dependencies(self) -> Collection[str]:
        """Return the dependencies required for instrumentation."""
        return _instruments

    def _instrument(self, **kwargs: Any) -> None:
        """Instrument the openai-agents library."""
        # Get tracer provider
        tracer_provider = kwargs.get("tracer_provider")
        if not tracer_provider:
            tracer_provider = trace_api.get_tracer_provider()

        # Create tracer
        tracer = tracer_provider.get_tracer(__name__, __version__)

        # Create our enhanced processor
        processor = EnhancedOpenAIAgentsProcessor(tracer)

        # Set our processor as the exclusive trace processor
        set_trace_processors([processor])

    def _uninstrument(self, **kwargs: Any) -> None:
        """Uninstrument the openai-agents library."""
        # Reset to no processors
        set_trace_processors([])