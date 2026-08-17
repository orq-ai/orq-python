"""Inject W3C traceparent from the active @traced span onto outbound HTTP."""

from __future__ import annotations

from typing import Any, Callable

from .context import merge_orq_tracestate, propagation_headers

_INSTALLED = False


def install_http_propagation() -> None:
    """Patch httpx and requests once so OpenAI/Anthropic pick up traceparent."""
    global _INSTALLED  # pylint: disable=global-statement
    if _INSTALLED:
        return
    _INSTALLED = True
    _patch_httpx()
    _patch_requests()


def _inject(headers: Any) -> None:
    if headers is None:
        return
    incoming = propagation_headers()
    if not incoming:
        return
    if "traceparent" not in headers:
        for key, value in incoming.items():
            headers[key] = value
        return
    # Another instrumentor already set traceparent. Only stamp orq=1 when that
    # parent is the active @traced span — never claim a foreign APM parent.
    if headers.get("traceparent") != incoming["traceparent"]:
        return
    headers["tracestate"] = merge_orq_tracestate(headers.get("tracestate") or "")


def _patch_method(cls: type, name: str, wrapper_factory: Callable[..., Any]) -> None:
    original = getattr(cls, name)
    if getattr(original, "_orq_traced_patched", False):
        return
    wrapped = wrapper_factory(original)
    wrapped._orq_traced_patched = True  # type: ignore[attr-defined]  # pylint: disable=protected-access
    setattr(cls, name, wrapped)


def _patch_httpx() -> None:
    try:
        import httpx  # pylint: disable=import-outside-toplevel
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
        import requests  # pylint: disable=import-outside-toplevel
    except ImportError:
        return

    def wrap_send(original: Callable[..., Any]) -> Callable[..., Any]:
        def send(self: Any, request: Any, *args: Any, **kwargs: Any) -> Any:
            _inject(getattr(request, "headers", None))
            return original(self, request, *args, **kwargs)

        return send

    _patch_method(requests.Session, "send", wrap_send)
