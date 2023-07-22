import time
from typing import Any, Dict, Optional

from .cache import CacheStore
from .remote_config_kind import OrquestaRemoteConfigKind
from .request import PROMPTS_URL
from .result import OrquestaBaseEntity, OrquestaResult


class OrquestaPromptMetricsEconomics:
    def __init__(self, prompt_tokens: Optional[int], completion_tokens: int, total_tokens: Optional[int]):
        """
        Initializes an instance of the OrquestaPromptMetricsEconomics class.

        Parameters
        ----------
        prompt_tokens : int
            The number of tokens used in the initial prompt.
        completion_tokens : int
            The number of tokens used in the completion generated in response to the prompt.
        total_tokens : int
            The total number of tokens used, including both the prompt and completion.
        """
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = total_tokens


class OrquestaPromptMetrics:
    def __init__(
            self,
            score: Optional[float] = None,
            latency: Optional[int] = None,
            metadata: Optional[Dict[str, Any]] = None,
            llm_response: Optional[str] = None,
            economics: Optional[OrquestaPromptMetricsEconomics] = None
    ):
        self.score = score
        self.latency = latency
        self.metadata = metadata
        self.economics = economics
        self.llm_response = llm_response


class OrquestaPrompt(OrquestaResult):
    def __init__(
            self,
            api_key: str,
            start_time: int,
            value: Any,
            trace_id: Optional[str],
            kind: Optional[OrquestaRemoteConfigKind],
    ):
        super().__init__(api_key, PROMPTS_URL, start_time, value, trace_id, kind)

        self.has_error = not bool(trace_id)

    def add_metrics(self, metrics: OrquestaPromptMetrics) -> None:
        return super().add_metrics(metrics)


class OrquestaPrompts(OrquestaBaseEntity):
    def __init__(self, dsn: str, cache: CacheStore):
        super().__init__(dsn, PROMPTS_URL)

        self.__cache = cache

    def query(
            self,
            key: str,
            context: Optional[Dict[str, Any]] = None,
            variables: Optional[Dict[str, str]] = None,
            metadata: Optional[Dict[str, Any]] = None,
    ) -> OrquestaPrompt:
        cached_result = self.__cache.get(key, context or {})

        if cached_result:
            return cached_result.result

        start_time = int(time.time() * 1000)

        response = self.perform_request(
            key=key,
            context=context,
            metadata=metadata,
            variables=variables,
        )

        result = response.json().get(key, {})

        prompt = OrquestaPrompt(
            self.dsn,
            start_time,
            result.get("value"),
            result.get("trace_id"),
            result.get("type"),
        )

        if result.get("trace_id") and result.get("value") is not None:
            self.__cache.set(key, prompt, context)

        return prompt
