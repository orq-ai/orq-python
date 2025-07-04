"""Utility functions for Orq decorator SDK."""

import time
import uuid
import json
from datetime import datetime, timezone
from typing import Any, Dict, Optional
import random
import string


def get_current_time_iso() -> str:
    """Get current time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


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


def extract_attributes(obj: Any) -> Dict[str, Any]:
    """Extract attributes from an object."""
    if isinstance(obj, dict):
        return obj
    elif hasattr(obj, "__dict__"):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    else:
        return {}


def safe_json_dumps(obj: Any) -> str:
    """Safely convert object to JSON string."""
    try:
        return json.dumps(serialize_value(obj))
    except Exception:
        return json.dumps({"error": "Failed to serialize", "type": str(type(obj))})


def calculate_duration(start_time: float, end_time: Optional[float] = None) -> float:
    """Calculate duration in seconds."""
    if end_time is None:
        end_time = time.time()
    return end_time - start_time