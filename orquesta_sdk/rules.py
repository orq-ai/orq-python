import time
from typing import Any, Dict, Optional

from .cache import CacheStore
from .request import RULES_URL
from .result import OrquestaBaseEntity, OrquestaResult
from .rule_type import OrquestaRuleType


class OrquestaRulesMetrics:
    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata


class OrquestaRuleResult(OrquestaResult):
    def __init__(
        self,
        dsn: str,
        start_time: int,
        value: Any,
        trace_id: Optional[str],
        type: Optional[OrquestaRuleType],
    ):
        super().__init__(dsn, RULES_URL, start_time, value, trace_id, type)
        self.default_matched = not trace_id


class OrquestaRules(OrquestaBaseEntity):
    def __init__(self, dsn: str, cache: CacheStore):
        super().__init__(dsn, RULES_URL, "rules")

        self.__cache = cache

    def query(
        self,
        rule_key: str,
        default_value: Any,
        context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> OrquestaRuleResult:
        cached_result = self.__cache.get(rule_key, context or {})

        if cached_result:
            return cached_result.result

        start_time = int(time.time() * 1000)

        response = self.perform_request(rule_key, context, metadata)

        result = response.json().get(rule_key, {})

        rule_result = OrquestaRuleResult(
            self.dsn,
            start_time,
            result.get("value", default_value),
            result.get("trace_id"),
            result.get("type"),
        )

        if result.get("trace_id") and result.get("value") is not None:
            self.__cache.set(rule_key, rule_result, context or {})

        return rule_result
