"""Shared helpers for the LangChain callback integration."""

import logging
import traceback
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

logger = logging.getLogger("orq_ai_sdk.langchain")


def get_iso_string() -> str:
    """Get current datetime in UTC as ISO 8601 string."""
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def extract_model_name(
    serialized: Dict[str, Any], kwargs: Dict[str, Any]
) -> Optional[str]:
    """Try multiple paths to extract the model name."""
    # serialized.kwargs paths
    ser_kwargs = serialized.get("kwargs", {})
    for key in ("model_name", "model"):
        if key in ser_kwargs:
            return ser_kwargs[key]

    # serialized.name
    if "name" in serialized:
        return serialized["name"]

    # invocation_params paths
    inv = kwargs.get("invocation_params", {})
    for key in ("model_name", "model"):
        if key in inv:
            return inv[key]

    return None


def extract_model_parameters(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Pull model parameters from invocation_params."""
    inv = kwargs.get("invocation_params", {})
    params: Dict[str, Any] = {}
    for key in (
        "temperature",
        "max_tokens",
        "top_p",
        "top_k",
        "frequency_penalty",
        "presence_penalty",
        "seed",
    ):
        if key in inv:
            params[key] = inv[key]
    return params


def normalize_messages(messages: List[List[Any]]) -> List[Dict[str, Any]]:
    """Normalize all LangChain message types to dicts."""
    from langchain_core.messages import (  # type: ignore  # pylint: disable=import-error,import-outside-toplevel
        AIMessage,
        ChatMessage,
        FunctionMessage,
        HumanMessage,
        SystemMessage,
        ToolMessage,
    )

    result: List[Dict[str, Any]] = []
    for group in messages:
        for msg in group:
            if isinstance(msg, HumanMessage):
                result.append({"role": "user", "content": msg.content})
            elif isinstance(msg, SystemMessage):
                result.append({"role": "system", "content": msg.content})
            elif isinstance(msg, AIMessage):
                entry: Dict[str, Any] = {
                    "role": "assistant",
                    "content": msg.content,
                }
                tool_calls = getattr(msg, "tool_calls", None) or msg.additional_kwargs.get("tool_calls")
                if tool_calls:
                    entry["tool_calls"] = tool_calls
                result.append(entry)
            elif isinstance(msg, ToolMessage):
                result.append({
                    "role": "tool",
                    "content": msg.content,
                    "tool_call_id": getattr(msg, "tool_call_id", None),
                })
            elif isinstance(msg, FunctionMessage):
                result.append({
                    "role": "function",
                    "content": msg.content,
                    "name": msg.name,
                })
            elif isinstance(msg, ChatMessage):
                result.append({"role": msg.role, "content": msg.content})
            else:
                result.append({"role": "unknown", "content": str(msg.content)})
    return result


def extract_assistant_tool_calls(message: Any) -> Optional[List[Any]]:
    """Extract tool_calls from a LangChain message, supporting both OpenAI and LangChain shapes."""
    if message is None:
        return None

    additional_kwargs = getattr(message, "additional_kwargs", None)
    if isinstance(additional_kwargs, dict):
        from_kwargs = additional_kwargs.get("tool_calls")
        if isinstance(from_kwargs, list) and from_kwargs:
            return from_kwargs

    from_message = getattr(message, "tool_calls", None)
    if isinstance(from_message, list) and from_message:
        return from_message

    return None


def extract_token_usage(response: Any) -> Optional[Dict[str, Any]]:
    """Robustly extract token usage from LLMResult.

    LangChain places usage in different locations depending on call mode:
    non-streaming chat populates ``response.llm_output["token_usage"]``,
    while streaming chat populates ``response.generations[0][0].message.usage_metadata``
    (the standardized langchain-core ``UsageMetadata`` shape). Both are
    checked so streaming runs do not silently drop usage attributes.
    """
    llm_output = getattr(response, "llm_output", None) or {}
    usage = llm_output.get("token_usage") or llm_output.get("usage")

    if not usage:
        usage_metadata = None
        try:
            generations = getattr(response, "generations", None) or []
            message = getattr(generations[0][0], "message", None)
            usage_metadata = getattr(message, "usage_metadata", None)
        except (AttributeError, IndexError):
            pass

        if usage_metadata:
            usage = {
                "prompt_tokens": usage_metadata.get("input_tokens", 0),
                "completion_tokens": usage_metadata.get("output_tokens", 0),
                "total_tokens": usage_metadata.get("total_tokens", 0),
            }
            input_details = usage_metadata.get("input_token_details")
            if isinstance(input_details, dict) and "cache_read" in input_details:
                usage["prompt_tokens_details"] = {"cached_tokens": input_details["cache_read"]}
            output_details = usage_metadata.get("output_token_details")
            if isinstance(output_details, dict) and "reasoning" in output_details:
                usage["completion_tokens_details"] = {"reasoning_tokens": output_details["reasoning"]}

    if not usage:
        return None

    result: Dict[str, Any] = {}

    # Standard keys
    result["prompt_tokens"] = usage.get("prompt_tokens") or usage.get("input_tokens", 0)
    result["completion_tokens"] = usage.get("completion_tokens") or usage.get("output_tokens", 0)
    result["total_tokens"] = usage.get("total_tokens", result["prompt_tokens"] + result["completion_tokens"])

    # Optional detailed usage
    cached = usage.get("prompt_tokens_details", {}).get("cached_tokens") if isinstance(usage.get("prompt_tokens_details"), dict) else None
    if cached is not None:
        result["cached_tokens"] = cached

    reasoning = usage.get("completion_tokens_details", {}).get("reasoning_tokens") if isinstance(usage.get("completion_tokens_details"), dict) else None
    if reasoning is not None:
        result["reasoning_tokens"] = reasoning

    return result


def coerce_chain_payload(payload: Any) -> Dict[str, Any]:
    """Wrap chain inputs/outputs into a dict suitable for the span normalizer.

    LangChain hands callbacks raw BaseMessage objects (or lists thereof) for
    chains like RunnableSequence wrapping a chat model. Without coercion they
    get stored as ``{"outputs": <AIMessage>}`` and serialized via ``__str__``,
    producing an unreadable Python repr in the trace. Wrapping them as
    ``{"messages": [...]}`` routes through the normal role/tool_calls path.
    """
    if isinstance(payload, dict):
        return payload

    try:
        from langchain_core.messages import BaseMessage  # type: ignore  # pylint: disable=import-error,import-outside-toplevel
    except ImportError:
        return {"outputs": payload}

    if isinstance(payload, BaseMessage):
        return {"messages": [payload]}
    if isinstance(payload, list) and payload and all(
        isinstance(m, BaseMessage) for m in payload
    ):
        return {"messages": payload}
    return {"outputs": payload}


def root_output_delta(
    inputs: Optional[Dict[str, Any]],
    outputs: Dict[str, Any],
) -> Dict[str, Any]:
    """Return outputs with input messages stripped from outputs['messages'].

    LangGraph's root on_chain_end receives the full merged state, so the
    input turns reappear in outputs['messages']. Use message ids when every
    input has one (handles RemoveMessage correctly); otherwise fall back to
    positional trimming, which is safe under the append-only add_messages
    reducer LangGraph uses by default.
    """
    if not isinstance(inputs, dict) or not isinstance(outputs, dict):
        return outputs
    in_msgs = inputs.get("messages")
    out_msgs = outputs.get("messages")
    if not isinstance(in_msgs, list) or not isinstance(out_msgs, list) or not out_msgs:
        return outputs

    def _id_of(msg: Any) -> Optional[str]:
        if isinstance(msg, dict):
            return msg.get("id")
        return getattr(msg, "id", None)

    in_ids = [_id_of(m) for m in in_msgs]
    if in_msgs and all(mid for mid in in_ids):
        input_id_set = set(in_ids)
        delta = [m for m in out_msgs if _id_of(m) not in input_id_set]
        return {**outputs, "messages": delta}

    if len(out_msgs) >= len(in_msgs):
        return {**outputs, "messages": out_msgs[len(in_msgs):]}
    return outputs


def resolve_span_name(
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    serialized: Optional[Dict[str, Any]] = None,
    fallback: str = "LangGraph",
) -> str:
    """Resolve span name from multiple sources.

    Priority: explicit name > serialized name > last element of serialized
    id list > langgraph_node metadata > fallback.
    """
    if name:
        return name
    if serialized:
        if serialized.get("name"):
            return serialized["name"]
        id_list = serialized.get("id") or []
        if id_list:
            return id_list[-1]
    if metadata and metadata.get("langgraph_node"):
        return metadata["langgraph_node"]
    return fallback


def format_error(error: BaseException) -> Dict[str, str]:
    """Format an error with traceback."""
    return {
        "message": str(error),
        "traceback": "".join(traceback.format_exception(type(error), error, error.__traceback__)),
    }


def nano_timestamp() -> str:
    """Return current time as nanoseconds since epoch string."""
    return str(int(time.time() * 1_000_000_000))
