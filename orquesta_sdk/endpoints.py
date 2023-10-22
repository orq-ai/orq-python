from typing import Any, Dict, Optional

from .cache import CacheStore
from .options import OrquestaClientOptions
from .request import post, ENDPOINTS_API, METRICS_API
from reactivex import create, Observable

from .utils import extract_json


class OrquestaEndpointRequest:
    def __init__(
            self, key: str,
            context: Optional[Dict[str, Any]] = None,
            variables: Optional[Dict[str, str]] = None,
            metadata: Optional[Dict[str, Any]] = None
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
            trace_id: str
    ):
        self.__options = options
        self.content = content
        self.is_final = is_final
        self.trace_id = trace_id

    def add_metrics(self, metrics: OrquestaEndpointMetrics) -> None:
        body = metrics.to_dict()
        body["trace_id"] = self.trace_id

        post(
            url=METRICS_API,
            api_key=self.__options.api_key,
            body=body
        )


class OrquestaEndpoints:
    def __init__(self, options: OrquestaClientOptions, cache: CacheStore):
        self.__options = options
        self.__cache = cache

    def query(
            self,
            request: OrquestaEndpointRequest,
    ) -> OrquestaEndpoint:
        response = post(
            url=ENDPOINTS_API,
            api_key=self.__options.api_key,
            body=request.to_dict(),
        )

        data = response.json()

        return OrquestaEndpoint(
            self.__options,
            content=data.get("content"),
            is_final=data.get("is_final"),
            trace_id=data.get("trace_id"),
        )

    def stream(
            self,
            request: OrquestaEndpointRequest
    ) -> Observable[OrquestaEndpoint]:

        def handle_stream(observer, _):

            with post(
                    url=ENDPOINTS_API,
                    api_key=self.__options.api_key,
                    body=request.to_dict(),
                    stream=True
            ) as response:

                if response.ok is None or response.status_code != 200:
                    observer.on_error({
                        "errorCode": 500,
                        "providerErrorMessage": "An error occurred while processing your request.",
                    })

                for line in response.iter_lines():
                    if line:

                        data = extract_json(line)

                        if data.get("is_final") or "[DONE]" in line.decode("utf-8"):
                            observer.on_completed()
                            break

                        if data:
                            endpoint_chunk = OrquestaEndpoint(
                                self.__options,
                                content=data.get("content"),
                                is_final=data.get("is_final"),
                                trace_id=data.get("trace_id"),
                            )
                            observer.on_next(endpoint_chunk)

        source = create(handle_stream)

        return source
