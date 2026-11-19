"""Utility functions for Orq decorator SDK."""
# pylint: disable=no-else-return

import enum
import json
import math
import numbers
import time
import random
from datetime import datetime, timezone
from typing import Any, Dict, Optional, Set, Union

from pydantic_core import to_jsonable_python

from .constants import VALID_SPAN_TYPES


def get_current_time_iso() -> str:
    """Get current time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')


MAX_ENCODE_DEPTH = 32
_INT64_MIN, _INT64_MAX = -(2 ** 63), 2 ** 63 - 1


def _safe_str(value: Any) -> str:
    try:
        return str(value)
    except Exception:  # pylint: disable=broad-except
        return f"<unrepresentable {type(value).__name__}>"


def _json_key(key: Any) -> str:
    if isinstance(key, enum.Enum):
        key = key.value
    return str.__str__(key) if isinstance(key, str) else _safe_str(key)


def to_json_safe(value: Any, _stack: Optional[Set[int]] = None, _depth: int = 0) -> Any:
    """Convert any value into a tree of plain JSON types. Never raises.

    NaN/Infinity and ints outside int64 become strings: JSON has no NaN, and
    OTel attributes are int64. Other objects go through pydantic (dataclasses,
    models, dates, bytes) and otherwise become ``str()``; their fields are
    never dumped, so a client's ``api_key`` cannot leak into a span.
    """
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, enum.Enum):
        return to_json_safe(value.value, _stack, _depth)
    if isinstance(value, str):
        return str.__str__(value)
    if isinstance(value, int):
        number = int.__int__(value)
        return number if _INT64_MIN <= number <= _INT64_MAX else str(number)
    if isinstance(value, float):
        real = float.__float__(value)
        return real if math.isfinite(real) else str(real)
    if _depth >= MAX_ENCODE_DEPTH:
        return "[MaxDepth]"
    stack = _stack if _stack is not None else set()
    if id(value) in stack:
        return "[Circular]"
    stack.add(id(value))
    try:
        if isinstance(value, dict):
            return {
                _json_key(k): to_json_safe(v, stack, _depth + 1)
                for k, v in value.items()
            }
        if isinstance(value, (list, tuple, set, frozenset)):
            return [to_json_safe(v, stack, _depth + 1) for v in value]
        if isinstance(value, numbers.Integral):  # numpy ints and friends
            return to_json_safe(int(value))
        if isinstance(value, numbers.Real):
            return to_json_safe(float(value))
        return to_json_safe(to_jsonable_python(value, fallback=_safe_str), stack, _depth + 1)
    except Exception:  # pylint: disable=broad-except
        return _safe_str(value)
    finally:
        stack.discard(id(value))


def to_attribute_text(value: Any) -> str:
    """Render a value as an OTel string attribute: strings as-is, anything else as JSON.

    The value goes through to_json_safe first, so this never raises.
    """
    if isinstance(value, str):
        return str.__str__(value)
    return json.dumps(to_json_safe(value), ensure_ascii=False)


def flatten_attribute(key: str, value: Any) -> Dict[str, Union[str, bool, int, float]]:
    """Flatten one span attribute into OTel-ready dotted keys. Never raises.

    The value goes through to_json_safe first. Dicts then recurse into
    ``key.child`` keys, so ``metrics={"prompt_tokens": 76}`` becomes
    ``metrics.prompt_tokens = 76``. Booleans and numbers stay native, strings
    pass through to_attribute_text, None is dropped, and lists become JSON text.
    """
    return _flatten_json_safe(key, to_json_safe(value))


def _flatten_json_safe(key: str, value: Any) -> Dict[str, Union[str, bool, int, float]]:
    if value is None:
        return {}
    if isinstance(value, dict):
        flat: Dict[str, Union[str, bool, int, float]] = {}
        for child_key, child_value in value.items():
            flat.update(_flatten_json_safe(f"{key}.{child_key}", child_value))
        return flat
    if isinstance(value, (bool, int, float)):
        return {key: value}
    return {key: to_attribute_text(value)}


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
