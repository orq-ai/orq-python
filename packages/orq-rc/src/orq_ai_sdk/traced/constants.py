# only function is supported for now which then set as SpanType.Generic in the backend - but will support other types especially llm once the POC is completed client sdk + server endpoint
VALID_SPAN_TYPES = {"agent", "embedding", "function", "llm", "retrieval", "tool"}

# Upper bound for a serialized input/output OTel attribute value, in characters.
MAX_ATTRIBUTE_VALUE_CHARS = 64 * 1024
TRUNCATION_MARKER = "...[truncated]"
