"""OTel GenAI semantic-convention names for @traced span attributes.

Orq ingest reads ``gen_ai.usage.input_tokens`` / ``output_tokens``,
``gen_ai.provider.name`` and ``gen_ai.request.*``, so those values are written
under their semconv name only. Cached and reasoning tokens are the exception:
Orq bills them from ``gen_ai.usage.*_tokens_details.*``, so they are written
under that key as well as the semconv one.
"""

from typing import Any, Dict, Mapping, NamedTuple, Optional, Tuple

from .constants import SPAN_TYPE_OPERATIONS


class Rule(NamedTuple):
    semconv_key: str
    kind: type  # int, float (any real number) or str
    billing_key: Optional[str] = None  # remove once BOPS-1505 ships


# span.log() key -> how it is exported.
RULES: Dict[str, Rule] = {
    "request.provider": Rule("gen_ai.provider.name", str),
    "request.model": Rule("gen_ai.request.model", str),
    "request.temperature": Rule("gen_ai.request.temperature", float),
    "request.top_p": Rule("gen_ai.request.top_p", float),
    "request.max_tokens": Rule("gen_ai.request.max_tokens", int),
    "request.frequency_penalty": Rule("gen_ai.request.frequency_penalty", float),
    "request.presence_penalty": Rule("gen_ai.request.presence_penalty", float),
    "request.seed": Rule("gen_ai.request.seed", int),
    "metrics.prompt_tokens": Rule("gen_ai.usage.input_tokens", int),
    "metrics.completion_tokens": Rule("gen_ai.usage.output_tokens", int),
    "metrics.prompt_tokens_details.cached_tokens": Rule(
        "gen_ai.usage.cache_read.input_tokens", int, "gen_ai.usage.prompt_tokens_details.cached_tokens"
    ),
    "metrics.completion_tokens_details.reasoning_tokens": Rule(
        "gen_ai.usage.reasoning.output_tokens", int, "gen_ai.usage.completion_tokens_details.reasoning_tokens"
    ),
}


def _coerce(value: Any, kind: type) -> Tuple[bool, Any]:
    """(fits, value as ``kind``). ``76.0`` fits int; bools and strings never fit a number."""
    if isinstance(value, bool):
        return False, value
    if kind is str:
        return isinstance(value, str), value
    if isinstance(value, int):
        return True, value
    if isinstance(value, float) and kind is float:
        return True, value
    if isinstance(value, float) and value.is_integer():
        return True, int(value)
    return False, value


def to_genai(attributes: Mapping[str, Any], span_type: str, span_name: str) -> Dict[str, Any]:
    """Return ``attributes`` with semconv names, plus the Orq billing keys.

    A key the caller set explicitly is never overwritten.
    """
    out: Dict[str, Any] = {}
    for key, value in attributes.items():
        rule = RULES.get(key)
        fits, coerced = _coerce(value, rule.kind) if rule else (False, value)
        if rule and fits and rule.semconv_key not in attributes:
            out[rule.semconv_key] = coerced
        else:
            out[key] = value

    for rule in RULES.values():
        if rule.billing_key is None:
            continue
        if rule.semconv_key in out:
            out.setdefault(rule.billing_key, out[rule.semconv_key])
        elif rule.billing_key in out:
            out[rule.semconv_key] = out[rule.billing_key]

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
