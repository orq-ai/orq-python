import time
from typing import Any, Optional

from .options import OrquestaClientOptions
from .remote_config_kind import OrquestaRemoteConfigKind
from .request import post


class OrquestaResult:
    def __init__(
        self,
        api_key: str,
        endpoint_url: str,
        start_time: int,
        value: Any,
        trace_id: Optional[str],
        kind: Optional[OrquestaRemoteConfigKind],
    ):
        self.trace_id = trace_id
        self.kind = kind
        self.value = value
        self.__api_key = api_key
        self.__endpoint_url = endpoint_url

        self.__report_roundtrip_time(start_time)

    @property
    def _metrics_endpoint_url(self) -> str:
        return f"{self.__endpoint_url}/{self.trace_id}/metrics"

    def add_metrics(self, metrics) -> None:
        if not self.trace_id:
            return

        post(self._metrics_endpoint_url, self.__api_key, metrics)
