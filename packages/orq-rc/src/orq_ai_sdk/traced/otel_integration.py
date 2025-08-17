"""OpenTelemetry integration for the traced module."""

from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)

# Try to import OpenTelemetry, but make it optional
try:
    from opentelemetry import trace
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
        logger.debug("Failed to get OpenTelemetry context: %s", e)
        return None
