"""Orq OpenAI Agents Instrumentation SDK.

A simplified OpenTelemetry instrumentation package for OpenAI agents with enhanced
agent span input/output tracking capabilities.
"""

# Try to import OpenTelemetry, but make it optional
try:
    from opentelemetry import trace
except ImportError as exc:
    raise ImportError(
        "OpenTelemetry not available. Install with: pip install opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation"
    ) from exc

# Try to import OpenAI Agents, but make it optional
try:
    import agents  # type: ignore[import-not-found]
except ImportError as exc:
    raise ImportError(
        "OpenAI Agents not available. Install with: pip install openai-agents"
    ) from exc

from .instrumentor import OpenAIAgentsInstrumentor

__all__ = ["OpenAIAgentsInstrumentor"]
