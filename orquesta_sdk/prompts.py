import time
from typing import Any, Dict, Optional

from .cache import CacheStore
from .options import OrquestaClientOptions
from .request import PROMPTS_API, post, METRICS_API


class OrquestaPromptRequest:
    """
    OrquestaPromptRequest represents a configuration request for the Orquesta system.

    Attributes:
        key (str): The configuration key.
        default_value (Any): The default value to be used if the key is not present.
        context (Optional[Dict[str, Any]]): Optional context information for the configuration request.
        metadata (Optional[Dict[str, Any]]): Optional metadata associated with the request.

    Methods:
        to_dict(): Returns a dictionary representation of the instance.
    """

    def __init__(
            self,
            key: str,
            context: Optional[Dict[str, Any]] = None,
            variables: Optional[Dict[str, Any]] = None,
            metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initializes a new OrquestaPromptRequest instance.

        Args:
            key (str): The configuration key.
            context (Optional[Dict[str, Any]]): Optional context information for the configuration request.
            variables (Optional[Dict[str, Any]]): Optional variables associated with the request.
            metadata (Optional[Dict[str, Any]]): Optional metadata associated with the request.

        Returns:
            None
        """
        self.key = key  # The configuration key
        self.context = context  # Additional context for the request
        self.variables = variables  # Additional variables for the request
        self.metadata = metadata  # Metadata related to the request

    def to_dict(self):
        """
        Returns a dictionary representation of the OrquestaPromptRequest instance.

        The returned dictionary will contain the key and optionally, the context and metadata
        if they are not None.

        Returns:
            Dict: A dictionary containing the keys, context, and metadata of the instance.
        """
        value = {
            "keys": [self.key],
        }

        if self.context:
            value["context"] = self.context
        if self.variables:
            value["variables"] = self.variables
        if self.metadata:
            value["metadata"] = self.metadata

        return value


class OrquestaPromptMetricsEconomics:
    def __init__(
            self,
            prompt_tokens: Optional[int],
            completion_tokens: int,
            total_tokens: Optional[int],
    ):
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
            economics: Optional[OrquestaPromptMetricsEconomics] = None,
    ):
        self.score = score
        self.latency = latency
        self.metadata = metadata
        self.economics = economics
        self.llm_response = llm_response

    def to_dict(self):
        value = {}

        if self.score is not None:
            value["score"] = self.score
        if self.latency is not None:
            value["latency"] = self.latency
        if self.metadata is not None:
            value["metadata"] = self.metadata
        if self.economics is not None:
            value["economics"] = self.economics
        if self.llm_response is not None:
            value["llm_response"] = self.llm_response

        return value


class OrquestaPrompt:
    def __init__(
            self,
            options: OrquestaClientOptions,
            value: Any,
            trace_id: Optional[str],
    ):
        self.__options = options
        self.value = value
        self.trace_id = trace_id
        self.has_error = not bool(trace_id)

    def add_metrics(self, metrics: OrquestaPromptMetrics) -> None:
        body = metrics.to_dict()
        body['trace_id'] = self.trace_id

        return post(
            api_key=self.__options.api_key,
            url=METRICS_API,
            body=body
        )


class OrquestaPrompts:
    def __init__(self, options: OrquestaClientOptions, cache: CacheStore):
        self.__options = options
        self.__cache = cache

    def query(
            self,
            request: OrquestaPromptRequest,
    ) -> OrquestaPrompt:

        context = request.context or {}

        cached_result = self.__cache.get(request.key, context)

        if cached_result:
            return cached_result.result

        response = post(
            url=PROMPTS_API,
            api_key=self.__options.api_key,
            body=request.to_dict()
        )

        data = response.json().get(request.key, {})

        prompt = OrquestaPrompt(
            options=self.__options,
            value=data.get("value"),
            trace_id=data.get("trace_id")
        )

        if prompt.trace_id and prompt.value is not None:
            self.__cache.set(request.key, prompt, context)

        return prompt
