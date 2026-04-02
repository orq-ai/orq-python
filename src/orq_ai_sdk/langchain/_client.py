"""Traces client for sending OTLP spans to the Orq API."""

from typing import Any, Dict, List

import httpx

from ._utils import logger


class OrqTracesClient:
    """Sync client that posts OTLP-formatted spans to /v2/traces/v1/traces."""

    def __init__(self, api_key: str, api_url: str = "https://my.orq.ai"):
        self._api_key = api_key
        self._url = f"{api_url.rstrip('/')}/v2/traces/v1/traces"
        self._client = httpx.Client(timeout=30.0)

    def send_spans(self, spans: List[Dict[str, Any]]) -> None:
        """Send one or more spans to the traces API."""
        if not spans:
            return
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        try:
            resp = self._client.post(
                self._url, headers=headers, json={"spans": spans}
            )
            if resp.status_code >= 400:
                logger.debug("Failed to send spans: %s %s", resp.status_code, resp.text)
        except Exception:
            logger.debug("Error sending spans", exc_info=True)

    def send_span(self, span: Dict[str, Any]) -> None:
        """Send a single span."""
        self.send_spans([span])

    def close(self) -> None:
        self._client.close()


class AsyncOrqTracesClient:
    """Async client that posts OTLP-formatted spans to /v2/traces/v1/traces."""

    def __init__(self, api_key: str, api_url: str = "https://my.orq.ai"):
        self._api_key = api_key
        self._url = f"{api_url.rstrip('/')}/v2/traces/v1/traces"
        self._client = httpx.AsyncClient(timeout=30.0)

    async def send_spans(self, spans: List[Dict[str, Any]]) -> None:
        """Send one or more spans to the traces API."""
        if not spans:
            return
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        try:
            resp = await self._client.post(
                self._url, headers=headers, json={"spans": spans}
            )
            if resp.status_code >= 400:
                logger.debug("Failed to send spans: %s %s", resp.status_code, resp.text)
        except Exception:
            logger.debug("Error sending spans", exc_info=True)

    async def send_span(self, span: Dict[str, Any]) -> None:
        """Send a single span."""
        await self.send_spans([span])

    async def close(self) -> None:
        await self._client.aclose()
