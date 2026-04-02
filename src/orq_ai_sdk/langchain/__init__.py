"""Orq.ai LangChain integration -- automatic tracing via OTLP spans."""

try:
    from langchain_core.callbacks import BaseCallbackHandler  # type: ignore  # noqa: F401
except ImportError as exc:
    raise ModuleNotFoundError(
        "Please install langchain-core to use the orq.ai langchain native integration: "
        "'pip install langchain-core'"
    ) from exc

from ._handler import OrqLangchainCallback
from ._async_handler import AsyncOrqLangchainCallback
from ._global import setup, teardown

# Register the configure hook at import time so that setup() activates
# automatic tracing without any additional wiring.
from ._global import _register_hook

_register_hook()

__all__ = [
    "setup",
    "teardown",
    "OrqLangchainCallback",
    "AsyncOrqLangchainCallback",
]
