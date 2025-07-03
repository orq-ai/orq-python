"""Decorator implementations for Orq decorator tracing."""

import functools
import inspect
import time
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from decorator.span import Span
from decorator.types import SpanType
from decorator.context import create_span_context, get_current_span, SpanContextManager
from decorator.utils import serialize_value


F = TypeVar('F', bound=Callable[..., Any])


def traced(
    _func: Optional[F] = None,
    *,
    name: Optional[str] = None,
    type: Union[SpanType, str] = SpanType.Generic,
    capture_input: bool = True,
    capture_output: bool = True,
    attributes: Optional[Dict[str, Any]] = None
) -> Union[F, Callable[[F], F]]:
    """
    Decorator to trace function execution.
    
    Args:
        name: Custom name for the span. Defaults to function name.
        type: Type of span. Defaults to SpanType.Generic = "span.generic".
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
            # Determine span name
            span_name = name or func.__name__
            
            # Create span context
            span_context = create_span_context(
                name=span_name,
                attributes=attributes or {}
            )
            
            # Create span
            span = Span(
                trace_id=span_context.trace_id,
                span_id=span_context.span_id,
                parent_id=span_context.parent_id,
                name=span_name,
                type=type,
                attributes={
                    # TODO: attributes values
                    "function.name": func.__name__,
                    "function.module": func.__module__ if hasattr(func, "__module__") else None,
                    "service.name": config.service_name,
                    "environment": config.environment,
                    **(attributes or {}),
                    **config.extra_attributes
                }
            )
            
            # TODO: Capture input if requested from config
            # if capture_input:
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
            
            # TODO: api client to trace decorator
            
            try:
                with SpanContextManager(span_context):
                    # Execute the function
                    result = func(*args, **kwargs)
                    
                    # TODO: Capture output if requested from config
                    # if capture_output:
                    try:
                        span.set_output(serialize_value(result))
                    except Exception as e:
                        if config.debug:
                            print(f"Failed to capture output: {e}")
                    
                    # Mark span as successful
                    span.set_attribute("status", "success")
                    
                    return result
            
            except Exception as e:
                # Mark span as failed
                span.set_attribute("status", "error")
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                
                # Add error event
                span.add_event("exception", {
                    "exception.type": type(e).__name__,
                    "exception.message": str(e)
                })
                
                raise
            
            finally:
                # End the span
                span.end()
                
                # Submit the span
                # TODO: submit span to api - integrate with trace decorator endpoint
        
        return wrapper
    
    # Handle both @traced and @traced() syntax
    if _func is None:
        return decorator
    else:
        return decorator(_func)