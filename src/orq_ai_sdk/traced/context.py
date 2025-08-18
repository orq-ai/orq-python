"""Context management for tracing."""

import contextvars
from typing import Optional, Dict, Any, List, TYPE_CHECKING
from dataclasses import dataclass, field

from .otel_integration import get_current_otel_context
from .utils import generate_ulid

if TYPE_CHECKING:
    from .span import Span


@dataclass
class SpanContext:
    """Context for a single span."""
    trace_id: str
    span_id: str
    parent_id: Optional[str] = None
    session_id: Optional[str] = None
    user_id: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TraceContext:
    """Context for the entire trace."""
    trace_id: str
    root_span_id: str


# Context variables for trace and span tracking
_trace_context: contextvars.ContextVar[Optional[TraceContext]] = contextvars.ContextVar(
    "trace_context", default=None
)
_span_stack: contextvars.ContextVar[List[SpanContext]] = contextvars.ContextVar(
    "span_stack", default=[]
)
_active_span_object: contextvars.ContextVar[Optional["Span"]] = contextvars.ContextVar(
    "active_span_object", default=None
)


def get_current_trace() -> Optional[TraceContext]:
    """Get the current trace context."""
    return _trace_context.get()


def set_current_trace(trace: Optional[TraceContext]) -> None:
    """Set the current trace context."""
    _trace_context.set(trace)


def get_span_stack() -> List[SpanContext]:
    """Get the current span stack."""
    return _span_stack.get()


def push_span(span: SpanContext) -> None:
    """Push a span onto the stack."""
    stack = get_span_stack().copy()
    stack.append(span)
    _span_stack.set(stack)


def pop_span() -> Optional[SpanContext]:
    """Pop a span from the stack."""
    stack = get_span_stack().copy()
    if stack:
        span = stack.pop()
        _span_stack.set(stack)
        return span
    return None


def get_current_span_context() -> Optional[SpanContext]:
    """Get the current active span context (metadata only - IDs and attributes)."""
    stack = get_span_stack()
    return stack[-1] if stack else None


def set_active_span(span: Optional["Span"]) -> None:
    """Set the active span object (full span with logging capabilities)."""
    _active_span_object.set(span)


def current_span() -> Optional["Span"]:
    """Get the current active span object that can be used to log data."""
    return _active_span_object.get()


def create_trace_context(trace_id: Optional[str] = None) -> TraceContext:
    """Create a new trace context."""
    if not trace_id:
        trace_id = generate_ulid()
    
    root_span_id = generate_ulid()
    trace = TraceContext(trace_id=trace_id, root_span_id=root_span_id)
    set_current_trace(trace)
    return trace


def create_span_context(
    parent_id: Optional[str] = None,
    attributes: Optional[Dict[str, Any]] = None
) -> SpanContext:
    """Create a new span context."""
    # Try to get OpenTelemetry context first
    otel_context = get_current_otel_context()
    
    if otel_context:
        # Use OpenTelemetry trace context
        otel_trace_id, otel_span_id, otel_parent_span_id = otel_context
        
        # Check if we have an existing trace with the same ID
        trace = get_current_trace()
        if not trace or trace.trace_id != otel_trace_id:
            # Create a new trace context with OpenTelemetry trace ID
            trace = TraceContext(trace_id=otel_trace_id, root_span_id=otel_span_id)
            set_current_trace(trace)
        
        # Use OpenTelemetry parent span ID if no parent specified
        if not parent_id:
            parent_id = otel_parent_span_id  # This will be None for root spans
    else:
        # Fallback to original behavior
        trace = get_current_trace()
        span_stack = get_span_stack()
        
        # Create new trace if:
        # 1. No trace exists, OR
        # 2. Trace exists but no active spans (meaning previous operations ended)
        if not trace or len(span_stack) == 0:
            trace = create_trace_context()
    
    # If no parent_id is provided, use the current span as parent
    if not parent_id:
        current_span_context = get_current_span_context()
        if current_span_context:
            parent_id = current_span_context.span_id

    # Use OpenTelemetry span_id when available to maintain format consistency
    if otel_context:
        span_id = otel_context[1]  # Use OpenTelemetry span_id (hex format)
    else:
        span_id = generate_ulid()  # Use ULID format when no OpenTelemetry
    
    span = SpanContext(
        trace_id=trace.trace_id,
        span_id=span_id,
        parent_id=parent_id,
        attributes=attributes or {}
    )
    
    return span


class SpanContextManager:
    """Context manager for span lifecycle."""
    
    def __init__(self, span: SpanContext, span_object: Optional["Span"] = None):
        self.span = span
        self.span_object = span_object
        self.previous_span = None
    
    def __enter__(self):
        push_span(self.span)
        if self.span_object:
            self.previous_span = current_span()
            set_active_span(self.span_object)
        return self.span
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pop_span()
        if self.span_object:
            set_active_span(self.previous_span)
        return False
