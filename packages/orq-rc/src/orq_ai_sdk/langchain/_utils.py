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
    from langchain_core.messages import (  # type: ignore
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


def extract_token_usage(response: Any) -> Optional[Dict[str, Any]]:
    """Robustly extract token usage from LLMResult."""
    llm_output = getattr(response, "llm_output", None)
    if not llm_output:
        return None

    usage = llm_output.get("token_usage") or llm_output.get("usage")
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
