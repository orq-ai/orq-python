"""Type definitions for Orq decorator tracing."""

from enum import Enum


class SpanType(str, Enum):
    """Enumeration of available span types."""
    
    Generic = "span.generic"
    # TODO: to add other types for now its generic for capturing function span input/output