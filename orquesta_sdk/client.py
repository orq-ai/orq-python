import os

from .cache import CacheStore
from .prompts import OrquestaPrompts
from .remote_configs import OrquestaRemoteConfigs
from .utils import is_invalid_api_key


class OrquestaIncorrectAPIException(BaseException):
    """Raised if the provider API key is invalid."""
    pass


class OrquestaClientOptions:
    def __init__(self, api_key: str, ttl: int = 3600) -> None:
        self.api_key = api_key
        self.ttl = ttl


class OrquestaClient:
    def __init__(self, options: OrquestaClientOptions = None):
        cache = CacheStore(ttl=options.ttl)

        api_key = options.api_key or os.environ.get("ORQUESTA_API_KEY")

        if not api_key or is_invalid_api_key(api_key):
            raise OrquestaIncorrectAPIException("The provided API key is invalid.")

        self.prompts = OrquestaPrompts(api_key, cache)
        self.remote_configs = OrquestaRemoteConfigs(api_key, cache)
