"""Decorator implementations for Orq decorator tracing."""
# pylint: disable=no-else-return

import functools
import inspect
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar, Union

from .client import get_client, OrqClient
from .config import get_config, Config
from .span import Span
from .context import create_span_context, SpanContext, SpanContextManager
from .utils import serialize_value, validate_span_type
from .otel_integration import is_otel_available


F = TypeVar('F', bound=Callable[..., Any])


def _setup_tracing(
    func: Callable,
    span_name: str,
    span_type: str,
    attributes: Optional[Dict[str, Any]],
    capture_input: bool,
    args: tuple,
    kwargs: dict,
) -> Tuple[Config, Span, SpanContext, Any, Any, OrqClient]:
    """Set up tracing infrastructure: OTel span, span context, span object, and input capture."""
    config = get_config()

    # Create OpenTelemetry span if integration is enabled (before traced span context)
    otel_span = None
    otel_context_token = None
    if is_otel_available():
        from opentelemetry import trace, context  # pylint: disable=import-outside-toplevel,import-error
        tracer = trace.get_tracer(__name__)
        otel_span = tracer.start_span(span_name)
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
        type=validate_span_type(span_type),
        attributes={
            **(attributes or {}),
            **config.extra_attributes
        }
    )

    # Capture input if requested
    if capture_input:
        try:
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            input_data = {}
            for param_name, param_value in bound_args.arguments.items():
                if param_name not in ('self', 'cls'):
                    input_data[param_name] = serialize_value(param_value)

            span.set_input(input_data)
        except Exception as e:
            if config.debug:
                print(f"Failed to capture input: {e}")

    client = get_client()
    return config, span, span_context, otel_span, otel_context_token, client


def _finalize_span_success(span: Span, result: Any, capture_output: bool, otel_span: Any, config: Config) -> None:
    """Handle successful span completion: capture output and update OTel span."""
    if capture_output:
        try:
            span.set_output(serialize_value(result))
        except Exception as e:
            if config.debug:
                print(f"Failed to capture output: {e}")

    span.set_attribute("status", "success")

    if otel_span:
        try:
            from opentelemetry.trace import Status, StatusCode  # pylint: disable=import-outside-toplevel,import-error

            for key, value in span.attributes.items():
                otel_span.set_attribute(key, str(value))
            otel_span.set_attribute("type", span.type)
            if span.input is not None:
                otel_span.set_attribute("input", str(span.input))
            if span.output is not None:
                otel_span.set_attribute("output", str(span.output))
            otel_span.set_status(Status(StatusCode.OK))
        except Exception:
            pass


def _finalize_span_error(span: Span, error: Exception, otel_span: Any, config: Config) -> None:  # pylint: disable=unused-argument
    """Handle failed span: record error attributes and update OTel span."""
    span.set_attribute("status", "error")
    span.set_attribute("error.message", str(error))

    if otel_span:
        try:
            from opentelemetry.trace import Status, StatusCode  # pylint: disable=import-outside-toplevel,import-error

            for key, value in span.attributes.items():
                otel_span.set_attribute(key, str(value))
            otel_span.set_attribute("type", span.type)
            if span.input is not None:
                otel_span.set_attribute("input", str(span.input))
            otel_span.set_status(Status(StatusCode.ERROR, str(error)))
            otel_span.record_exception(error)
        except Exception:
            pass


def _teardown_tracing(span: Span, otel_span: Any, otel_context_token: Any, client: OrqClient, config: Config) -> None:
    """Clean up tracing: end OTel span, end traced span, and submit."""
    if otel_span:
        otel_span.end()
    if otel_context_token:
        from opentelemetry import context  # pylint: disable=import-outside-toplevel,import-error
        context.detach(otel_context_token)

    span.end()

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
    Decorator to trace function execution. Works with both sync and async functions.

    Args:
        name: Custom name for the span. Defaults to function name.
        type: Type of span. Must be one of: "llm", "score", "function", "eval", "task", "tool". Defaults to "function".
        attributes: Additional attributes to add to the span.

    Usage:
        @traced
        def my_function():
            pass

        @traced
        async def my_async_function():
            pass

        # Override name
        @traced(name="custom_name")
        def my_function():
            pass
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            config = get_config()
            if not config.enabled:
                return func(*args, **kwargs)

            span_name = name or func.__name__
            config, span, span_context, otel_span, otel_context_token, client = _setup_tracing(
                func, span_name, type, attributes, capture_input, args, kwargs
            )

            try:
                with SpanContextManager(span_context, span):
                    result = func(*args, **kwargs)
                    _finalize_span_success(span, result, capture_output, otel_span, config)
                    return result
            except Exception as e:
                _finalize_span_error(span, e, otel_span, config)
                raise
            finally:
                _teardown_tracing(span, otel_span, otel_context_token, client, config)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            config = get_config()
            if not config.enabled:
                return await func(*args, **kwargs)

            span_name = name or func.__name__
            config, span, span_context, otel_span, otel_context_token, client = _setup_tracing(
                func, span_name, type, attributes, capture_input, args, kwargs
            )

            try:
                async with SpanContextManager(span_context, span):
                    result = await func(*args, **kwargs)
                    _finalize_span_success(span, result, capture_output, otel_span, config)
                    return result
            except Exception as e:
                _finalize_span_error(span, e, otel_span, config)
                raise
            finally:
                _teardown_tracing(span, otel_span, otel_context_token, client, config)

        if inspect.iscoroutinefunction(func):
            return async_wrapper  # type: ignore[return-value]
        return wrapper  # type: ignore[return-value]

    # Handle both @traced and @traced() syntax
    if _func is None:
        return decorator
    else:
        return decorator(_func)
