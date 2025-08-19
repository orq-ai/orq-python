"""Decorator implementations for Orq decorator tracing."""
# pylint: disable=no-else-return

import functools
import inspect
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from .client import get_client
from .config import get_config
from .span import Span
from .context import create_span_context, SpanContextManager
from .utils import serialize_value, validate_span_type
from .otel_integration import is_otel_available


F = TypeVar('F', bound=Callable[..., Any])


def traced(
    _func: Optional[F] = None,
    *,
    name: Optional[str] = None,
    type: str = "function",  # pylint: disable=redefined-builtin
    capture_input: bool = True,
    capture_output: bool = True,
    attributes: Optional[Dict[str, Any]] = None
) -> Union[F, Callable[[F], F]]:
    """
    Decorator to trace function execution.
    
    Args:
        name: Custom name for the span. Defaults to function name.
        type: Type of span. Must be one of: "llm", "score", "function", "eval", "task", "tool". Defaults to "function".
        attributes: Additional attributes to add to the span.
    
    Usage:
        @traced
        def my_function():
            pass
        
        # Override name
        @trace(name="custom_name")
        def my_function():
            pass
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # Get configuration
            config = get_config()
            if not config.enabled:
                return func(*args, **kwargs)

            # Determine span name
            span_name = name or func.__name__
            
            # Create OpenTelemetry span if integration is enabled (before traced span context)
            otel_span = None
            otel_context_token = None
            if is_otel_available():
                from opentelemetry import trace, context  # pylint: disable=import-outside-toplevel,import-error
                # Use the global tracer - this will inherit from current context automatically
                tracer = trace.get_tracer(__name__)
                otel_span = tracer.start_span(span_name)
                # Properly attach the span context
                otel_span_context = trace.set_span_in_context(otel_span)
                otel_context_token = context.attach(otel_span_context)
            
            # Create span context (this will now pick up the OpenTelemetry context we just created)
            span_context = create_span_context(
                attributes=attributes or {}
            )
            
            # Create span
            span = Span(
                trace_id=span_context.trace_id,
                span_id=span_context.span_id,
                parent_id=span_context.parent_id,
                name=span_name,
                type=validate_span_type(type),
                attributes={
                    **(attributes or {}),
                    **config.extra_attributes
                }
            )
            
            # Capture input if requested
            if capture_input:
                try:
                    # Get function signature
                    sig = inspect.signature(func)
                    bound_args = sig.bind(*args, **kwargs)
                    bound_args.apply_defaults()
                    
                    # Create input dict
                    input_data = {}
                    for param_name, param_value in bound_args.arguments.items():
                        # Skip 'self' and 'cls' parameters
                        if param_name not in ('self', 'cls'):
                            input_data[param_name] = serialize_value(param_value)
                    
                    span.set_input(input_data)
                except Exception as e:
                    if config.debug:
                        print(f"Failed to capture input: {e}")
            
            # Execute function within span context
            client = get_client()
            
            try:
                with SpanContextManager(span_context, span):
                    # Execute the function
                    result = func(*args, **kwargs)
                    
                    # Capture output if requested
                    if capture_output:
                        try:
                            span.set_output(serialize_value(result))
                        except Exception as e:
                            if config.debug:
                                print(f"Failed to capture output: {e}")
                    
                    # Mark span as successful
                    span.set_attribute("status", "success")

                    # Update OpenTelemetry span with data and status
                    if otel_span:
                        try:
                            from opentelemetry.trace import Status, StatusCode  # pylint: disable=import-outside-toplevel,import-error
                            
                            # Copy attributes from traced span to OpenTelemetry span
                            for key, value in span.attributes.items():
                                otel_span.set_attribute(key, str(value))
                            
                            # Add traced span type
                            otel_span.set_attribute("type", span.type)
                            
                            # Add input data if captured
                            if span.input is not None:
                                otel_span.set_attribute("input", str(span.input))
                            
                            # Add output data if captured
                            if span.output is not None:
                                otel_span.set_attribute("output", str(span.output))
                            
                            otel_span.set_status(Status(StatusCode.OK))
                        except Exception:
                            pass
                    
                    return result
            
            except Exception as e:
                # Mark span as failed
                span.set_attribute("status", "error")
                span.set_attribute("error.message", str(e))

                # Update OpenTelemetry span with error and data
                if otel_span:
                    try:
                        from opentelemetry.trace import Status, StatusCode  # pylint: disable=import-outside-toplevel,import-error
                        
                        # Copy attributes from traced span to OpenTelemetry span
                        for key, value in span.attributes.items():
                            otel_span.set_attribute(key, str(value))
                        
                        # Add traced span type
                        otel_span.set_attribute("type", span.type)
                        
                        # Add input data if captured
                        if span.input is not None:
                            otel_span.set_attribute("input", str(span.input))
                        
                        otel_span.set_status(Status(StatusCode.ERROR, str(e)))
                        otel_span.record_exception(e)
                    except Exception:
                        pass
                
                raise
            
            finally:
                # End the OpenTelemetry span and restore context
                if otel_span:
                    otel_span.end()
                if otel_context_token:
                    from opentelemetry import context  # pylint: disable=import-outside-toplevel,import-error
                    context.detach(otel_context_token)
                
                # End the span
                span.end()
                
                # Submit the span only if OpenTelemetry is not handling tracing
                if not otel_span:
                    if config.debug:
                        print(f"Submitting span: {span.name} (trace_id: {span.trace_id}, span_id: {span.span_id}, parent_id: {span.parent_id})")
                    client.submit_span(span)
                    
                    # Force flush for parent spans (spans with no parent_id) to ensure immediate sending
                    if span.parent_id is None:
                        if config.debug:
                            print(f"Force flushing parent span {span.name}")
                        client.flush()
                else:
                    if config.debug:
                        print(f"OpenTelemetry active - skipping Orq API submission for span: {span.name}")
        
        return wrapper  # type: ignore[return-value]

    # Handle both @traced and @traced() syntax
    if _func is None:
        return decorator
    else:
        return decorator(_func)
