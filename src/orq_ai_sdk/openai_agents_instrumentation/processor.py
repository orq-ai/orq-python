"""Custom OpenAI Agents tracing processor with enhanced agent span support."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Optional

from agents.tracing import Span, Trace, TracingProcessor
from agents.tracing.span_data import (
    AgentSpanData,
    FunctionSpanData,
    GenerationSpanData,
    ResponseSpanData,
    SpanData,
)
from opentelemetry.context import attach, detach
from opentelemetry.trace import Span as OtelSpan
from opentelemetry.trace import (
    Status,
    StatusCode,
    Tracer,
    set_span_in_context,
)
from opentelemetry.util.types import AttributeValue

from openai_agents_instrumentation.constants import (
    GenAIAttributes,
    GenAIOperation,
    GenAISystem,
    SpanAttributes,
    SpanKind,
)


class EnhancedOpenAIAgentsProcessor(TracingProcessor):
    """Enhanced tracing processor that adds input/output to agent spans."""

    def __init__(self, tracer: Tracer) -> None:
        self._tracer = tracer
        self._root_spans: dict[str, OtelSpan] = {}
        self._otel_spans: dict[str, OtelSpan] = {}
        self._tokens: dict[str, object] = {}
        # Track agent spans and their child spans to aggregate input/output
        self._agent_spans: dict[str, str] = {}  # span_id -> agent_name
        self._span_hierarchy: dict[str, str] = {}  # child_span_id -> parent_agent_span_id
        self._agent_inputs: dict[str, list[Any]] = {}  # agent_span_id -> inputs
        self._agent_outputs: dict[str, list[Any]] = {}  # agent_span_id -> outputs

    def on_trace_start(self, trace: Trace) -> None:
        """Called when a trace is started."""
        otel_span = self._tracer.start_span(
            name=trace.name,
            attributes={
                SpanAttributes.KIND.value: SpanKind.WORKFLOW.value,
                GenAIAttributes.OPERATION_NAME.value: trace.name,
                GenAIAttributes.SYSTEM.value: GenAISystem.OPENAI.value,
            },
        )
        self._root_spans[trace.trace_id] = otel_span

    def on_trace_end(self, trace: Trace) -> None:
        """Called when a trace is finished."""
        if root_span := self._root_spans.pop(trace.trace_id, None):
            root_span.set_status(Status(StatusCode.OK))
            root_span.end()

    def on_span_start(self, span: Span[Any]) -> None:
        """Called when a span is started."""
        if not span.started_at:
            return
        
        start_time = datetime.fromisoformat(span.started_at)
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
            start_time=self._as_utc_nano(start_time),
            attributes={
                SpanAttributes.KIND.value: self._get_span_kind(span.span_data),
                GenAIAttributes.OPERATION_NAME.value: span_name,
                GenAIAttributes.SYSTEM.value: GenAISystem.OPENAI.value,
            },
        )
        
        self._otel_spans[span.span_id] = otel_span
        self._tokens[span.span_id] = attach(set_span_in_context(otel_span))
        
        # Track agent spans and hierarchy
        if isinstance(span.span_data, AgentSpanData):
            agent_name = span.span_data.name
            self._agent_spans[span.span_id] = agent_name
            if span.span_id not in self._agent_inputs:
                self._agent_inputs[span.span_id] = []
            if span.span_id not in self._agent_outputs:
                self._agent_outputs[span.span_id] = []
        else:
            # For non-agent spans, find their parent agent span
            parent_agent_span_id = self._find_parent_agent_span(span.parent_id)
            if parent_agent_span_id:
                self._span_hierarchy[span.span_id] = parent_agent_span_id

    def on_span_end(self, span: Span[Any]) -> None:
        """Called when a span is finished."""
        if token := self._tokens.pop(span.span_id, None):
            detach(token)
        if not (otel_span := self._otel_spans.pop(span.span_id, None)):
            return

        otel_span.update_name(self._get_span_name(span))
        data = span.span_data

        # Handle different span types and collect input/output for agent spans
        if isinstance(data, AgentSpanData):
            self._handle_agent_span(otel_span, data, span.span_id)
        elif isinstance(data, ResponseSpanData):
            self._handle_response_span(otel_span, data)
            self._collect_agent_data(span.span_id, data, "input", "output")
        elif isinstance(data, GenerationSpanData):
            self._handle_generation_span(otel_span, data)
            self._collect_agent_data(span.span_id, data, "input")
        elif isinstance(data, FunctionSpanData):
            self._handle_function_span(otel_span, data)

        end_time: Optional[int] = None
        if span.ended_at:
            try:
                end_time = self._as_utc_nano(datetime.fromisoformat(span.ended_at))
            except ValueError:
                pass

        otel_span.set_status(status=self._get_span_status(span))
        otel_span.end(end_time)

    def _handle_agent_span(self, otel_span: OtelSpan, data: AgentSpanData, span_id: str) -> None:
        """Handle agent span with enhanced input/output collection."""
        otel_span.set_attribute(SpanAttributes.AGENT_NAME.value, data.name)
        
        # Add aggregated input/output from child spans as JSON strings
        if span_id in self._agent_inputs and self._agent_inputs[span_id]:
            try:
                json_input = json.dumps(self._agent_inputs[span_id])
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, json_input)
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, str(self._agent_inputs[span_id]))
        
        if span_id in self._agent_outputs and self._agent_outputs[span_id]:
            try:
                json_output = json.dumps(self._agent_outputs[span_id])
                otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, json_output)
            except (TypeError, ValueError):
                otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, str(self._agent_outputs[span_id]))
        
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
                otel_span.set_attribute(GenAIAttributes.RESPONSE_MODEL.value, response.model)
            if hasattr(response, "id"):
                otel_span.set_attribute(GenAIAttributes.RESPONSE_ID.value, response.id)
            
            # Extract text content from response output
            if hasattr(response, "output") and response.output:
                text_content = self._extract_text_from_output(response.output)
                if text_content:
                    otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, text_content)
            
            # Extract usage information
            if hasattr(response, "usage") and response.usage:
                self._set_usage_attributes(otel_span, response.usage)
        
        if hasattr(data, "input") and data.input:
            # Set structured input messages for LLM spans
            try:
                input_json = json.dumps(data.input)
                otel_span.set_attribute(GenAIAttributes.REQUEST_MESSAGES.value, input_json)
            except (TypeError, ValueError):
                otel_span.set_attribute(GenAIAttributes.REQUEST_MESSAGES.value, str(data.input))

    def _handle_generation_span(self, otel_span: OtelSpan, data: GenerationSpanData) -> None:
        """Handle generation span."""
        otel_span.set_attribute(GenAIAttributes.OPERATION_NAME.value, GenAIOperation.CHAT.value)
        
        if hasattr(data, "model") and isinstance(data.model, str):
            otel_span.set_attribute(GenAIAttributes.REQUEST_MODEL.value, data.model)
        
        if hasattr(data, "input") and data.input:
            # Set structured input messages for LLM spans
            try:
                input_json = json.dumps(data.input)
                otel_span.set_attribute(GenAIAttributes.REQUEST_MESSAGES.value, input_json)
            except (TypeError, ValueError):
                otel_span.set_attribute(GenAIAttributes.REQUEST_MESSAGES.value, str(data.input))
        
        if hasattr(data, "output") and data.output:
            # Set structured output messages for LLM spans
            try:
                output_json = json.dumps(data.output)
                otel_span.set_attribute(GenAIAttributes.RESPONSE_MESSAGES.value, output_json)
            except (TypeError, ValueError):
                otel_span.set_attribute(GenAIAttributes.RESPONSE_MESSAGES.value, str(data.output))
        
        # Extract usage information if available
        if hasattr(data, "usage") and data.usage:
            self._set_usage_attributes(otel_span, data.usage)

    def _handle_function_span(self, otel_span: OtelSpan, data: FunctionSpanData) -> None:
        """Handle function span."""
        otel_span.set_attribute(GenAIAttributes.TOOL_NAME.value, data.name)
        
        if data.input:
            otel_span.set_attribute(SpanAttributes.INPUT_VALUE.value, data.input)
        
        if data.output is not None:
            otel_span.set_attribute(SpanAttributes.OUTPUT_VALUE.value, str(data.output))

    def _collect_agent_data(self, span_id: str, data: SpanData, *data_types: str) -> None:
        """Collect input/output data for agent spans."""
        # Find the parent agent span for this child span
        parent_agent_span_id = self._span_hierarchy.get(span_id)
        if not parent_agent_span_id:
            return
            
        for data_type in data_types:
            if data_type == "input" and hasattr(data, "input") and data.input:
                if parent_agent_span_id in self._agent_inputs:
                    # Preserve structured input data for agent aggregation
                    self._agent_inputs[parent_agent_span_id].extend(
                        data.input if isinstance(data.input, list) else [data.input]
                    )
            elif data_type == "output":
                if hasattr(data, "output") and data.output:
                    if parent_agent_span_id in self._agent_outputs:
                        # Preserve structured output data for agent aggregation
                        self._agent_outputs[parent_agent_span_id].extend(
                            data.output if isinstance(data.output, list) else [data.output]
                        )
                elif hasattr(data, "response") and data.response:
                    if parent_agent_span_id in self._agent_outputs:
                        # Extract structured output from response
                        if hasattr(data.response, "output") and data.response.output:
                            self._agent_outputs[parent_agent_span_id].extend(
                                data.response.output if isinstance(data.response.output, list) else [data.response.output]
                            )

    def _find_parent_agent_span(self, parent_id: Optional[str]) -> Optional[str]:
        """Find the nearest parent agent span ID."""
        if not parent_id:
            return None
        
        # Check if parent is an agent span
        if parent_id in self._agent_spans:
            return parent_id
            
        # Recursively check up the hierarchy
        return self._span_hierarchy.get(parent_id)

    def _get_span_name(self, span: Span[Any]) -> str:
        """Get span name from span data."""
        if hasattr(data := span.span_data, "name") and isinstance(name := data.name, str):
            return name
        return getattr(data, "type", "unknown")

    def _get_span_kind(self, data: SpanData) -> str:
        """Get span kind based on span data type."""
        if isinstance(data, AgentSpanData):
            return SpanKind.AGENT.value
        elif isinstance(data, FunctionSpanData):
            return SpanKind.TOOL.value
        elif isinstance(data, GenerationSpanData):
            return SpanKind.LLM.value
        elif isinstance(data, ResponseSpanData):
            return SpanKind.LLM.value
        else:
            return SpanKind.CHAIN.value

    def _get_span_status(self, span: Span[Any]) -> Status:
        """Get span status from span error information."""
        if error := getattr(span, "error", None):
            return Status(
                status_code=StatusCode.ERROR,
                description=f"{error.get('message', '')}: {error.get('data', '')}"
            )
        return Status(StatusCode.OK)

    def _extract_text_from_input(self, input_data: Any) -> Optional[str]:
        """Extract text content from input data."""
        if isinstance(input_data, str):
            return input_data
        elif isinstance(input_data, list):
            texts = []
            for item in input_data:
                if isinstance(item, dict):
                    if "content" in item:
                        texts.append(str(item["content"]))
                    elif "text" in item:
                        texts.append(str(item["text"]))
                elif isinstance(item, str):
                    texts.append(item)
            return " ".join(texts) if texts else None
        elif isinstance(input_data, dict):
            if "content" in input_data:
                return str(input_data["content"])
            elif "text" in input_data:
                return str(input_data["text"])
        return str(input_data) if input_data else None

    def _extract_text_from_output(self, output_data: Any) -> Optional[str]:
        """Extract text content from output data."""
        if isinstance(output_data, str):
            return output_data
        elif isinstance(output_data, list):
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

    def _set_usage_attributes(self, otel_span: OtelSpan, usage: Any) -> None:
        """Set usage-related attributes on the span."""
        if hasattr(usage, "input_tokens"):
            otel_span.set_attribute(GenAIAttributes.USAGE_INPUT_TOKENS.value, usage.input_tokens)
        if hasattr(usage, "output_tokens"):
            otel_span.set_attribute(GenAIAttributes.USAGE_OUTPUT_TOKENS.value, usage.output_tokens)

    def _as_utc_nano(self, dt: datetime) -> int:
        """Convert datetime to nanoseconds since epoch."""
        return int(dt.astimezone(timezone.utc).timestamp() * 1_000_000_000)

    def force_flush(self) -> None:
        """Forces an immediate flush of all queued spans/traces."""
        pass

    def shutdown(self) -> None:
        """Called when the application stops."""
        pass