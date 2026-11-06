"""Propagate the active Orq or OpenTelemetry span onto outbound HTTP."""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import Any

from .context import get_current_span_context, merge_orq_tracestate, propagation_headers

_INSTALLED = False
_OTEL_CONTEXT = False


def install_http_propagation(*, otel_context: bool = False) -> None:
    """Install request-time propagation for available HTTP client libraries."""
    global _INSTALLED, _OTEL_CONTEXT  # pylint: disable=global-statement
    _OTEL_CONTEXT = _OTEL_CONTEXT or otel_context
    if _INSTALLED:
        return
    _INSTALLED = True
    _patch_httpx("httpx")
    _patch_httpx("httpx2")
    _patch_requests()
    _patch_aiohttp()


def _active_headers() -> tuple[dict[str, str], bool]:
    if _OTEL_CONTEXT:
        try:
            from opentelemetry import trace
            from opentelemetry.trace.propagation.tracecontext import (
                TraceContextTextMapPropagator,
            )

            native = trace.get_current_span().get_span_context()
            if native.is_valid:
                orq_span = get_current_span_context()
                if orq_span is not None and (
                    orq_span.trace_id == format(native.trace_id, "032x")
                    and orq_span.span_id == format(native.span_id, "016x")
                ):
                    return propagation_headers(), True
                headers: dict[str, str] = {}
                TraceContextTextMapPropagator().inject(headers)
                return headers, False
        except ImportError:
            pass
    return propagation_headers(), True


def _header_key(headers: Any, name: str) -> Any:
    return next((key for key in headers if str(key).lower() == name), None)


def _inject(headers: Any) -> None:
    if headers is None:
        return
    incoming, orq_owned = _active_headers()
    if not incoming:
        return
    parent_key = _header_key(headers, "traceparent")
    if parent_key is None:
        for key, value in incoming.items():
            if _header_key(headers, key) is None:
                headers[key] = value
        return
    if not orq_owned or headers[parent_key] != incoming["traceparent"]:
        return
    state_key = _header_key(headers, "tracestate") or "tracestate"
    headers[state_key] = merge_orq_tracestate(headers.get(state_key) or "")


def _patch_method(cls: type, name: str, wrapper_factory: Callable[..., Any]) -> None:
    original = getattr(cls, name)
    if getattr(original, "_orq_traced_patched", False):
        return
    wrapped = wrapper_factory(original)
    wrapped._orq_traced_patched = True  # type: ignore[attr-defined]  # pylint: disable=protected-access
    setattr(cls, name, wrapped)


def _patch_httpx(module_name: str) -> None:
    try:
        httpx = import_module(module_name)
    except ImportError:
        return

    def wrap_send(original: Callable[..., Any]) -> Callable[..., Any]:
        def send(self: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            _inject(getattr(request, "headers", None))
            return original(self, request, *args, **kwargs)

        return send

    def wrap_async_send(original: Callable[..., Any]) -> Callable[..., Any]:
        async def send(self: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            _inject(getattr(request, "headers", None))
            return await original(self, request, *args, **kwargs)

        return send

    _patch_method(httpx.Client, "send", wrap_send)
    _patch_method(httpx.AsyncClient, "send", wrap_async_send)


def _patch_requests() -> None:
    try:
        import requests
    except ImportError:
        return

    def wrap_send(original: Callable[..., Any]) -> Callable[..., Any]:
        def send(self: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            _inject(getattr(request, "headers", None))
            return original(self, request, *args, **kwargs)

        return send

    _patch_method(requests.Session, "send", wrap_send)


def _patch_aiohttp() -> None:
    try:
        import aiohttp
        from multidict import CIMultiDict
    except ImportError:
        return

    def wrap_request(original: Callable[..., Any]) -> Callable[..., Any]:
        async def request(self: Any, *args: Any, **kwargs: Any) -> Any:
            headers = CIMultiDict(self.headers)
            headers.update(kwargs.get("headers") or {})
            _inject(headers)
            kwargs["headers"] = headers
            return await original(self, *args, **kwargs)

        return request

    _patch_method(aiohttp.ClientSession, "_request", wrap_request)
