import time
from typing import Any, Dict, Optional

from .cache import CacheStore
from .remote_config_kind import OrquestaRemoteConfigKind
from .request import REMOTE_CONFIGS_URL
from .result import OrquestaBaseEntity, OrquestaResult


class OrquestaRemoteConfigMetrics:
    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata

    def to_dict(self):
        if not self.metadata:
            return {}
        return {
            "metadata": self.metadata,
        }


class OrquestaRemoteConfig(OrquestaResult):
    def __init__(
        self,
        dsn: str,
        start_time: int,
        value: Any,
        trace_id: Optional[str],
        config_type: Optional[OrquestaRemoteConfigKind],
    ):
        super().__init__(
            dsn, REMOTE_CONFIGS_URL, start_time, value, trace_id, config_type
        )
        self.default_matched = not trace_id

    def add_metrics(self, metrics: OrquestaRemoteConfigMetrics) -> None:
        return super().add_metrics(metrics.to_dict())


class OrquestaRemoteConfigs(OrquestaBaseEntity):
    def __init__(self, dsn: str, cache: CacheStore):
        super().__init__(dsn, REMOTE_CONFIGS_URL)

        self.__cache = cache

    def query(
        self,
        key: str,
        default_value: Any,
        context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> OrquestaRemoteConfig:
        cached_result = self.__cache.get(key, context or {})

        if cached_result:
            return cached_result.result

        start_time = int(time.time() * 1000)

        response = self.perform_request(key, context, metadata)

        result = response.json().get(key, {})

        config = OrquestaRemoteConfig(
            self.dsn,
            start_time,
            result.get("value", default_value),
            result.get("trace_id"),
            result.get("type"),
        )

        if result.get("trace_id") and result.get("value") is not None:
            self.__cache.set(key, config, context or {})

        return config
