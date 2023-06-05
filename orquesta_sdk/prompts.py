import time
from typing import Any, Dict, Optional

from .cache import CacheStore
from .request import PROMPTS_URL
from .result import OrquestaBaseEntity, OrquestaResult
from .rule_type import OrquestaRuleType


class OrquestaPromptMetricsEconomics:
    def __init__(self, prompt_tokens: int, completion_tokens: int, total_tokens: int):
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = total_tokens


class OrquestaPromptMetrics:
    def __init__(
        self,
        score: Optional[float] = None,
        latency: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
        economics: Optional[OrquestaPromptMetricsEconomics] = None,
    ):
        self.score = score
        self.latency = latency
        self.metadata = metadata
        self.economics = economics


class OrquestaPromptResponse:
    def __init__(self, trace_id: str, value: Dict[str, Any], status: int):
        self.trace_id = trace_id
        self.value = value
        self.status = status


class OrquestaPromptResult(OrquestaResult):
    def __init__(
        self,
        api_key: str,
        start_time: int,
        value: Any,
        trace_id: Optional[str],
        type: Optional[OrquestaRuleType],
    ):
        super().__init__(api_key, PROMPTS_URL, start_time, value, trace_id, type)

        self.has_error = not bool(trace_id)


class OrquestaPrompts(OrquestaBaseEntity):
    def __init__(self, dsn: str, cache: CacheStore):
        super().__init__(dsn, PROMPTS_URL, "prompts")

        self.__cache = cache

    def query(
        self,
        prompt_key: str,
        context: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> OrquestaPromptResult:
        cached_result = self.__cache.get(prompt_key, context or {})

        if cached_result:
            return cached_result.result

        start_time = int(time.time() * 1000)

        response = self.perform_request(prompt_key, context, metadata)

        result = response.json().get(prompt_key, {})

        prompt_result = OrquestaPromptResult(
            self.dsn,
            start_time,
            result.get("value"),
            result.get("trace_id"),
            result.get("type"),
        )

        if result.get("trace_id") and result.get("value") is not None:
            self.__cache.set(prompt_key, prompt_result, context or {})

        return prompt_result
