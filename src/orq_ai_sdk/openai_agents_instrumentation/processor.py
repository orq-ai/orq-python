"""Orq Custom OpenAI Agents tracing processor with enhanced agent span support."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union, cast

from .constants import GenAIOperation, SpanAttributes

if TYPE_CHECKING:
    from openai.types.responses import (
        ResponseComputerToolCall,
        ResponseFileSearchToolCall,
        ResponseFunctionToolCall,
        ResponseFunctionWebSearch,
        ResponseOutputMessage,
    )
    from openai.types.responses.response_code_interpreter_tool_call import (
        ResponseCodeInterpreterToolCall,
    )
    from openai.types.responses.response_output_item import (
        ImageGenerationCall,
        LocalShellCall,
        McpApprovalRequest,
        McpCall,
        McpListTools,
    )
    from openai.types.responses.response_reasoning_item import ResponseReasoningItem

# Type aliases for better clarity
SemconvParts = List[Dict[str, object]]
SemconvMessages = List[Dict[str, object]]
SpanOutputData = Union[
    str,
    List[Dict[str, object]],
    Dict[str, object],
    List[
        Union[
            "ResponseOutputMessage",
            "ResponseFileSearchToolCall",
            "ResponseFunctionToolCall",
            "ResponseFunctionWebSearch",
            "ResponseComputerToolCall",
            "ResponseCodeInterpreterToolCall",
            "ImageGenerationCall",
            "LocalShellCall",
            "McpApprovalRequest",
            "McpCall",
            "McpListTools",
            "ResponseReasoningItem",
        ]
    ],
]
UsageData = object
ErrorData = Optional[Dict[str, object]]

# Try to import required dependencies
try:
    from agents.tracing import Span, Trace, TracingProcessor  # type: ignore[import-not-found]
    from agents.tracing.span_data import (  # type: ignore[import-not-found]
        AgentSpanData,
        FunctionSpanData,
        GenerationSpanData,
        HandoffSpanData,
        ResponseSpanData,
        SpanData,
    )
except ImportError as exc:
    raise ImportError(
        "OpenAI Agents not available. Install with: pip install openai-agents"
    ) from exc

try:
    from opentelemetry.context import Context, attach, detach
    from opentelemetry.context import Token as ContextToken  # type: ignore[attr-defined]
    from opentelemetry.trace import Span as OtelSpan
    from opentelemetry.trace import SpanKind as OtelSpanKind
    from opentelemetry.trace import (
        Status,
        StatusCode,
        Tracer,
        set_span_in_context,
    )
except ImportError as exc:
    raise ImportError(
        "OpenTelemetry not available. Install with: pip install opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation"
    ) from exc


class EnhancedOpenAIAgentsProcessor(TracingProcessor):
    """Enhanced tracing processor that adds input/output to agent spans."""

    def __init__(self, tracer: Tracer) -> None:
        self._tracer = tracer
        self._root_spans: dict[str, OtelSpan] = {}
        self._otel_spans: dict[str, OtelSpan] = {}
        self._tokens: dict[str, ContextToken[Context]] = {}
        # Track agent spans and their child spans to aggregate input/output
        self._agent_spans: dict[str, str] = {}  # span_id -> agent_name
        self._span_hierarchy: dict[str, str] = {}  # child_span_id -> parent_agent_span_id
        self._agent_inputs: Dict[str, Optional[SemconvMessages]] = {}  # agent_span_id -> first LLM input
        self._agent_outputs: Dict[str, Optional[SpanOutputData]] = {}  # agent_span_id -> last LLM output
        # User metadata captured from response.metadata on LLM calls. Cached
        # per trace so we can bubble it onto the workflow root span at
        # on_trace_end — Orq's traces-list Metadata column reads from the
        # leading row, which is the root, not the LLM child.
        self._trace_metadata: Dict[str, Dict[str, Any]] = {}
        # FunctionSpanData has no call id, so tool spans take theirs from the
        # response span, which carries the ids and always ends first.
        self._pending_tool_call_ids: Dict[str, Dict[str, List[Optional[str]]]] = {}  # scope -> tool name -> ids
        self._tool_call_ids: Dict[str, str] = {}  # function span id -> id

    def on_trace_start(self, trace: Trace) -> None:
        """Called when a trace is started."""
        otel_span = self._tracer.start_span(
            name=f"{GenAIOperation.INVOKE_WORKFLOW.value} {trace.name}",
            attributes={
                SpanAttributes.OPERATION_NAME.value: GenAIOperation.INVOKE_WORKFLOW.value,
                SpanAttributes.WORKFLOW_NAME.value: trace.name,
            },
        )
        self._root_spans[trace.trace_id] = otel_span

    def on_trace_end(self, trace: Trace) -> None:
        """Called when a trace is finished."""
        if root_span := self._root_spans.pop(trace.trace_id, None):
            metadata = self._trace_metadata.pop(trace.trace_id, None)
            if metadata:
                self._apply_metadata_attributes(root_span, metadata)
            root_span.set_status(Status(StatusCode.OK))
            root_span.end()
        else:
            self._trace_metadata.pop(trace.trace_id, None)
        self._pending_tool_call_ids.pop(trace.trace_id, None)

    @staticmethod
    def _apply_metadata_attributes(otel_span: OtelSpan, metadata: Dict[str, Any]) -> None:
        for key, value in metadata.items():
            if value is None:
                continue
            if isinstance(value, (str, bool, int, float)):
                otel_span.set_attribute(f"metadata.{key}", value)
            else:
                try:
                    otel_span.set_attribute(f"metadata.{key}", json.dumps(value))
                except (TypeError, ValueError):
                    otel_span.set_attribute(f"metadata.{key}", str(value))

    def on_span_start(self, span: Span[SpanData]) -> None:
        """Called when a span is started."""
        if not span.started_at:
            return

        parent_span = (
            self._otel_spans.get(span.parent_id)
            if span.parent_id
            else self._root_spans.get(span.trace_id)
        )
        context = set_span_in_context(parent_span) if parent_span else None
        attributes: Dict[str, str] = self._get_provider_attributes(span.span_data)
        operation = self._get_operation(span.span_data)
        if operation:
            attributes[SpanAttributes.OPERATION_NAME.value] = operation.value

        otel_span = self._tracer.start_span(
            name=self._get_span_name(span),
            context=context,
            kind=self._get_otel_span_kind(span.span_data),
            start_time=self._as_utc_nano(span.started_at),
            attributes=attributes,
        )
        
        self._otel_spans[span.span_id] = otel_span
        self._tokens[span.span_id] = attach(set_span_in_context(otel_span))
        
        # Track agent spans and hierarchy
        if isinstance(span.span_data, AgentSpanData):
            agent_name = span.span_data.name
            self._agent_spans[span.span_id] = agent_name
            if span.span_id not in self._agent_inputs:
                self._agent_inputs[span.span_id] = None
            if span.span_id not in self._agent_outputs:
                self._agent_outputs[span.span_id] = None
        else:
            # For non-agent spans, find their parent agent span
            parent_agent_span_id = self._find_parent_agent_span(span.parent_id)
            if parent_agent_span_id:
                self._span_hierarchy[span.span_id] = parent_agent_span_id

        # At start: parallel tool spans finish out of order, but start in order.
        if isinstance(span.span_data, FunctionSpanData):
            call_id = self._take_tool_call_id(
                self._tool_call_scope(span), span.span_data.name
            )
            if call_id:
                self._tool_call_ids[span.span_id] = call_id

    def on_span_end(self, span: Span[SpanData]) -> None:
        """Called when a span is finished."""
        if token := self._tokens.pop(span.span_id, None):
            detach(token)
        if not (otel_span := self._otel_spans.pop(span.span_id, None)):
            return

        # Response spans only learn their model at the end.
        otel_span.update_name(self._get_span_name(span))
        data = span.span_data

        # Handle different span types and collect input/output for agent spans
        if isinstance(data, AgentSpanData):
            self._handle_agent_span(otel_span, data, span.span_id)
        elif isinstance(data, ResponseSpanData):
            self._handle_response_span(otel_span, data, getattr(span, "trace_id", None))
            self._record_tool_call_ids(span, data)
            self._collect_agent_data(span.span_id, data, "input", "output")
        elif isinstance(data, GenerationSpanData):
            self._handle_generation_span(otel_span, data)
            self._collect_agent_data(span.span_id, data, "input", "output")
        elif isinstance(data, FunctionSpanData):
            self._handle_function_span(otel_span, data, span.span_id)
        elif isinstance(data, HandoffSpanData):
            self._handle_handoff_span(otel_span, data)

        end_time: Optional[int] = None
        if span.ended_at:
            try:
                end_time = self._as_utc_nano(span.ended_at)
            except ValueError:
                pass

        otel_span.set_status(status=self._get_span_status(span))
        otel_span.end(end_time)

    def _handle_agent_span(self, otel_span: OtelSpan, data: AgentSpanData, span_id: str) -> None:
        """Handle agent span with enhanced input/output collection."""
        otel_span.set_attribute(SpanAttributes.GEN_AI_AGENT_NAME.value, data.name)

        # Add first LLM input and last LLM output as JSON strings
        input_messages = self._agent_inputs.get(span_id)
        if input_messages:
            self._set_json_attribute(otel_span, SpanAttributes.INPUT_MESSAGES.value, input_messages)

        output = self._agent_outputs.get(span_id)
        if output is not None:
            output_messages = self._output_messages(output, self._finish_reason(output))
            if output_messages:
                self._set_json_attribute(otel_span, SpanAttributes.OUTPUT_MESSAGES.value, output_messages)

        # Clean up tracking data
        self._agent_spans.pop(span_id, None)
        self._agent_inputs.pop(span_id, None)
        self._agent_outputs.pop(span_id, None)
        self._pending_tool_call_ids.pop(span_id, None)

    def _handle_response_span(self, otel_span: OtelSpan, data: ResponseSpanData, trace_id: Optional[str] = None) -> None:
        """Handle response span."""
        if hasattr(data, "response") and data.response:
            # Extract meaningful data from response instead of dumping the whole object
            response = data.response

            # response.id is the canonical LLM response identifier. When routed through
            # the orq router the id is stamped with a ULID suffix ("gentext_{provider}_{ULID}"),
            # which the traces-processor uses to detect and drop duplicate CLIENT_SPANs.
            if hasattr(response, "id") and response.id:
                otel_span.set_attribute(SpanAttributes.RESPONSE_ID.value, response.id)

            # Set basic response info
            if hasattr(response, "model"):
                otel_span.set_attribute(SpanAttributes.REQUEST_MODEL.value, response.model)
                otel_span.set_attribute(SpanAttributes.RESPONSE_MODEL.value, response.model)

            # Surface user metadata as flat `metadata.{key}` attributes so it
            # lands on the genai_traces row and renders in Orq's traces list
            # Metadata column. The OpenAI Responses API echoes the request's
            # ModelSettings(metadata=...) back on response.metadata. We also
            # cache it under the trace_id so on_trace_end can bubble it onto
            # the workflow root span (the leading row in Orq's traces list).
            metadata = getattr(response, "metadata", None)
            if isinstance(metadata, dict) and metadata:
                self._apply_metadata_attributes(otel_span, metadata)
                if trace_id:
                    self._trace_metadata.setdefault(trace_id, {}).update(metadata)

            # Extract usage information
            if hasattr(response, "usage") and response.usage:
                self._set_usage_attributes(otel_span, response.usage)

            self._set_request_attributes(
                otel_span,
                temperature=getattr(response, "temperature", None),
                top_p=getattr(response, "top_p", None),
                max_tokens=getattr(response, "max_output_tokens", None),
            )

            system_instructions = self._system_instructions(getattr(response, "instructions", None))
            if system_instructions:
                self._set_json_attribute(otel_span, SpanAttributes.SYSTEM_INSTRUCTIONS.value, system_instructions)

            response_output = getattr(response, "output", None)
            incomplete_details = getattr(response, "incomplete_details", None)
            finish_reason = self._finish_reason(response_output, getattr(incomplete_details, "reason", None))
            otel_span.set_attribute(SpanAttributes.RESPONSE_FINISH_REASONS.value, [finish_reason])
            output_messages = self._output_messages(response_output, finish_reason)
            if output_messages:
                self._set_json_attribute(otel_span, SpanAttributes.OUTPUT_MESSAGES.value, output_messages)

        input_messages = self._messages(getattr(data, "input", None))
        if input_messages:
            self._set_json_attribute(otel_span, SpanAttributes.INPUT_MESSAGES.value, input_messages)

    def _handle_generation_span(self, otel_span: OtelSpan, data: GenerationSpanData) -> None:
        """Handle generation span."""
        if hasattr(data, "model") and isinstance(data.model, str):
            otel_span.set_attribute(SpanAttributes.REQUEST_MODEL.value, data.model)

        model_config = getattr(data, "model_config", None)
        if isinstance(model_config, dict):
            self._set_request_attributes(
                otel_span,
                temperature=model_config.get("temperature"),
                top_p=model_config.get("top_p"),
                max_tokens=model_config.get("max_tokens"),
            )

        input_messages = self._messages(getattr(data, "input", None))
        if input_messages:
            self._set_json_attribute(otel_span, SpanAttributes.INPUT_MESSAGES.value, input_messages)

        if hasattr(data, "output") and data.output:
            finish_reason = self._finish_reason(data.output)
            otel_span.set_attribute(SpanAttributes.RESPONSE_FINISH_REASONS.value, [finish_reason])
            output_messages = self._output_messages(data.output, finish_reason)
            if output_messages:
                self._set_json_attribute(otel_span, SpanAttributes.OUTPUT_MESSAGES.value, output_messages)

        # Extract usage information if available
        if hasattr(data, "usage") and data.usage:
            self._set_usage_attributes(otel_span, data.usage)

    def _handle_function_span(
        self, otel_span: OtelSpan, data: FunctionSpanData, span_id: str
    ) -> None:
        """Handle function span."""
        otel_span.set_attribute(SpanAttributes.TOOL_NAME.value, data.name)
        otel_span.set_attribute(SpanAttributes.TOOL_TYPE.value, "function")

        call_id = self._tool_call_ids.pop(span_id, None)
        if call_id:
            otel_span.set_attribute(SpanAttributes.TOOL_CALL_ID.value, call_id)

        if data.input is not None:
            arguments = data.input if isinstance(data.input, str) else str(data.input)
            otel_span.set_attribute(SpanAttributes.TOOL_CALL_ARGUMENTS.value, arguments)

        if data.output is not None:
            result = str(data.output)
            otel_span.set_attribute(SpanAttributes.TOOL_CALL_RESULT.value, result)

    def _handle_handoff_span(self, otel_span: OtelSpan, data: HandoffSpanData) -> None:
        """Handle handoff span."""
        # Additional handoff-specific attributes can be added here if needed

    def _collect_agent_data(self, span_id: str, data: SpanData, *data_types: str) -> None:
        """Collect input/output data for agent spans - first LLM input and last LLM output per agent."""
        # Find the parent agent span for this child span
        parent_agent_span_id = self._span_hierarchy.get(span_id)
        if not parent_agent_span_id:
            return

        for data_type in data_types:
            data_input = getattr(data, "input", None)
            if data_type == "input" and data_input:
                if parent_agent_span_id in self._agent_inputs:
                    # Only capture the first LLM input for this specific agent if none exists yet
                    if self._agent_inputs[parent_agent_span_id] is None:
                        self._agent_inputs[parent_agent_span_id] = self._messages(data_input)
            elif data_type == "output":
                data_output = getattr(data, "output", None)
                if data_output:
                    if parent_agent_span_id in self._agent_outputs:
                        # Always capture the latest LLM output for this specific agent (last one wins)
                        self._agent_outputs[parent_agent_span_id] = data_output
                else:
                    response = getattr(data, "response", None)
                    if response:
                        if parent_agent_span_id in self._agent_outputs:
                            # Extract output from response and always update for this specific agent (last one wins)
                            response_output = getattr(response, "output", None)
                            if response_output:
                                self._agent_outputs[parent_agent_span_id] = response_output

    def _tool_call_scope(self, span: Span[SpanData]) -> str:
        return self._span_hierarchy.get(span.span_id) or span.trace_id

    def _record_tool_call_ids(self, span: Span[SpanData], data: ResponseSpanData) -> None:
        """Queue the ids of the tool calls the model just asked for."""
        response = getattr(data, "response", None)
        output = getattr(response, "output", None) if response else None
        if not isinstance(output, list):
            return

        queues = self._pending_tool_call_ids.setdefault(self._tool_call_scope(span), {})
        for item in output:
            if getattr(item, "type", None) != "function_call":
                continue
            tool_name = getattr(item, "name", None)
            if tool_name:
                # call_id, not item.id ("fc_..."): None keeps the slot so a
                # later call of the same name cannot inherit this id.
                queues.setdefault(tool_name, []).append(getattr(item, "call_id", None))

    def _take_tool_call_id(self, scope: str, tool_name: str) -> Optional[str]:
        queue = self._pending_tool_call_ids.get(scope, {}).get(tool_name)
        if queue:
            return queue.pop(0)
        return None

    def _find_parent_agent_span(self, parent_id: Optional[str]) -> Optional[str]:
        """Find the nearest parent agent span ID."""
        if not parent_id:
            return None
        
        # Check if parent is an agent span
        if parent_id in self._agent_spans:
            return parent_id
            
        # Recursively check up the hierarchy
        return self._span_hierarchy.get(parent_id)

    def _get_span_name(self, span: Span[SpanData]) -> str:
        """Get span name from span data."""
        data = span.span_data

        # Handle HandoffSpanData specifically
        if isinstance(data, HandoffSpanData):
            # Extract target agent name from to_agent attribute
            to_agent = getattr(data, 'to_agent', None)
            if to_agent:
                agent_name = getattr(to_agent, 'name', None)
                if agent_name:
                    return f"handoff to {agent_name}"
                if isinstance(to_agent, str):
                    return f"handoff to {to_agent}"
            return "handoff"

        operation = self._get_operation(data)
        if operation is GenAIOperation.CHAT:
            model = (
                getattr(data.response, "model", None)
                if isinstance(data, ResponseSpanData) and data.response
                else getattr(data, "model", None)
            )
            return f"{operation.value} {model}" if isinstance(model, str) and model else operation.value
        if operation is not None:
            return f"{operation.value} {getattr(data, 'name', '')}".rstrip()

        # Handle other span types with name attribute
        name = getattr(data, "name", None)
        if isinstance(name, str):
            return name
        return getattr(data, "type", "unknown")

    @staticmethod
    def _get_operation(data: SpanData) -> Optional[GenAIOperation]:
        """Handoffs, guardrails and custom spans have no semconv operation."""
        if isinstance(data, AgentSpanData):
            return GenAIOperation.INVOKE_AGENT
        if isinstance(data, FunctionSpanData):
            return GenAIOperation.EXECUTE_TOOL
        if isinstance(data, (ResponseSpanData, GenerationSpanData)):
            return GenAIOperation.CHAT
        return None

    def _get_span_status(self, span: Span[SpanData]) -> Status:
        """Get span status from span error information."""
        error: ErrorData = getattr(span, "error", None)
        if error:
            message = error.get('message', '') if isinstance(error, dict) else ''
            data = error.get('data', '') if isinstance(error, dict) else ''
            return Status(
                status_code=StatusCode.ERROR,
                description=f"{message}: {data}"
            )
        return Status(StatusCode.OK)

    def _set_usage_attributes(self, otel_span: OtelSpan, usage: UsageData) -> None:
        """Set usage-related attributes on the span."""
        input_tokens = self._usage_value(usage, "input_tokens")
        if input_tokens is not None:
            otel_span.set_attribute(SpanAttributes.USAGE_INPUT_TOKENS.value, input_tokens)
        output_tokens = self._usage_value(usage, "output_tokens")
        if output_tokens is not None:
            otel_span.set_attribute(SpanAttributes.USAGE_OUTPUT_TOKENS.value, output_tokens)
        cached_tokens = self._usage_value(self._usage_value(usage, "input_tokens_details"), "cached_tokens")
        if cached_tokens is not None:
            otel_span.set_attribute(SpanAttributes.USAGE_CACHE_READ_INPUT_TOKENS.value, cached_tokens)

    @staticmethod
    def _usage_value(usage: object, key: str) -> Any:
        # Responses usage is an object; generation spans carry a plain dict.
        if isinstance(usage, dict):
            return cast(Dict[str, Any], usage).get(key)
        return getattr(usage, key, None)

    @staticmethod
    def _set_request_attributes(
        otel_span: OtelSpan, temperature: object, top_p: object, max_tokens: object
    ) -> None:
        for attribute, value in (
            (SpanAttributes.REQUEST_TEMPERATURE, temperature),
            (SpanAttributes.REQUEST_TOP_P, top_p),
            (SpanAttributes.REQUEST_MAX_TOKENS, max_tokens),
        ):
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                otel_span.set_attribute(attribute.value, value)

    @staticmethod
    def _set_json_attribute(otel_span: OtelSpan, key: str, value: object) -> None:
        otel_span.set_attribute(key, json.dumps(value, default=str))

    @staticmethod
    def _get_otel_span_kind(data: SpanData) -> OtelSpanKind:
        if isinstance(data, (ResponseSpanData, GenerationSpanData)):
            return OtelSpanKind.CLIENT
        return OtelSpanKind.INTERNAL

    @staticmethod
    def _get_provider_attributes(data: SpanData) -> Dict[str, str]:
        if isinstance(data, ResponseSpanData):
            return {
                SpanAttributes.PROVIDER_NAME.value: "openai",
                SpanAttributes.OPENAI_API_TYPE.value: "responses",
            }
        if isinstance(data, GenerationSpanData):
            model_config = getattr(data, "model_config", None)
            # LiteLLM can route to any provider, so only the OpenAI client is attributed.
            if not (isinstance(model_config, dict) and model_config.get("model_impl") == "litellm"):
                return {
                    SpanAttributes.PROVIDER_NAME.value: "openai",
                    SpanAttributes.OPENAI_API_TYPE.value: "chat_completions",
                }
        return {}

    @staticmethod
    def _as_dict(item: object) -> Optional[Dict[str, Any]]:
        if isinstance(item, dict):
            return cast(Dict[str, Any], item)
        model_dump = getattr(item, "model_dump", None)
        if callable(model_dump):
            dumped = model_dump(exclude_none=True)
            if isinstance(dumped, dict):
                return cast(Dict[str, Any], dumped)
        return None

    def _messages(self, items: object) -> SemconvMessages:
        """Convert Responses input/output items or Chat Completions messages to semconv messages."""
        if isinstance(items, str):
            return [{"role": "user", "parts": [{"type": "text", "content": items}]}] if items else []
        if not isinstance(items, list):
            return []
        messages: SemconvMessages = []
        for raw_item in cast(List[object], items):
            item = self._as_dict(raw_item)
            message = self._message_from_item(item) if item else None
            if message:
                messages.append(message)
        return messages

    def _message_from_item(self, item: Dict[str, Any]) -> Optional[Dict[str, object]]:
        item_type = item.get("type")
        if item_type == "function_call":
            return {
                "role": "assistant",
                "parts": [self._tool_call_part(item.get("call_id"), item.get("name"), item.get("arguments"))],
            }
        if item_type == "function_call_output":
            return {
                "role": "tool",
                "parts": [{"type": "tool_call_response", "id": item.get("call_id"), "response": item.get("output")}],
            }
        if item_type == "reasoning":
            summary = " ".join(
                str(entry.get("text", "")) for entry in item.get("summary") or [] if isinstance(entry, dict)
            )
            return {"role": "assistant", "parts": [{"type": "reasoning", "content": summary}]} if summary else None
        if isinstance(item_type, str) and item_type.endswith("_call"):
            # Hosted tools (web/file search, code interpreter, MCP, ...) run server-side.
            return {"role": "assistant", "parts": [self._tool_call_part(item.get("id"), item_type, None)]}

        role = item.get("role")
        if not isinstance(role, str):
            return None
        if role == "tool":
            return {
                "role": "tool",
                "parts": [{"type": "tool_call_response", "id": item.get("tool_call_id"), "response": item.get("content")}],
            }
        parts = self._content_parts(item.get("content"))
        for tool_call in item.get("tool_calls") or []:
            if isinstance(tool_call, dict):
                function = cast(Dict[str, Any], tool_call).get("function") or {}
                parts.append(self._tool_call_part(tool_call.get("id"), function.get("name"), function.get("arguments")))
        return {"role": "system" if role == "developer" else role, "parts": parts}

    def _content_parts(self, content: object) -> SemconvParts:
        if content is None:
            return []
        if isinstance(content, str):
            return [{"type": "text", "content": content}]
        if not isinstance(content, list):
            return [{"type": "text", "content": str(content)}]
        parts: SemconvParts = []
        for raw_part in cast(List[object], content):
            part = self._as_dict(raw_part)
            if part is None:
                continue
            part_type = part.get("type")
            if part_type in ("input_text", "output_text", "text"):
                parts.append({"type": "text", "content": part.get("text", "")})
            elif part_type == "refusal":
                parts.append({"type": "text", "content": part.get("refusal", "")})
            elif isinstance(part_type, str):
                # Media payloads (images, files, audio) stay out of span attributes.
                parts.append({"type": part_type})
        return parts

    @staticmethod
    def _tool_call_part(call_id: object, name: object, arguments: object) -> Dict[str, object]:
        return {"type": "tool_call", "id": call_id, "name": name, "arguments": arguments}

    def _output_messages(self, output: object, finish_reason: str) -> SemconvMessages:
        parts: SemconvParts = []
        for message in self._messages(output):
            parts.extend(cast(SemconvParts, message["parts"]))
        if not parts:
            return []
        return [{"role": "assistant", "parts": parts, "finish_reason": finish_reason}]

    def _system_instructions(self, instructions: object) -> SemconvParts:
        if isinstance(instructions, str):
            return [{"type": "text", "content": instructions}] if instructions else []
        parts: SemconvParts = []
        for message in self._messages(instructions):
            parts.extend(cast(SemconvParts, message["parts"]))
        return parts

    def _finish_reason(self, output: object, incomplete_reason: Optional[str] = None) -> str:
        if incomplete_reason == "max_output_tokens":
            return "length"
        if incomplete_reason == "content_filter":
            return "content_filter"
        for raw_item in cast(List[object], output) if isinstance(output, list) else []:
            item = self._as_dict(raw_item) or {}
            if item.get("type") == "function_call" or item.get("tool_calls"):
                return "tool_call"
        return "stop"

    def _as_utc_nano(self, dt: str) -> int:
        """Convert ISO format datetime string to nanoseconds since epoch."""
        return int(datetime.fromisoformat(dt).astimezone(timezone.utc).timestamp() * 1_000_000_000)

    def force_flush(self) -> None:
        """Forces an immediate flush of all queued spans/traces."""

    def shutdown(self) -> None:
        """Called when the application stops."""
