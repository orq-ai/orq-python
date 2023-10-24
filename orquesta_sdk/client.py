import os

from .cache import CacheStore
from .endpoints import OrquestaEndpoints
from .options import OrquestaClientOptions
from .prompts import OrquestaPrompts
from .remoteconfigs import OrquestaRemoteConfigs


class OrquestaInvalidAPIException(BaseException):
    """Raised if the provider API key is invalid."""

    pass


class OrquestaClient:
    def __init__(self, options: OrquestaClientOptions):
        cache = CacheStore(ttl=options.ttl)
        api_key = options.api_key or os.environ.get("ORQUESTA_API_KEY")

        if not api_key:
            raise OrquestaInvalidAPIException("The provided API key is invalid.")

        self.endpoints = OrquestaEndpoints(options)
        self.prompts = OrquestaPrompts(options, cache)
        self.remoteconfigs = OrquestaRemoteConfigs(options, cache)
