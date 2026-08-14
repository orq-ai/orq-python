"""Inject W3C traceparent from the active @traced span onto outbound HTTP."""

from __future__ import annotations

from typing import Any, Callable

from .context import propagation_headers

_installed = False


def install_http_propagation() -> None:
    """Patch httpx and requests once so OpenAI/Anthropic pick up traceparent."""
    global _installed  # pylint: disable=global-statement
    if _installed:
        return
    _installed = True
    _patch_httpx()
    _patch_requests()


def _inject(headers: Any) -> None:
    if headers is None or "traceparent" in headers:
        return
    for key, value in propagation_headers().items():
        headers[key] = value


def _patch_method(cls: type, name: str, wrapper_factory: Callable[..., Any]) -> None:
    original = getattr(cls, name)
    if getattr(original, "_orq_traced_patched", False):
        return
    wrapped = wrapper_factory(original)
    wrapped._orq_traced_patched = True  # type: ignore[attr-defined]
    setattr(cls, name, wrapped)


def _patch_httpx() -> None:
    try:
        import httpx
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
