"""Convert completed LangChain events to OTLP-compatible span dicts.

Produces the same JSON structure as OpenTelemetry's OTLPSpanExporter
(resourceSpans > scopeSpans > spans) so the backend's LangSmith adapter
can parse it. Detection keys: scope.name="langsmith", langsmith.span.kind,
and root span with empty parentSpanId -> SpanTypes.Trace.
"""

import json
import time
from typing import Any, Dict, List, Optional

from ._models import EventType, InFlightEvent


def _nano_timestamp() -> str:
    """Current time as nanoseconds since epoch string."""
    return str(int(time.time() * 1_000_000_000))


# ── OTLP attribute encoding ──────────────────────────────────────

def _str_attr(key: str, value: str) -> Dict[str, Any]:
    return {"key": key, "value": {"stringValue": value}}


def _int_attr(key: str, value: int) -> Dict[str, Any]:
    return {"key": key, "value": {"intValue": str(value)}}


def _bool_attr(key: str, value: bool) -> Dict[str, Any]:
    return {"key": key, "value": {"boolValue": value}}


def _double_attr(key: str, value: float) -> Dict[str, Any]:
    return {"key": key, "value": {"doubleValue": value}}


def _array_attr(key: str, values: List[str]) -> Dict[str, Any]:
    return {
        "key": key,
        "value": {
            "arrayValue": {
                "values": [{"stringValue": v} for v in values]
            }
        },
    }


def _encode_attr(key: str, value: Any) -> Dict[str, Any]:
    """Encode a single attribute value in OTLP format."""
    if isinstance(value, bool):
        return _bool_attr(key, value)
    elif isinstance(value, int):
        return _int_attr(key, value)
    elif isinstance(value, float):
        return _double_attr(key, value)
    elif isinstance(value, list):
        return _array_attr(key, [str(v) for v in value])
    else:
        return _str_attr(key, str(value))


# ── Span kind mapping ────────────────────────────────────────────

_SPAN_KIND_MAP = {
    EventType.LLM: "llm",
    EventType.CHAIN: "chain",
    EventType.AGENT: "chain",
    EventType.TOOL: "tool",
    EventType.RETRIEVAL: "chain",
}

_OPERATION_NAME_MAP = {
    EventType.LLM: "chat",
    EventType.CHAIN: "chain",
    EventType.AGENT: "chain",
    EventType.TOOL: "execute_tool",
    EventType.RETRIEVAL: "chain",
}


# ── Build a single OTLP span ────────────────────────────────────

def build_otlp_span(event: InFlightEvent) -> Dict[str, Any]:
    """Convert a completed InFlightEvent to an OTLP span dict."""
    langsmith_kind = _SPAN_KIND_MAP.get(event.event_type, "chain")
    operation_name = _OPERATION_NAME_MAP.get(event.event_type, "chain")

    if event.event_type == EventType.LLM:
        operation_name = "chat" if event.messages else "completion"

    attrs = _build_attributes(event, langsmith_kind, operation_name)

    span: Dict[str, Any] = {
        "traceId": event.trace_id,
        "spanId": event.run_id,
        "traceState": "",
        "parentSpanId": event.parent_run_id or "",
        "name": event.name,
        "kind": 1,  # SPAN_KIND_INTERNAL
        "startTimeUnixNano": event.start_time_ns or _nano_timestamp(),
        "endTimeUnixNano": event.end_time_ns or _nano_timestamp(),
        "attributes": attrs,
        "droppedAttributesCount": 0,
        "events": _build_events(event),
        "droppedEventsCount": 0,
        "links": [],
        "droppedLinksCount": 0,
        "status": {"message": "", "code": 1},
    }

    if event.error:
        span["status"] = {"message": event.error.get("message", ""), "code": 2}

    return span


def _build_attributes(
    event: InFlightEvent, langsmith_kind: str, operation_name: str
) -> List[Dict[str, Any]]:
    """Build OTLP-formatted attribute list."""
    attrs: List[Dict[str, Any]] = []

    # Core attributes that drive adapter detection + span type mapping
    attrs.append(_str_attr("langsmith.span.kind", langsmith_kind))
    attrs.append(_str_attr("langsmith.trace.name", event.name))
    attrs.append(_str_attr("langsmith.trace.session_name", "default"))
    attrs.append(_str_attr("gen_ai.operation.name", operation_name))
    attrs.append(_str_attr("gen_ai.system", _extract_provider(event.serialized) or "langchain"))

    # LLM-specific attributes
    if event.event_type == EventType.LLM:
        _add_llm_attributes(attrs, event)

    # Tool-specific
    if event.event_type == EventType.TOOL:
        tool_name = event.serialized.get("name") if event.serialized else None
        if tool_name:
            attrs.append(_str_attr("gen_ai.serialized.name", tool_name))

    # Metadata passthrough
    if event.metadata:
        for k, v in event.metadata.items():
            attrs.append(_encode_attr(f"langsmith.metadata.{k}", v))

    # Tags
    if event.tags:
        for tag in event.tags:
            attrs.append(_str_attr("langsmith.span.tags", tag))

    # Input as gen_ai.prompt (JSON-encoded string)
    prompt = _build_prompt(event)
    if prompt is not None:
        attrs.append(_str_attr("gen_ai.prompt", json.dumps(prompt, default=str)))

    # Output as gen_ai.completion (JSON-encoded string)
    completion = _build_completion(event)
    if completion is not None:
        attrs.append(_str_attr("gen_ai.completion", json.dumps(completion, default=str)))

    return attrs


def _add_llm_attributes(attrs: List[Dict[str, Any]], event: InFlightEvent) -> None:
    """Add gen_ai.* attributes for LLM spans."""
    if event.model_name:
        attrs.append(_str_attr("gen_ai.serialized.name", event.name))
        attrs.append(_str_attr("gen_ai.request.model", event.model_name))

    provider = _extract_provider(event.serialized)
    if provider:
        # Override gen_ai.system with actual provider
        for i, a in enumerate(attrs):
            if a["key"] == "gen_ai.system":
                attrs[i] = _str_attr("gen_ai.system", provider)
                break

    # Model parameters as langsmith.metadata.*
    if event.model_parameters:
        for k, v in event.model_parameters.items():
            if v is not None:
                attrs.append(_encode_attr(f"langsmith.metadata.{k}", v))

    # ls_* metadata fields for adapter extraction
    if event.metadata:
        if "ls_provider" not in event.metadata and provider:
            attrs.append(_str_attr("langsmith.metadata.ls_provider", provider))
        if "ls_model_name" not in event.metadata and event.model_name:
            attrs.append(_str_attr("langsmith.metadata.ls_model_name", event.model_name))
        if "ls_model_type" not in event.metadata:
            attrs.append(_str_attr("langsmith.metadata.ls_model_type", "chat" if event.messages else "completion"))

    # Token usage as top-level gen_ai.usage.* attributes
    if event.token_usage:
        usage = event.token_usage
        if "prompt_tokens" in usage:
            attrs.append(_int_attr("gen_ai.usage.input_tokens", usage["prompt_tokens"]))
        if "completion_tokens" in usage:
            attrs.append(_int_attr("gen_ai.usage.output_tokens", usage["completion_tokens"]))
        if "total_tokens" in usage:
            attrs.append(_int_attr("gen_ai.usage.total_tokens", usage["total_tokens"]))


def _extract_provider(serialized: Optional[Dict[str, Any]]) -> Optional[str]:
    """Extract the provider name from serialized data."""
    if not serialized:
        return None
    id_parts = serialized.get("id", [])
    for part in id_parts:
        part_lower = str(part).lower()
        for provider in ("openai", "anthropic", "google", "cohere", "mistral", "bedrock", "azure"):
            if provider in part_lower:
                return provider
    return None


def _build_prompt(event: InFlightEvent) -> Optional[Any]:
    """Build gen_ai.prompt value."""
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


def _build_completion(event: InFlightEvent) -> Optional[Any]:
    """Build gen_ai.completion value."""
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
    """Build OTEL-style events (for errors)."""
    events: List[Dict[str, Any]] = []
    if event.error:
        events.append({
            "timeUnixNano": event.end_time_ns or _nano_timestamp(),
            "name": "exception",
            "attributes": [
                _str_attr("exception.type", event.error.get("type", "Exception")),
                _str_attr("exception.message", event.error.get("message", "")),
                _str_attr("exception.stacktrace", event.error.get("traceback", "")),
            ],
            "droppedAttributesCount": 0,
        })
    return events


# ── Wrap spans in the full OTLP envelope ─────────────────────────

def wrap_in_otlp_envelope(spans: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Wrap span dicts in the full resourceSpans > scopeSpans > spans structure.

    Matches the exact format that the OTLP protobuf/JSON exporter produces,
    with scope.name="langsmith" so the backend's LangSmith adapter detects it.
    """
    return {
        "resourceSpans": [
            {
                "resource": {
                    "attributes": [
                        _str_attr("telemetry.sdk.language", "python"),
                        _str_attr("telemetry.sdk.name", "opentelemetry"),
                        _str_attr("telemetry.sdk.version", "1.39.1"),
                        _str_attr("service.name", "unknown_service"),
                    ],
                    "droppedAttributesCount": 0,
                },
                "scopeSpans": [
                    {
                        "scope": {
                            "name": "langsmith",
                            "version": "",
                            "attributes": [],
                            "droppedAttributesCount": 0,
                        },
                        "spans": spans,
                    }
                ],
            }
        ]
    }
