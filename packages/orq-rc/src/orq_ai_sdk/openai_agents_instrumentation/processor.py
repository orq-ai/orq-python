"""Orq Custom OpenAI Agents tracing processor with enhanced agent span support."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Dict, List, Optional, Union, cast

from .constants import SpanAttributes, SpanKind

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
SpanInputData = Union[str, List[Dict[str, object]], Dict[str, object]]
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
    from opentelemetry.context import Context, Token, attach, detach
    from opentelemetry.trace import Span as OtelSpan
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
        self._tokens: dict[str, Token[Context]] = {}
        # Track agent spans and their child spans to aggregate input/output
        self._agent_spans: dict[str, str] = {}  # span_id -> agent_name
        self._span_hierarchy: dict[str, str] = {}  # child_span_id -> parent_agent_span_id
        self._agent_inputs: Dict[str, Optional[SpanInputData]] = {}  # agent_span_id -> first LLM input
        self._agent_outputs: Dict[str, Optional[SpanOutputData]] = {}  # agent_span_id -> last LLM output

    def on_trace_start(self, trace: Trace) -> None:
        """Called when a trace is started."""
        otel_span = self._tracer.start_span(
            name=trace.name,
            attributes={
                SpanAttributes.KIND.value: SpanKind.WORKFLOW.value,
                SpanAttributes.OPERATION_NAME.value: trace.name
            },
        )
        self._root_spans[trace.trace_id] = otel_span

    def on_trace_end(self, trace: Trace) -> None:
        """Called when a trace is finished."""
        if root_span := self._root_spans.pop(trace.trace_id, None):
            root_span.set_status(Status(StatusCode.OK))
            root_span.end()

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
        span_name = self._get_span_name(span)

        otel_span = self._tracer.start_span(
            name=span_name,
            context=context,
            start_time=self._as_utc_nano(span.started_at),
            attributes={
                SpanAttributes.KIND.value: self._get_span_kind(span.span_data),
                SpanAttributes.OPERATION_NAME.value: span_name,
            },
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

    def on_span_end(self, span: Span[SpanData]) -> None:
        """Called when a span is finished."""
        if token := self._tokens.pop(span.span_id, None):
            detach(token)
        if not (otel_span := self._otel_spans.pop(span.span_id, None)):
            return

        span_name = self._get_span_name(span)
        otel_span.update_name(span_name)
        otel_span.set_attribute(SpanAttributes.OPERATION_NAME.value, span_name)
        data = span.span_data

        # Handle different span types and collect input/output for agent spans
        if isinstance(data, AgentSpanData):
            self._handle_agent_span(otel_span, data, span.span_id)
        elif isinstance(data, ResponseSpanData):
            self._handle_response_span(otel_span, data)
            self._collect_agent_data(span.span_id, data, "input", "output")
        elif isinstance(data, GenerationSpanData):
            self._handle_generation_span(otel_span, data)
            self._collect_agent_data(span.span_id, data, "input", "output")
        elif isinstance(data, FunctionSpanData):
            self._handle_function_span(otel_span, data)
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
        otel_span.set_attribute(SpanAttributes.AGENT_NAME.value, data.name)
        otel_span.set_attribute(SpanAttributes.GEN_AI_AGENT_NAME.value, data.name)
        
        # Add first LLM input and last LLM output as JSON strings
        if span_id in self._agent_inputs and self._agent_inputs[span_id] is not None:
            try:
                json_input = json.dumps(self._agent_inputs[span_id])
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, json_input)
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(self._agent_inputs[span_id]))
        
        if span_id in self._agent_outputs:
            output = self._agent_outputs[span_id]
            if output is not None:
                try:
                    # Transform the output to the required format
                    formatted_output = self._format_llm_output(output)
                    json_output = json.dumps(formatted_output)
                    otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, json_output)
                except (TypeError, ValueError):
                    otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, str(output))
        
        # Clean up tracking data
        self._agent_spans.pop(span_id, None)
        self._agent_inputs.pop(span_id, None)
        self._agent_outputs.pop(span_id, None)

    def _handle_response_span(self, otel_span: OtelSpan, data: ResponseSpanData) -> None:
        """Handle response span."""
        if hasattr(data, "response") and data.response:
            # Extract meaningful data from response instead of dumping the whole object
            response = data.response
            
            # Set basic response info
            if hasattr(response, "model"):
                otel_span.set_attribute(SpanAttributes.REQUEST_MODEL.value, response.model)
            
            # Extract and format output from response
            if hasattr(response, "output") and response.output:
                try:
                    formatted_output = self._format_llm_output(cast(SpanOutputData, response.output))
                    json_output = json.dumps(formatted_output)
                    otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, json_output)
                except (TypeError, ValueError):
                    text_content = self._extract_text_from_output(cast(SpanOutputData, response.output))
                    if text_content:
                        otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, text_content)
            
            # Extract usage information
            if hasattr(response, "usage") and response.usage:
                self._set_usage_attributes(otel_span, response.usage)
        
        # Also check for output directly on data (not just in data.response)
        if hasattr(data, "output") and data.output:
            try:
                formatted_output = self._format_llm_output(cast(SpanOutputData, data.output))
                json_output = json.dumps(formatted_output)
                otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, json_output)
            except (TypeError, ValueError):
                text_content = self._extract_text_from_output(cast(SpanOutputData, data.output))
                if text_content:
                    otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, text_content)
        
        if hasattr(data, "input") and data.input:
            # Set input for LLM spans, including system message from instructions if not already present
            try:
                enhanced_input = self._format_llm_input(data)
                if enhanced_input is not None:
                    input_json = json.dumps(enhanced_input)
                    otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, input_json)
                else:
                    otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(data.input))
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(data.input))

    def _handle_generation_span(self, otel_span: OtelSpan, data: GenerationSpanData) -> None:
        """Handle generation span."""
        if hasattr(data, "model") and isinstance(data.model, str):
            otel_span.set_attribute(SpanAttributes.REQUEST_MODEL.value, data.model)
        
        if hasattr(data, "input") and data.input:
            # Set input for LLM spans, including system message from instructions if not already present
            try:
                enhanced_input = self._format_llm_input(data)
                if enhanced_input is not None:
                    input_json = json.dumps(enhanced_input)
                    otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, input_json)
                else:
                    otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(data.input))
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(data.input))
        
        if hasattr(data, "output") and data.output:
            # Set structured output messages for LLM spans
            try:
                # Also set formatted output for orq.output.value
                formatted_output = self._format_llm_output(cast(SpanOutputData, data.output))
                formatted_json = json.dumps(formatted_output)
                otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, formatted_json)
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, str(data.output))
        
        # Extract usage information if available
        if hasattr(data, "usage") and data.usage:
            self._set_usage_attributes(otel_span, data.usage)

    def _handle_function_span(self, otel_span: OtelSpan, data: FunctionSpanData) -> None:
        """Handle function span."""
        otel_span.set_attribute(SpanAttributes.TOOL_NAME.value, data.name)

        # Add tool call ID if available
        if hasattr(data, 'call_id') and data.call_id:
            otel_span.set_attribute(SpanAttributes.TOOL_CALL_ID.value, data.call_id)
        elif hasattr(data, 'id') and data.id:
            otel_span.set_attribute(SpanAttributes.TOOL_CALL_ID.value, data.id)

        if data.input:
            otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, data.input)

        if data.output is not None:
            otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, str(data.output))

    def _handle_handoff_span(self, otel_span: OtelSpan, data: HandoffSpanData) -> None:
        """Handle handoff span."""
        # Additional handoff-specific attributes can be added here if needed

    def _format_llm_input(self, data: SpanData) -> Optional[SpanInputData]:
        """Format LLM input that includes system message from instructions if not already present."""
        if not hasattr(data, "input") or not data.input:
            return None
            
        try:
            input_messages = []
            
            # Check if system message already exists in input
            has_system_message = False
            if isinstance(data.input, list):
                has_system_message = any(
                    isinstance(msg, dict) and msg.get("role") == "system" 
                    for msg in data.input
                )
                input_messages = list(data.input)
            else:
                input_messages = [data.input]
            
            # Add system message FIRST only if not already present
            if not has_system_message and hasattr(data, "response") and data.response and hasattr(data.response, "instructions") and data.response.instructions:
                system_message = {
                    "role": "system",
                    "content": data.response.instructions
                }
                input_messages.insert(0, system_message)
            
            return input_messages
        except (TypeError, ValueError):
            return data.input

    def _collect_agent_data(self, span_id: str, data: SpanData, *data_types: str) -> None:
        """Collect input/output data for agent spans - first LLM input and last LLM output per agent."""
        # Find the parent agent span for this child span
        parent_agent_span_id = self._span_hierarchy.get(span_id)
        if not parent_agent_span_id:
            return
            
        for data_type in data_types:
            if data_type == "input" and hasattr(data, "input") and data.input:
                if parent_agent_span_id in self._agent_inputs:
                    # Only capture the first LLM input for this specific agent if none exists yet
                    if self._agent_inputs[parent_agent_span_id] is None:
                        # Use enhanced input that includes system message
                        enhanced_input = self._format_llm_input(data)
                        self._agent_inputs[parent_agent_span_id] = enhanced_input
            elif data_type == "output":
                if hasattr(data, "output") and data.output:
                    if parent_agent_span_id in self._agent_outputs:
                        # Always capture the latest LLM output for this specific agent (last one wins)
                        self._agent_outputs[parent_agent_span_id] = data.output
                elif hasattr(data, "response") and data.response:
                    if parent_agent_span_id in self._agent_outputs:
                        # Extract output from response and always update for this specific agent (last one wins)
                        if hasattr(data.response, "output") and data.response.output:
                            self._agent_outputs[parent_agent_span_id] = data.response.output

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
            if hasattr(data, 'to_agent') and data.to_agent:
                if hasattr(data.to_agent, 'name'):
                    return f"handoff to {data.to_agent.name}"
                if isinstance(data.to_agent, str):
                    return f"handoff to {data.to_agent}"
            return "handoff"
        
        # Handle other span types with name attribute
        if hasattr(data, "name") and isinstance(name := data.name, str):
            return name
        return getattr(data, "type", "unknown")

    def _get_span_kind(self, data: SpanData) -> str:
        """Get span kind based on span data type."""
        if isinstance(data, AgentSpanData):
            return SpanKind.AGENT.value
        if isinstance(data, FunctionSpanData):
            return SpanKind.TOOL.value
        if isinstance(data, GenerationSpanData):
            return SpanKind.LLM.value
        if isinstance(data, ResponseSpanData):
            return SpanKind.LLM.value
        if isinstance(data, HandoffSpanData):
            return SpanKind.TOOL.value
        return SpanKind.GENERIC.value

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

    def _format_llm_output(self, output_data: SpanOutputData) -> List[Dict[str, object]]:
        """Format output data to match the required structure."""
        formatted_output = []
        
        if isinstance(output_data, str):
            formatted_output.append({
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": output_data
                },
                "finish_reason": "stop"
            })
        elif isinstance(output_data, list):
            for index, item in enumerate(output_data):
                if hasattr(item, "content") and item.content:
                    # Extract text from content items
                    content_texts = []
                    for content_item in item.content:
                        if hasattr(content_item, "text"):
                            content_texts.append(content_item.text)
                    content = " ".join(content_texts) if content_texts else ""
                    
                    # Get role from item if available, default to "assistant"
                    role = getattr(item, "role", "assistant")
                    
                    formatted_output.append({
                        "index": index,
                        "message": {
                            "role": role,
                            "content": content
                        },
                        "finish_reason": "stop"
                    })
                elif hasattr(item, "type") and getattr(item, "type", None) == "function_call":
                    # Handle tool calls (ResponseFunctionToolCall)
                    tool_call_data = {
                        "role": "assistant",
                        "tool_calls": [{
                            "id": getattr(item, "id", getattr(item, "call_id", "")),
                            "type": "function",
                            "function": {
                                "name": getattr(item, "name", ""),
                                "arguments": getattr(item, "arguments", "")
                            }
                        }]
                    }
                    formatted_output.append({
                        "index": index,
                        "message": tool_call_data,
                        "finish_reason": "tool_calls"
                    })
                elif isinstance(item, dict):
                    content = str(item.get("content", item.get("text", "")))
                    role = str(item.get("role", "assistant"))
                    formatted_output.append({
                        "index": index,
                        "message": {
                            "role": role,
                            "content": str(content)
                        },
                        "finish_reason": "stop"
                    })
                elif isinstance(item, str):
                    formatted_output.append({
                        "index": index,
                        "message": {
                            "role": "assistant",
                            "content": item
                        },
                        "finish_reason": "stop"
                    })
        else:
            # Fallback for other types
            formatted_output.append({
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": str(output_data)
                },
                "finish_reason": "stop"
            })
        
        return formatted_output

    def _extract_text_from_output(self, output_data: SpanOutputData) -> Optional[str]:
        """Extract text content from output data."""
        if isinstance(output_data, str):
            return output_data
        if isinstance(output_data, list):
            texts = []
            for item in output_data:
                if hasattr(item, "content") and item.content:
                    for content_item in item.content:
                        if hasattr(content_item, "text"):
                            texts.append(content_item.text)
                elif isinstance(item, dict):
                    if "content" in item:
                        texts.append(str(item["content"]))
                    elif "text" in item:
                        texts.append(str(item["text"]))
                elif isinstance(item, str):
                    texts.append(item)
            return " ".join(texts) if texts else None
        return str(output_data) if output_data else None

    def _set_usage_attributes(self, otel_span: OtelSpan, usage: UsageData) -> None:
        """Set usage-related attributes on the span."""
        if hasattr(usage, "input_tokens"):
            otel_span.set_attribute(SpanAttributes.USAGE_INPUT_TOKENS.value, usage.input_tokens)
        if hasattr(usage, "output_tokens"):
            otel_span.set_attribute(SpanAttributes.USAGE_OUTPUT_TOKENS.value, usage.output_tokens)

    def _as_utc_nano(self, dt: str) -> int:
        """Convert ISO format datetime string to nanoseconds since epoch."""
        return int(datetime.fromisoformat(dt).astimezone(timezone.utc).timestamp() * 1_000_000_000)

    def force_flush(self) -> None:
        """Forces an immediate flush of all queued spans/traces."""

    def shutdown(self) -> None:
        """Called when the application stops."""
