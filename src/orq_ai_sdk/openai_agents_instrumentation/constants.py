"""Constants and semantic conventions for OpenAI Agents instrumentation."""

from enum import Enum


class GenAIAttributes(Enum):
    """GenAI semantic convention attribute names."""
    OPERATION_NAME = "gen_ai.operation.name"
    REQUEST_MODEL = "gen_ai.request.model"
    REQUEST_MESSAGES = "gen_ai.request.messages"
    RESPONSE_MODEL = "gen_ai.response.model"
    RESPONSE_MESSAGES = "gen_ai.response.messages"
    RESPONSE_ID = "gen_ai.response.id"
    RESPONSE_FINISH_REASONS = "gen_ai.response.finish_reasons"
    USAGE_INPUT_TOKENS = "gen_ai.usage.input_tokens"
    USAGE_OUTPUT_TOKENS = "gen_ai.usage.output_tokens"
    SYSTEM = "gen_ai.system"
    TOOL_NAME = "gen_ai.tool.name"


class SpanAttributes(Enum):
    """Additional span attribute names."""
    KIND = "orq.span.kind"
    INPUT_VALUE = "orq.input.value"
    OUTPUT_VALUE = "orq.output.value"
    AGENT_NAME = "agent.name"


class SpanKind(Enum):
    """Span kind values."""
    WORKFLOW = "workflow"
    AGENT = "agent"
    LLM = "llm"
    TOOL = "tool"
    CHAIN = "chain"


class GenAISystem(Enum):
    """GenAI system values."""
    OPENAI = "openai"


class GenAIOperation(Enum):
    """GenAI operation values."""
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"


class FinishReason(Enum):
    """LLM finish reason values."""
    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"
    ERROR = "error"