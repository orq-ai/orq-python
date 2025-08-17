"""Utility functions for Orq decorator SDK."""
# pylint: disable=no-else-return

import time
import random
from datetime import datetime, timezone
from typing import Any
from .constants import VALID_SPAN_TYPES


def get_current_time_iso() -> str:
    """Get current time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def serialize_value(value: Any) -> Any:
    """Serialize a value for JSON encoding."""
    if hasattr(value, "__dict__"):
        return {k: serialize_value(v) for k, v in value.__dict__.items()}
    elif isinstance(value, (list, tuple)):
        return [serialize_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    elif isinstance(value, (str, int, float, bool, type(None))):
        return value
    else:
        return str(value)


def generate_ulid() -> str:
    """Generate a ULID (Universally Unique Lexicographically Sortable Identifier)."""
    # ULID is composed of:
    # - 48 bits of timestamp (milliseconds since epoch)
    # - 80 bits of randomness
    
    # Get current timestamp in milliseconds
    timestamp_ms = int(time.time() * 1000)
    
    # Convert timestamp to base32-like encoding (using Crockford's base32)
    base32_chars = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
    
    # Encode timestamp (10 characters for 48 bits)
    timestamp_str = ""
    for _ in range(10):
        timestamp_str = base32_chars[timestamp_ms & 0x1F] + timestamp_str
        timestamp_ms >>= 5
    
    # Generate 16 random characters (80 bits of randomness)
    random_str = ''.join(random.choices(base32_chars, k=16))
    
    return timestamp_str + random_str


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
