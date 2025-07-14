"""Context management for tracing."""

import contextvars
from typing import Optional, Dict, Any, List, TYPE_CHECKING
from dataclasses import dataclass, field

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
    spans: List[SpanContext] = field(default_factory=list)
    active_span: Optional[SpanContext] = None


# Context variables for trace and span tracking
_trace_context: contextvars.ContextVar[Optional[TraceContext]] = contextvars.ContextVar(
    "trace_context", default=None
)
_span_stack: contextvars.ContextVar[List[SpanContext]] = contextvars.ContextVar(
    "span_stack", default=[]
)
_active_span: contextvars.ContextVar[Optional["Span"]] = contextvars.ContextVar(
    "active_span", default=None
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
    """Get the current active span context."""
    stack = get_span_stack()
    return stack[-1] if stack else None


def set_active_span(span: Optional["Span"]) -> None:
    """Set the active span object."""
    _active_span.set(span)


def current_span() -> Optional["Span"]:
    """Get the current active span object that can be used to log data."""
    return _active_span.get()


def create_trace_context(trace_id: Optional[str] = None) -> TraceContext:
    """Create a new trace context."""
    if not trace_id:
        trace_id = generate_ulid()
    
    root_span_id = generate_ulid()
    trace = TraceContext(trace_id=trace_id, root_span_id=root_span_id)
    set_current_trace(trace)
    return trace


def create_span_context(
    name: str,
    parent_id: Optional[str] = None,
    attributes: Optional[Dict[str, Any]] = None
) -> SpanContext:
    """Create a new span context."""
    trace = get_current_trace()
    if not trace:
        trace = create_trace_context()
    
    # If no parent_id is provided, use the current span as parent
    if not parent_id:
        current_span_ctx = get_current_span_context()
        if current_span_ctx:
            parent_id = current_span_ctx.span_id
    
    span = SpanContext(
        trace_id=trace.trace_id,
        span_id=generate_ulid(),
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