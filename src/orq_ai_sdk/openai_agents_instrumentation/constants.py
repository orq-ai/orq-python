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
    TOOL_CALL_ARGUMENTS = "gen_ai.tool.call.arguments"
    TOOL_CALL_RESULT = "gen_ai.tool.call.result"
    GEN_AI_AGENT_NAME = "gen_ai.agent.name"
    PROVIDER_NAME = "gen_ai.provider.name"
    WORKFLOW_NAME = "gen_ai.workflow.name"
    INPUT_MESSAGES = "gen_ai.input.messages"
    OUTPUT_MESSAGES = "gen_ai.output.messages"
    SYSTEM_INSTRUCTIONS = "gen_ai.system_instructions"
    RESPONSE_FINISH_REASONS = "gen_ai.response.finish_reasons"
    USAGE_CACHE_READ_INPUT_TOKENS = "gen_ai.usage.cache_read.input_tokens"
    REQUEST_TEMPERATURE = "gen_ai.request.temperature"
    REQUEST_TOP_P = "gen_ai.request.top_p"
    REQUEST_MAX_TOKENS = "gen_ai.request.max_tokens"
    TOOL_TYPE = "gen_ai.tool.type"
    OPENAI_API_TYPE = "openai.api.type"


class GenAIOperation(Enum):
    """gen_ai.operation.name values."""
    INVOKE_WORKFLOW = "invoke_workflow"
    INVOKE_AGENT = "invoke_agent"
    CHAT = "chat"
    EXECUTE_TOOL = "execute_tool"
