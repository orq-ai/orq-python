from typing import Any, Dict, Optional

from .exceptions import OrquestaException
from .options import OrquestaClientOptions
from .request import ENDPOINTS_API, METRICS_API, post
from .utils import extract_json, notify_error


class OrquestaEndpointRequest:
    def __init__(
        self,
        key: str,
        context: Optional[Dict[str, Any]] = None,
        variables: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.key = key
        self.context = context
        self.variables = variables
        self.metadata = metadata

    def to_dict(self):
        value = {
            "key": self.key,
        }

        if self.context:
            value["context"] = self.context
        if self.variables:
            value["variables"] = self.variables
        if self.metadata:
            value["metadata"] = self.metadata

        return value


class OrquestaEndpointMetrics:
    def __init__(
        self,
        score: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.score = score
        self.metadata = metadata

    def to_dict(self):
        value = {}

        if self.score is not None:
            value["score"] = self.score
        if self.metadata is not None:
            value["metadata"] = self.metadata

        return value


class OrquestaEndpoint:
    def __init__(
        self,
        options: OrquestaClientOptions,
        content: str,
        is_final: bool,
        trace_id: str,
    ):
        self.__options = options
        self.content = content
        self.is_final = is_final
        self.trace_id = trace_id

    def add_metrics(self, metrics: OrquestaEndpointMetrics) -> None:
        body = metrics.to_dict()
        body["trace_id"] = self.trace_id

        post(url=METRICS_API, api_key=self.__options.api_key, body=body)


class OrquestaEndpoints:
    def __init__(self, options: OrquestaClientOptions):
        self.__options = options

    def query(
        self,
        request: OrquestaEndpointRequest,
    ) -> OrquestaEndpoint:
        response = post(
            url=ENDPOINTS_API,
            api_key=self.__options.api_key,
            body=request.to_dict(),
        )

        if response.ok is None or response.status_code != 200:
            notify_error(response)

        data = response.json()

        return OrquestaEndpoint(
            self.__options,
            content=data.get("content"),
            is_final=data.get("is_final"),
            trace_id=data.get("trace_id"),
        )

    def stream(self, request: OrquestaEndpointRequest):
        with post(
            url=ENDPOINTS_API,
            api_key=self.__options.api_key,
            body=request.to_dict(),
            stream=True,
        ) as response:
            if response.ok is None or response.status_code != 200:
                notify_error(response)

            for line in response.iter_lines():
                if line:
                    data = extract_json(line)

                    if data:
                        yield OrquestaEndpoint(
                            self.__options,
                            content=data.get("content"),
                            is_final=data.get("is_final"),
                            trace_id=data.get("trace_id"),
                        )
