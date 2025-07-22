"""OpenTelemetry integration for the traced module."""

from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)

# Try to import OpenTelemetry, but make it optional
try:
    from opentelemetry import trace
    from opentelemetry.trace import SpanContext, TraceFlags, TraceState
    from opentelemetry.trace.span import Span as OTelSpan
    OTEL_AVAILABLE = True
except ImportError:
    OTEL_AVAILABLE = False
    logger.debug("OpenTelemetry not available. Install with: pip install opentelemetry-api")


def is_otel_available() -> bool:
    """Check if OpenTelemetry is available and configured."""
    if not OTEL_AVAILABLE:
        return False
    
    try:
        # Check if there's a proper tracer provider configured
        tracer_provider = trace.get_tracer_provider()
        provider_class = tracer_provider.__class__.__name__
        
        # Only consider it available if we have a real TracerProvider (not proxy or noop)
        # Real providers are usually TracerProvider from the SDK
        return provider_class == 'TracerProvider'
    except Exception:
        return False


def get_current_otel_context() -> Optional[Tuple[str, str, Optional[str]]]:
    """
    Get the current OpenTelemetry trace context.
    
    Returns:
        Tuple of (trace_id, span_id, parent_span_id) in hex format, or None if no context
    """
    if not is_otel_available():
        return None
    
    try:
        current_span = trace.get_current_span()
        if not current_span or not current_span.is_recording():
            return None
        
        span_context = current_span.get_span_context()
        if not span_context or not span_context.is_valid:
            return None
        
        # Convert to hex strings (OpenTelemetry uses int representation)
        trace_id = format(span_context.trace_id, '032x')
        span_id = format(span_context.span_id, '016x')
        
        # Try to get parent span ID if available
        parent_span_id = None
        if hasattr(current_span, 'parent') and current_span.parent:
            parent_context = current_span.parent
            if hasattr(parent_context, 'span_id'):
                parent_span_id = format(parent_context.span_id, '016x')
        
        return trace_id, span_id, parent_span_id
    
    except Exception as e:
        logger.debug(f"Failed to get OpenTelemetry context: {e}")
        return None


def create_otel_span(name: str, trace_id: str, span_id: str, parent_id: Optional[str] = None) -> Optional[OTelSpan]:
    """
    Create an OpenTelemetry span that corresponds to our traced span.
    This allows the traced spans to appear in OpenTelemetry-compatible tools.
    
    Args:
        name: Span name
        trace_id: Trace ID in hex format (32 chars)
        span_id: Span ID in hex format (16 chars)
        parent_id: Parent span ID in hex format (16 chars)
    
    Returns:
        OpenTelemetry span or None if not available
    """
    if not OTEL_AVAILABLE:
        return None
    
    try:
        tracer = trace.get_tracer("orq_ai_sdk.traced")
        
        # Use the current OpenTelemetry context as parent to maintain correlation
        # This ensures the traced span becomes a child of the existing OpenTelemetry span
        current_context = trace.get_current()
        
        # Start the span with the current context as parent
        span = tracer.start_span(name, context=current_context)
        
        return span
    
    except Exception as e:
        logger.debug(f"Failed to create OpenTelemetry span: {e}")
        return None


def format_trace_id_for_otel(trace_id: str) -> str:
    """
    Format a trace ID for OpenTelemetry compatibility.
    OpenTelemetry expects 32 character hex strings.
    """
    # If it's a ULID or other format, take first 32 chars or pad
    if len(trace_id) >= 32:
        return trace_id[:32]
    else:
        # Pad with zeros if too short
        return trace_id.ljust(32, '0')


def format_span_id_for_otel(span_id: str) -> str:
    """
    Format a span ID for OpenTelemetry compatibility.
    OpenTelemetry expects 16 character hex strings.
    """
    # If it's a ULID or other format, take first 16 chars or pad
    if len(span_id) >= 16:
        return span_id[:16]
    else:
        # Pad with zeros if too short
        return span_id.ljust(16, '0')