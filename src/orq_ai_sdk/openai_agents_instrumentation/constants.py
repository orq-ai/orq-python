"""Constants and semantic conventions for OpenAI Agents instrumentation."""

from enum import Enum


class SpanAttributes(Enum):
    """Span attribute names for OpenAI Agents instrumentation."""
    # GenAI semantic convention attributes
    OPERATION_NAME = "gen_ai.operation.name"
    REQUEST_MODEL = "gen_ai.request.model"
    RESPONSE_ID = "gen_ai.response.id"
    RESPONSE_MODEL = "gen_ai.response.model"
    USAGE_INPUT_TOKENS = "gen_ai.usage.input_tokens"
    USAGE_OUTPUT_TOKENS = "gen_ai.usage.output_tokens"
    TOOL_NAME = "gen_ai.tool.name"
    TOOL_CALL_ID = "gen_ai.tool.call.id"
    GEN_AI_AGENT_NAME = "gen_ai.agent.name"

    # Orq custom attributes
    KIND = "orq.span.kind"
    OUTPUT_VALUE = "orq.output.value"
    AGENT_NAME = "agent.name"


class SpanKind(Enum):
    """Span kind values."""
    WORKFLOW = "workflow"
    AGENT = "agent"
    LLM = "llm"
    TOOL = "tool"
    GENERIC = "generic"
    CHAIN = "chain"
