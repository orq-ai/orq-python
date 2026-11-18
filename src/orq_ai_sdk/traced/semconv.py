"""OTel GenAI semantic-convention names for @traced span attributes.

The Orq ingest reads the decorator's own keys (``type``, ``request.*``,
``metrics.*``, ``input`` / ``output``). OTel GenAI tooling reads ``gen_ai.*``.
Where the two differ, the value is written under both names.
"""

from typing import Any, Dict, Mapping

# span.type -> gen_ai.operation.name. "function" has no GenAI operation.
OPERATION_NAMES = {
    "agent": "invoke_agent",
    "embedding": "embeddings",
    "llm": "chat",
    "retrieval": "retrieval",
    "tool": "execute_tool",
}

# (Orq key, semconv key). Whichever one is set is copied to the other.
ATTRIBUTE_ALIASES = (
    ("request.provider", "gen_ai.provider.name"),
    ("request.model", "gen_ai.request.model"),
    ("request.temperature", "gen_ai.request.temperature"),
    ("request.top_p", "gen_ai.request.top_p"),
    ("request.max_tokens", "gen_ai.request.max_tokens"),
    ("request.frequency_penalty", "gen_ai.request.frequency_penalty"),
    ("request.presence_penalty", "gen_ai.request.presence_penalty"),
    ("request.seed", "gen_ai.request.seed"),
    ("metrics.prompt_tokens", "gen_ai.usage.input_tokens"),
    ("metrics.completion_tokens", "gen_ai.usage.output_tokens"),
    ("metrics.prompt_tokens_details.cached_tokens", "gen_ai.usage.cache_read.input_tokens"),
    ("metrics.completion_tokens_details.reasoning_tokens", "gen_ai.usage.reasoning.output_tokens"),
)

# Semconv types these as int; a string seed stays under the Orq key only.
_INT_ONLY = {"gen_ai.request.seed"}


def genai_aliases(attributes: Mapping[str, Any], span_type: str, span_name: str) -> Dict[str, Any]:
    """Return the keys to add so each value is present under both names.

    Never overrides a key that is already set.
    """
    extra: Dict[str, Any] = {}
    for orq_key, semconv_key in ATTRIBUTE_ALIASES:
        if orq_key in attributes and semconv_key not in attributes:
            value = attributes[orq_key]
            if semconv_key not in _INT_ONLY or (isinstance(value, int) and not isinstance(value, bool)):
                extra[semconv_key] = value
        elif semconv_key in attributes and orq_key not in attributes:
            extra[orq_key] = attributes[semconv_key]

    def add(key: str, value: Any) -> None:
        if key not in attributes:
            extra[key] = value

    operation = OPERATION_NAMES.get(span_type)
    if operation:
        add("gen_ai.operation.name", operation)
    if span_type == "agent":
        add("gen_ai.agent.name", span_name)
    if span_type == "tool":
        add("gen_ai.tool.name", span_name)
        add("gen_ai.tool.type", "function")
    return extra


def error_type(error: BaseException) -> str:
    """Fully qualified exception class name, as semconv ``error.type`` expects."""
    cls = type(error)
    if cls.__module__ == "builtins":
        return cls.__qualname__
    return f"{cls.__module__}.{cls.__qualname__}"
