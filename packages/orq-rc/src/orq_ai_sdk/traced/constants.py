# only function is supported for now which then set as SpanType.Generic in the backend - but will support other types especially llm once the POC is completed client sdk + server endpoint
# Span type -> OTel GenAI gen_ai.operation.name; "function" has no GenAI operation.
SPAN_TYPE_OPERATIONS = {
    "agent": "invoke_agent",
    "embedding": "embeddings",
    "function": None,
    "llm": "chat",
    "retrieval": "retrieval",
    "tool": "execute_tool",
}
VALID_SPAN_TYPES = set(SPAN_TYPE_OPERATIONS)
