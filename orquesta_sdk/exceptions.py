from typing import Optional


class OrquestaException(Exception):
    def __init__(
        self,
        name: str,
        message: str,
        code: str,
        provider_error_message: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.name = name
        self.provider_error_message = provider_error_message
        self.code = code

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"
