"""OTel GenAI semantic-convention names for @traced span attributes.

Orq ingest reads ``gen_ai.usage.input_tokens`` / ``output_tokens``,
``gen_ai.provider.name`` and ``gen_ai.request.*``, so those values are written
under their semconv name only. Cached and reasoning tokens are the exception:
Orq bills them from ``gen_ai.usage.*_tokens_details.*``, so they are written
under that key as well as the semconv one.
"""

from typing import Any, Dict, Mapping

from .constants import SPAN_TYPE_OPERATIONS

# span.log() key -> semconv key. The span.log() key is replaced.
RENAMES = {
    "request.provider": "gen_ai.provider.name",
    "request.model": "gen_ai.request.model",
    "request.temperature": "gen_ai.request.temperature",
    "request.top_p": "gen_ai.request.top_p",
    "request.max_tokens": "gen_ai.request.max_tokens",
    "request.frequency_penalty": "gen_ai.request.frequency_penalty",
    "request.presence_penalty": "gen_ai.request.presence_penalty",
    "request.seed": "gen_ai.request.seed",
    "metrics.prompt_tokens": "gen_ai.usage.input_tokens",
    "metrics.completion_tokens": "gen_ai.usage.output_tokens",
    "metrics.prompt_tokens_details.cached_tokens": "gen_ai.usage.cache_read.input_tokens",
    "metrics.completion_tokens_details.reasoning_tokens": "gen_ai.usage.reasoning.output_tokens",
}

# Semconv key -> the key Orq billing reads. Both are written.
ORQ_BILLING_KEYS = {
    "gen_ai.usage.cache_read.input_tokens": "gen_ai.usage.prompt_tokens_details.cached_tokens",
    "gen_ai.usage.reasoning.output_tokens": "gen_ai.usage.completion_tokens_details.reasoning_tokens",
}

# Semconv attribute types. A value of another type keeps its span.log() key.
_NUMBER = (int, float)
_SEMCONV_TYPES = {
    "gen_ai.provider.name": (str,),
    "gen_ai.request.model": (str,),
    "gen_ai.request.temperature": _NUMBER,
    "gen_ai.request.top_p": _NUMBER,
    "gen_ai.request.max_tokens": (int,),
    "gen_ai.request.frequency_penalty": _NUMBER,
    "gen_ai.request.presence_penalty": _NUMBER,
    "gen_ai.request.seed": (int,),
    "gen_ai.usage.input_tokens": (int,),
    "gen_ai.usage.output_tokens": (int,),
    "gen_ai.usage.cache_read.input_tokens": (int,),
    "gen_ai.usage.reasoning.output_tokens": (int,),
}


def _renamable(semconv_key: str, value: Any) -> bool:
    return isinstance(value, _SEMCONV_TYPES[semconv_key]) and not isinstance(value, bool)


def to_genai(attributes: Mapping[str, Any], span_type: str, span_name: str) -> Dict[str, Any]:
    """Return ``attributes`` with semconv names, plus the Orq billing keys.

    A key the caller set explicitly is never overwritten.
    """
    out: Dict[str, Any] = {}
    for key, value in attributes.items():
        semconv_key = RENAMES.get(key)
        if semconv_key and semconv_key not in attributes and _renamable(semconv_key, value):
            out[semconv_key] = value
        else:
            out[key] = value

    for semconv_key, billing_key in ORQ_BILLING_KEYS.items():
        if semconv_key in out and billing_key not in out:
            out[billing_key] = out[semconv_key]
        elif billing_key in out and semconv_key not in out:
            out[semconv_key] = out[billing_key]

    operation = SPAN_TYPE_OPERATIONS.get(span_type)
    if operation:
        out.setdefault("gen_ai.operation.name", operation)
    if span_type == "agent":
        out.setdefault("gen_ai.agent.name", span_name)
    if span_type == "tool":
        out.setdefault("gen_ai.tool.name", span_name)
        out.setdefault("gen_ai.tool.type", "function")
    return out


def error_type(error: BaseException) -> str:
    """Fully qualified exception class name, as semconv ``error.type`` expects."""
    cls = type(error)
    if cls.__module__ == "builtins":
        return cls.__qualname__
    return f"{cls.__module__}.{cls.__qualname__}"
