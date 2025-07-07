"""Type definitions for Orq decorator tracing."""

# only function is supported for now which then set as SpanType.Generic in the backend - but will support other types especially llm once the POC is completed client sdk + server endpoint
VALID_SPAN_TYPES = {"llm", "score", "function", "eval", "task", "tool"}


def validate_span_type(span_type: str) -> str:
    """
    Validate that the span type is one of the allowed values.
    
    Args:
        span_type: The span type string to validate
        
    Returns:
        The validated span type
        
    Raises:
        ValueError: If span_type is not valid
    """
    if span_type not in VALID_SPAN_TYPES:
        raise ValueError(
            f"Invalid span type: '{span_type}'. "
            f"Must be one of: {', '.join(sorted(VALID_SPAN_TYPES))}"
        )
    return span_type