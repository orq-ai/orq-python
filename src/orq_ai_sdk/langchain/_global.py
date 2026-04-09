"""Global handler registration via LangChain's configure hook system."""

import os
from contextvars import ContextVar
from typing import Optional

from ._utils import logger

_handler_var: ContextVar = ContextVar("orq_langchain_handler", default=None)


def setup(
    *,
    api_key: Optional[str] = None,
    api_url: str = "https://my.orq.ai",
) -> None:
    """Enable automatic tracing for all LangChain/LangGraph calls.

    Reads ORQ_API_KEY from environment if api_key not provided.
    Uses sync handler by default -- LangChain automatically handles
    async contexts by running sync callbacks in a thread executor.
    """
    from ._handler import OrqLangchainCallback

    key = api_key or os.environ.get("ORQ_API_KEY")
    if not key:
        raise ValueError(
            "api_key must be provided or ORQ_API_KEY environment variable must be set"
        )

    handler = OrqLangchainCallback(api_key=key, api_url=api_url)
    _handler_var.set(handler)
    logger.debug("Orq LangChain tracing enabled")


def teardown() -> None:
    """Disable automatic tracing."""
    _handler_var.set(None)
    logger.debug("Orq LangChain tracing disabled")


def _register_hook() -> None:
    """Register the ContextVar with LangChain's configure hook system."""
    try:
        from langchain_core.tracers.context import register_configure_hook  # type: ignore

        register_configure_hook(context_var=_handler_var, inheritable=True)
    except ImportError:
        # Old langchain-core without register_configure_hook
        pass
    except Exception:
        logger.debug("Failed to register configure hook", exc_info=True)
