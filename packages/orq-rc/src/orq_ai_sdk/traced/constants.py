# only function is supported for now which then set as SpanType.Generic in the backend - but will support other types especially llm once the POC is completed client sdk + server endpoint
VALID_SPAN_TYPES = {"agent", "embedding", "function", "llm", "retrieval", "tool"}

# W3C tracestate vendor member so the orq router continues this parent instead
# of treating a bare traceparent as foreign APM.
ORQ_TRACESTATE_KEY = "orq"
ORQ_TRACESTATE_MEMBER = "orq=1"
