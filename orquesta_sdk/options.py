from typing import Optional


class OrquestaClientOptions:
    def __init__(
        self, api_key: str, ttl: int = 3600, environment: Optional[str] = None
    ) -> None:
        self.api_key = api_key
        self.ttl = ttl
        self.environment = environment
