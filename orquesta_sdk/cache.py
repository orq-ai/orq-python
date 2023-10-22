import time
from typing import Any, Dict, Optional

from .utils import are_object_equals


class OrquestaCacheItem:
    def __init__(
        self, key: str, result, context: Dict[str, Any], created: int
    ):
        self.key = key
        self.result = result
        self.context = context
        self.created = created


class CacheStore:
    def __init__(self, ttl: int):
        self.cache: list[OrquestaCacheItem] = []
        self.ttl = ttl

    def get(self, key: str, context: Dict[str, Any]) -> Optional[OrquestaCacheItem]:
        return next(
            (
                item
                for item in self.cache
                if item.key == key
                and are_object_equals(item.context, context)
                and not self.is_expired(item.created, self.ttl)
            ),
            None,
        )

    def set(self, key: str, result: Any, context: Dict[str, Any]):
        self.cache.append(
            OrquestaCacheItem(key, result, context, int(time.time() * 1000))
        )

    def is_expired(self, cache_time: int, ttl: int) -> bool:
        return time.time() * 1000 - cache_time > ttl * 1000

    def flush_expired(self):
        self.cache = [
            item for item in self.cache if not self.is_expired(item.created, self.ttl)
        ]
