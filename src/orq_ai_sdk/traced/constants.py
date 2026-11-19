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

# W3C tracestate vendor member so the orq router continues this parent instead
# of treating a bare traceparent as foreign APM.
ORQ_TRACESTATE_KEY = "orq"
ORQ_TRACESTATE_MEMBER = "orq=1"
