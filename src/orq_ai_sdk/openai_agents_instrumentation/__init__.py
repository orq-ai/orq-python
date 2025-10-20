"""OpenAI Agents Instrumentation SDK.

A simplified OpenTelemetry instrumentation package for OpenAI agents with enhanced
agent span input/output tracking capabilities.
"""

from openai_agents_instrumentation.instrumentor import OpenAIAgentsInstrumentor
from openai_agents_instrumentation.version import __version__

__all__ = ["OpenAIAgentsInstrumentor", "__version__"]