"""Orq OpenAI Agents Instrumentation SDK.

A simplified OpenTelemetry instrumentation package for OpenAI agents with enhanced
agent span input/output tracking capabilities.
"""

# Try to import OpenTelemetry, but make it optional
try:
    from opentelemetry import trace
except ImportError:
    raise ImportError(
        "OpenTelemetry not available. Install with: pip install opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation"
    )

# Try to import OpenAI Agents, but make it optional
try:
    import agents
except ImportError:
    raise ImportError(
        "OpenAI Agents not available. Install with: pip install openai-agents"
    )

from .instrumentor import OpenAIAgentsInstrumentor

__all__ = ["OpenAIAgentsInstrumentor"]