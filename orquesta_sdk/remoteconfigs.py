from enum import Enum
from typing import Any, Dict, Optional

from .cache import CacheStore
from .options import OrquestaClientOptions
from .request import REMOTE_CONFIGS_API, post, METRICS_API


class OrquestaRemoteConfigKind(Enum):
    Boolean = "boolean"
    Integer = "integer"
    String = "string"
    List = "list"
    Json = "json"


class OrquestaRemoteConfigRequest:
    """
    OrquestaRemoteConfigRequest represents a configuration request for the Orquesta system.

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
            default_value: Any,
            context: Optional[Dict[str, Any]] = None,
            metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initializes a new OrquestaRemoteConfigRequest instance.

        Args:
            key (str): The configuration key.
            default_value (Any): The default value to be used if the key is not present.
            context (Optional[Dict[str, Any]]): Optional context information for the configuration request.
            metadata (Optional[Dict[str, Any]]): Optional metadata associated with the request.

        Returns:
            None
        """
        self.key = key  # The configuration key
        self.default_value = default_value  # The default value for the configuration key
        self.context = context  # Additional context for the request
        self.metadata = metadata  # Metadata related to the request

    def to_dict(self):
        """
        Returns a dictionary representation of the OrquestaRemoteConfigRequest instance.

        The returned dictionary will contain the key and optionally, the context and metadata
        if they are not None.

        Returns:
            Dict: A dictionary containing the key, context, and metadata of the instance.
        """
        value = {
            "keys": [self.key],
        }

        if self.context:
            value["context"] = self.context
        if self.metadata:
            value["metadata"] = self.metadata

        return value


class OrquestaRemoteConfigMetrics:
    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata

    def to_dict(self):
        value = {}

        if self.metadata:
            value["metadata"] = self.metadata

        return value


class OrquestaRemoteConfig:
    def __init__(
            self,
            options: OrquestaClientOptions,
            value: Any,
            trace_id: Optional[str],
            config_type: Optional[OrquestaRemoteConfigKind],
    ):
        self.__options = options
        self.value = value
        self.trace_id = trace_id
        self.config_type = config_type
        self.default_matched = not trace_id

    def add_metrics(self, metrics: OrquestaRemoteConfigMetrics) -> None:
        body = metrics.to_dict()

        body['trace_id'] = self.trace_id

        return post(
            api_key=self.__options.api_key,
            url=METRICS_API,
            body=body
        )


class OrquestaRemoteConfigs:
    def __init__(self, options: OrquestaClientOptions, cache: CacheStore):
        self.__options = options
        self.__cache = cache

    def query(
            self,
            request: OrquestaRemoteConfigRequest
    ) -> OrquestaRemoteConfig:

        context = request.context or {}

        cached_result = self.__cache.get(request.key, context)

        if cached_result:
            return cached_result.result

        response = post(
            url=REMOTE_CONFIGS_API,
            api_key=self.__options.api_key,
            body=request.to_dict()
        )

        data = response.json().get(request.key, {})

        config = OrquestaRemoteConfig(
            options=self.__options,
            value=data.get("value", request.default_value),
            trace_id=data.get("trace_id"),
            config_type=data.get("type"),
        )

        if config.trace_id and config.value is not None:
            self.__cache.set(request.key, config, context)

        return config
