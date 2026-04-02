"""Convert completed LangChain events to OTLP-compatible span dicts."""

from typing import Any, Dict, List, Optional

from ._models import EventType, InFlightEvent
from ._utils import get_iso_string


# Maps EventType -> (langsmith.span.kind, orq span type field)
_SPAN_KIND_MAP = {
    EventType.LLM: ("llm", "llm"),
    EventType.CHAIN: ("chain", "function"),
    EventType.AGENT: ("agent", "agent"),
    EventType.TOOL: ("tool", "tool"),
    EventType.RETRIEVAL: ("retriever", "retrieval"),
}


def build_span(event: InFlightEvent) -> Dict[str, Any]:
    """Convert a completed InFlightEvent to an OTLP-compatible span dict."""
    langsmith_kind, span_type = _SPAN_KIND_MAP.get(
        event.event_type, ("chain", "function")
    )

    span: Dict[str, Any] = {
        "context": {
            "trace_id": event.trace_id or event.run_id,
            "span_id": event.run_id,
        },
        "name": event.name,
        "type": span_type,
        "start_time": event.start_time_iso,
        "end_time": event.end_time_iso or get_iso_string(),
        "attributes": _build_attributes(event, langsmith_kind),
        "events": _build_events(event),
    }

    if event.parent_run_id:
        span["parent_id"] = event.parent_run_id

    span_input = _build_input(event)
    if span_input is not None:
        span["input"] = span_input

    span_output = _build_output(event)
    if span_output is not None:
        span["output"] = span_output

    return span


def _build_attributes(event: InFlightEvent, langsmith_kind: str) -> Dict[str, Any]:
    """Build span attributes with gen_ai.* and langsmith.* keys."""
    attrs: Dict[str, Any] = {
        "langsmith.span.kind": langsmith_kind,
        "orq.span.kind": event.event_type.value,
    }

    if event.event_type == EventType.LLM:
        _add_llm_attributes(attrs, event)
    elif event.event_type == EventType.TOOL:
        tool_name = event.serialized.get("name") if event.serialized else None
        if tool_name:
            attrs["gen_ai.tool.name"] = tool_name

    # Metadata passthrough
    if event.metadata:
        for k, v in event.metadata.items():
            attrs[f"langsmith.metadata.{k}"] = v

    # Tags
    if event.tags:
        attrs["langsmith.tags"] = event.tags

    return attrs


def _add_llm_attributes(attrs: Dict[str, Any], event: InFlightEvent) -> None:
    """Add gen_ai.* attributes for LLM spans."""
    if event.model_name:
        attrs["gen_ai.request.model"] = event.model_name

    if event.model_parameters:
        param_map = {
            "temperature": "gen_ai.request.temperature",
            "max_tokens": "gen_ai.request.max_tokens",
            "top_p": "gen_ai.request.top_p",
            "top_k": "gen_ai.request.top_k",
            "frequency_penalty": "gen_ai.request.frequency_penalty",
            "presence_penalty": "gen_ai.request.presence_penalty",
        }
        for param_key, attr_key in param_map.items():
            if param_key in event.model_parameters:
                attrs[attr_key] = event.model_parameters[param_key]

    # Provider extraction from serialized
    provider = _extract_provider(event.serialized)
    if provider:
        attrs["gen_ai.system"] = provider

    # Operation name
    attrs["gen_ai.operation.name"] = "chat" if event.messages else "completion"

    # Token usage
    if event.token_usage:
        usage = event.token_usage
        attrs["gen_ai.usage.input_tokens"] = usage.get("prompt_tokens", 0)
        attrs["gen_ai.usage.output_tokens"] = usage.get("completion_tokens", 0)
        attrs["gen_ai.usage.total_tokens"] = usage.get("total_tokens", 0)
        if "cached_tokens" in usage:
            attrs["gen_ai.usage.prompt_tokens_details.cached_tokens"] = usage["cached_tokens"]
        if "reasoning_tokens" in usage:
            attrs["gen_ai.usage.completion_tokens_details.reasoning_tokens"] = usage["reasoning_tokens"]

    # Also store as metrics for the traced pipeline
    if event.token_usage:
        attrs["metrics"] = {
            "prompt_tokens": event.token_usage.get("prompt_tokens", 0),
            "completion_tokens": event.token_usage.get("completion_tokens", 0),
            "tokens": event.token_usage.get("total_tokens", 0),
        }

    if event.model_name:
        request: Dict[str, Any] = {"model": event.model_name}
        if provider:
            request["provider"] = provider
        if event.model_parameters:
            request.update(event.model_parameters)
        attrs["request"] = request


def _extract_provider(serialized: Dict[str, Any]) -> Optional[str]:
    """Extract the provider name from serialized data."""
    # Check serialized.id list for known provider patterns
    id_parts = serialized.get("id", [])
    for part in id_parts:
        part_lower = str(part).lower()
        for provider in ("openai", "anthropic", "google", "cohere", "mistral", "bedrock", "azure"):
            if provider in part_lower:
                return provider
    return None


def _build_input(event: InFlightEvent) -> Optional[Any]:
    """Build the input field based on event type."""
    if event.event_type == EventType.LLM:
        if event.messages:
            return {"messages": event.messages}
        elif event.prompts:
            return {"prompts": event.prompts}
    elif event.event_type in (EventType.CHAIN, EventType.AGENT):
        return event.inputs
    elif event.event_type == EventType.TOOL:
        if event.tool_input is not None:
            return {"input": event.tool_input}
    elif event.event_type == EventType.RETRIEVAL:
        if event.query is not None:
            return {"query": event.query}
    return None


def _build_output(event: InFlightEvent) -> Optional[Any]:
    """Build the output field based on event type."""
    if event.event_type == EventType.LLM:
        output: Dict[str, Any] = {}
        if event.response_choices:
            output["choices"] = event.response_choices
        if event.token_usage:
            output["usage"] = event.token_usage
        return output if output else None
    elif event.event_type in (EventType.CHAIN, EventType.AGENT):
        return event.outputs
    elif event.event_type == EventType.TOOL:
        if event.tool_output is not None:
            return {"output": event.tool_output}
    elif event.event_type == EventType.RETRIEVAL:
        if event.documents is not None:
            return {"documents": event.documents}
    return None


def _build_events(event: InFlightEvent) -> List[Dict[str, Any]]:
    """Build OTEL-style events (mainly for errors)."""
    events: List[Dict[str, Any]] = []
    if event.error:
        events.append({
            "name": "exception",
            "timestamp": event.end_time_iso or get_iso_string(),
            "attributes": {
                "exception.type": event.error.get("type", "Exception"),
                "exception.message": event.error.get("message", ""),
                "exception.stacktrace": event.error.get("traceback", ""),
            },
        })
    return events
