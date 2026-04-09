"""Traces client for sending OTLP-formatted spans to the Orq API."""

import atexit
import threading
from typing import Any, Dict, List

import httpx

from ._span_builder import wrap_in_otlp_envelope
from ._utils import logger


class OrqTracesClient:
    """Sync client that batches spans and posts OTLP JSON to /v2/traces/v1/traces.

    Spans are accumulated and flushed either when flush() is called explicitly
    or after a short delay, so that all spans from one trace arrive in a single
    request (matching the BatchSpanProcessor behaviour the backend expects).
    """

    def __init__(
        self,
        api_key: str,
        api_url: str = "https://my.orq.ai",
        flush_interval: float = 1.0,
    ):
        self._api_key = api_key
        self._url = f"{api_url.rstrip('/')}/v2/otel/v1/traces"
        self._client = httpx.Client(timeout=30.0)
        self._pending: List[Dict[str, Any]] = []
        self._lock = threading.Lock()
        self._flush_interval = flush_interval
        self._timer: threading.Timer | None = None
        atexit.register(self._atexit_flush)

    def _atexit_flush(self) -> None:
        """Flush remaining spans on interpreter shutdown."""
        if self._timer:
            self._timer.cancel()
        self.flush()

    def send_span(self, span: Dict[str, Any]) -> None:
        """Queue a span and schedule a flush."""
        with self._lock:
            self._pending.append(span)
            self._schedule_flush()

    def _schedule_flush(self) -> None:
        """Schedule a flush after the flush interval (debounced)."""
        if self._timer is None or not self._timer.is_alive():
            self._timer = threading.Timer(self._flush_interval, self.flush)
            self._timer.daemon = True
            self._timer.start()

    def flush(self) -> None:
        """Send all pending spans in one OTLP envelope."""
        with self._lock:
            if not self._pending:
                return
            spans = self._pending[:]
            self._pending.clear()

        logger.debug("FLUSH sending %d spans:", len(spans))
        for s in spans:
            logger.debug("  span: name=%s traceId=%s spanId=%s parentSpanId=%s", s.get("name"), s.get("traceId"), s.get("spanId"), s.get("parentSpanId"))
        payload = wrap_in_otlp_envelope(spans)
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        try:
            resp = self._client.post(self._url, headers=headers, json=payload)
            if resp.status_code >= 400:
                logger.debug("Failed to send spans: %s %s", resp.status_code, resp.text)
        except Exception:
            logger.debug("Error sending spans", exc_info=True)

    def close(self) -> None:
        if self._timer:
            self._timer.cancel()
        self.flush()
        self._client.close()


class AsyncOrqTracesClient:
    """Async client that posts OTLP-formatted spans to /v2/traces/v1/traces.

    Spans are accumulated and flushed after a short delay, mirroring the
    sync client's debounced flush behaviour.
    """

    def __init__(
        self,
        api_key: str,
        api_url: str = "https://my.orq.ai",
        flush_interval: float = 1.0,
    ):
        self._api_key = api_key
        self._url = f"{api_url.rstrip('/')}/v2/otel/v1/traces"
        self._client = httpx.AsyncClient(timeout=30.0)
        self._pending: List[Dict[str, Any]] = []
        self._flush_interval = flush_interval
        self._flush_task: Any = None

    async def send_span(self, span: Dict[str, Any]) -> None:
        """Queue a span and schedule a flush."""
        self._pending.append(span)
        self._schedule_flush()

    def _schedule_flush(self) -> None:
        """Schedule a flush after the flush interval (debounced)."""
        import asyncio  # pylint: disable=import-outside-toplevel

        if self._flush_task is None or self._flush_task.done():
            self._flush_task = asyncio.create_task(self._delayed_flush())

    async def _delayed_flush(self) -> None:
        import asyncio  # pylint: disable=import-outside-toplevel

        await asyncio.sleep(self._flush_interval)
        await self.flush()

    async def flush(self) -> None:
        """Send all pending spans in one OTLP envelope."""
        if not self._pending:
            return
        spans = self._pending[:]
        self._pending.clear()

        payload = wrap_in_otlp_envelope(spans)
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        try:
            resp = await self._client.post(self._url, headers=headers, json=payload)
            if resp.status_code >= 400:
                logger.debug("Failed to send spans: %s %s", resp.status_code, resp.text)
        except Exception:
            logger.debug("Error sending spans", exc_info=True)

    async def close(self) -> None:
        await self.flush()
        await self._client.aclose()
