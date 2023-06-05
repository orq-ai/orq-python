import time
from typing import Any, Optional

from .request import post
from .rule_type import OrquestaRuleType


class OrquestaResult:
    def __init__(
        self,
        api_key: str,
        endpoint_url: str,
        start_time: int,
        value: Any,
        trace_id: Optional[str],
        type: Optional[OrquestaRuleType],
    ):
        self.trace_id = trace_id
        self.type = type
        self.value = value
        self.__api_key = api_key
        self.__endpoint_url = endpoint_url

        self.__report_roundtrip_time(start_time)

    @property
    def _metrics_endpoint_url(self) -> str:
        return f"{self.__endpoint_url}/{self.trace_id}/metrics"

    def add_metrics(self, metrics: dict = {}) -> None:
        if not self.trace_id:
            return

        post(self._metrics_endpoint_url, self.__api_key, metrics)

    def __report_roundtrip_time(self, start_time: int) -> None:
        if not self.trace_id:
            return

        roundtrip_time = int(time.time() * 1000) - start_time

        post(
            self._metrics_endpoint_url,
            self.__api_key,
            {"roundtrip_time": roundtrip_time},
        )


class OrquestaBaseEntity:
    def __init__(
        self,
        dsn: str,
        endpointUrl: str,
        payloadKey: str,
    ):
        self.dsn = dsn
        self.__endpointUrl = endpointUrl
        self.__payloadKey = payloadKey

    def perform_request(
        self,
        key: str,
        context: Optional[dict] = None,
        metadata: Optional[dict] = None,
    ) -> Any:
        return post(
            self.__endpointUrl,
            self.dsn,
            {self.__payloadKey: [key], **(context or {}), **(metadata or {})},
        )
