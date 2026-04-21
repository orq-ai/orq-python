"""Async LangChain callback handler."""
# pylint: disable=unused-argument

from typing import Any, Dict, List, Optional, Sequence
from uuid import UUID

from langchain_core.callbacks import AsyncCallbackHandler  # type: ignore  # pylint: disable=import-error
from langchain_core.agents import AgentAction, AgentFinish  # type: ignore  # pylint: disable=import-error
from langchain_core.documents import Document  # type: ignore  # pylint: disable=import-error
from langchain_core.messages import BaseMessage  # type: ignore  # pylint: disable=import-error
from langchain_core.outputs import LLMResult  # type: ignore  # pylint: disable=import-error

from ._client import AsyncOrqTracesClient
from ._events import Events
from ._models import EventType, InFlightEvent
from ._span_builder import build_otlp_span, _nano_timestamp
from ._utils import (
    extract_model_name,
    extract_model_parameters,
    extract_token_usage,
    format_error,
    logger,
    normalize_messages,
    resolve_span_name,
)


class AsyncOrqLangchainCallback(AsyncCallbackHandler):
    """Async LangChain callback handler that sends traces to Orq as OTLP spans."""

    def __init__(self, api_key: str, api_url: str = "https://my.orq.ai"):
        self._events = Events()
        self._client = AsyncOrqTracesClient(api_key=api_key, api_url=api_url)

    def _start_event(
        self,
        run_id: UUID,
        parent_run_id: Optional[UUID],
        event_type: EventType,
        serialized: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
    ) -> InFlightEvent:
        rid = str(run_id)
        pid = str(parent_run_id) if parent_run_id else None

        self._events.map_parent(rid, pid)
        trace_id = self._events.get_trace_id(rid)
        span_id = self._events.get_span_id(rid)
        parent_span_id = self._events.get_span_id(pid) if pid else ""

        event = InFlightEvent(
            run_id=span_id,
            parent_run_id=parent_span_id,
            trace_id=trace_id,
            event_type=event_type,
            name=resolve_span_name(name, metadata, serialized),
            start_time_ns=_nano_timestamp(),
            serialized=serialized,
            metadata=metadata,
            tags=tags,
        )
        self._events.store(rid, event)
        return event

    async def _finish_and_send(self, run_id: UUID) -> None:
        rid = str(run_id)
        event = self._events.get(rid)
        if not event:
            return
        if not event.end_time_ns:
            event.end_time_ns = _nano_timestamp()
        span = build_otlp_span(event)
        await self._client.send_span(span)
        self._events.remove(rid)

    # ── LLM callbacks ──────────────────────────────────────────────

    async def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._start_event(
                run_id, parent_run_id, EventType.LLM, serialized, metadata, tags
            )
            event.prompts = prompts
            event.model_name = extract_model_name(serialized, kwargs)
            event.model_parameters = extract_model_parameters(kwargs)
        except Exception:
            logger.debug("on_llm_start error", exc_info=True)

    async def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._start_event(
                run_id, parent_run_id, EventType.LLM, serialized, metadata, tags
            )
            event.messages = normalize_messages(messages)
            event.model_name = extract_model_name(serialized, kwargs)
            event.model_parameters = extract_model_parameters(kwargs)
        except Exception:
            logger.debug("on_chat_model_start error", exc_info=True)

    async def on_llm_new_token(
        self,
        token: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if event:
                if event.streaming_tokens is None:
                    event.streaming_tokens = []
                event.streaming_tokens.append(token)
        except Exception:
            logger.debug("on_llm_new_token error", exc_info=True)

    async def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return

            event.end_time_ns = _nano_timestamp()
            event.token_usage = extract_token_usage(response)

            choices = []
            if response.generations:
                for idx, gen in enumerate(response.generations[0]):
                    finish_reason = None
                    if hasattr(gen, "generation_info") and gen.generation_info:
                        finish_reason = gen.generation_info.get("finish_reason")

                    content = gen.text
                    if not content and event.streaming_tokens:
                        content = "".join(event.streaming_tokens)

                    choices.append({
                        "index": idx,
                        "message": {"role": "assistant", "content": content},
                        "finish_reason": finish_reason,
                    })
            event.response_choices = choices

            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_llm_end error", exc_info=True)

    async def on_llm_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            err = format_error(error)
            event.error = {
                "type": type(error).__name__,
                "message": err["message"],
                "traceback": err["traceback"],
            }
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_llm_error error", exc_info=True)

    # ── Chain callbacks ────────────────────────────────────────────

    async def on_chain_start(
        self,
        serialized: Dict[str, Any],
        inputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._start_event(
                run_id, parent_run_id, EventType.CHAIN, serialized, metadata, tags,
                name=kwargs.get("name"),
            )
            event.inputs = inputs if isinstance(inputs, dict) else {"inputs": inputs}

            rid = str(run_id)
            if parent_run_id is None:
                self._events.set_root_if_needed(rid)
            elif self._events.is_graph_node(rid):
                span_id = self._events.get_span_id(rid)
                self._events.graph.on_node_start(event.name, span_id, str(self._events.root_run_id))
        except Exception:
            logger.debug("on_chain_start error", exc_info=True)

    async def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            rid = str(run_id)
            event = self._events.get(rid)
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            event.outputs = outputs if isinstance(outputs, dict) else {"outputs": outputs}

            if self._events.is_graph_node(rid):
                self._events.graph.on_node_end(event.name, str(self._events.root_run_id))

            if self._events.is_root(rid) and self._events.graph.has_nodes():
                event.graph_json = self._events.graph.build()

            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_chain_end error", exc_info=True)

    async def on_chain_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            err = format_error(error)
            event.error = {
                "type": type(error).__name__,
                "message": err["message"],
                "traceback": err["traceback"],
            }
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_chain_error error", exc_info=True)

    # ── Tool callbacks ─────────────────────────────────────────────

    async def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._start_event(
                run_id, parent_run_id, EventType.TOOL, serialized, metadata, tags
            )
            event.tool_input = input_str
        except Exception:
            logger.debug("on_tool_start error", exc_info=True)

    async def on_tool_end(
        self,
        output: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            event.tool_output = str(output)
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_tool_end error", exc_info=True)

    async def on_tool_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            err = format_error(error)
            event.error = {
                "type": type(error).__name__,
                "message": err["message"],
                "traceback": err["traceback"],
            }
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_tool_error error", exc_info=True)

    # ── Retriever callbacks ────────────────────────────────────────

    async def on_retriever_start(
        self,
        serialized: Dict[str, Any],
        query: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        try:
            event = self._start_event(
                run_id, parent_run_id, EventType.RETRIEVAL, serialized, metadata, tags
            )
            event.query = query
        except Exception:
            logger.debug("on_retriever_start error", exc_info=True)

    async def on_retriever_end(
        self,
        documents: Sequence[Document],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> None:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            event.documents = [
                doc.dict() if hasattr(doc, "dict") else {"page_content": doc.page_content, "metadata": doc.metadata}
                for doc in documents
            ]
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_retriever_end error", exc_info=True)

    async def on_retriever_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            err = format_error(error)
            event.error = {
                "type": type(error).__name__,
                "message": err["message"],
                "traceback": err["traceback"],
            }
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_retriever_error error", exc_info=True)

    # ── Agent callbacks ────────────────────────────────────────────

    async def on_agent_action(
        self,
        action: AgentAction,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            rid = str(run_id)
            event = self._events.get(rid)
            if not event:
                event = self._start_event(
                    run_id, parent_run_id, EventType.AGENT, {}, name="agent"
                )
            if event.agent_actions is None:
                event.agent_actions = []
            event.agent_actions.append({
                "tool": action.tool,
                "tool_input": str(action.tool_input),
                "log": action.log,
            })
        except Exception:
            logger.debug("on_agent_action error", exc_info=True)

    async def on_agent_finish(
        self,
        finish: AgentFinish,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event = self._events.get(str(run_id))
            if not event:
                return
            event.end_time_ns = _nano_timestamp()
            event.agent_finish = {
                "output": str(finish.return_values),
                "log": finish.log,
            }
            event.outputs = finish.return_values
            await self._finish_and_send(run_id)
        except Exception:
            logger.debug("on_agent_finish error", exc_info=True)

    # ── Retry callback ─────────────────────────────────────────────

    async def on_retry(
        self,
        retry_state: Any,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        logger.debug("on_retry run_id=%s attempt=%s", run_id, retry_state)
