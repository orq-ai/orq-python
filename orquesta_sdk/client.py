import os

from .rules import OrquestaRules
from .prompts import OrquestaPrompts

from .cache import CacheStore
from .utils import is_invalid_api_key


class OrquestaIncorrectAPIException(BaseException):
    """Raised if the provider API key is invalid."""

    pass


class OrquestaClienOptions:
    def __init__(self, ttl: int) -> None:
        self.ttl = ttl


class OrquestaClient:
    def __init__(self, api_key: str, options: OrquestaClienOptions = None):
        ttl = options.ttl if options else 3600

        cache = CacheStore(ttl=ttl)

        api_key = api_key or os.environ.get("ORQUESTA_API_KEY")

        if not api_key or is_invalid_api_key(api_key):
            raise OrquestaIncorrectAPIException("The provided API key is invalid.")

        self.rules = OrquestaRules(api_key, cache)
        self.prompts = OrquestaPrompts(api_key, cache)
