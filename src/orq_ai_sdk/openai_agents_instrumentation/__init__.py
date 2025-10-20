"""OpenAI Agents Instrumentation SDK.

A simplified OpenTelemetry instrumentation package for OpenAI agents with enhanced
agent span input/output tracking capabilities.
"""

from dependencies import validate_dependencies
from instrumentor import OpenAIAgentsInstrumentor

# Validate dependencies on import for immediate feedback
validate_dependencies()

__all__ = ["OpenAIAgentsInstrumentor"]