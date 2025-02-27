from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Dict, List, Literal, Optional, Sequence, Union
from uuid import UUID

import httpx

try:
    from langchain_core.documents import Document # type: ignore
    from langchain.schema.agent import AgentAction, AgentFinish # type: ignore
    from langchain.callbacks.base import BaseCallbackHandler # type: ignore
    from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage # type: ignore
    from langchain_core.outputs import LLMResult # type: ignore
except ImportError as exc:
    raise ModuleNotFoundError("Please install langchain to use the orq.ai langchain native integration: 'pip install langchain'") from exc

def get_iso_string():
    # Get current datetime in UTC, timezone-aware
    current_utc_datetime = datetime.now(timezone.utc)
    # Format it to ISO 8601 string with 'Z' indicating UTC
    return current_utc_datetime.isoformat(timespec="milliseconds").replace(
        "+00:00", "Z"
    )

class EventType(str, Enum):
    LLM = "llm"
    Retrieval = "retrieval"
    Chain = "chain"
    Tool = "tool"
    Agent = "agent"

class LlmRole(str, Enum):
    SYSTEM = "system"
    USER = "user"

class LlmUsage(BaseModel):
    input_tokens: int
    output_tokens: int

class ChoiceMessage(BaseModel):
    content: Union[str, List[str]]
    role: LlmRole

class Choice(BaseModel):
    index: int
    message: ChoiceMessage
    finish_reason: Optional[str] = None

class BaseEvent(BaseModel):
    type: EventType
    parent_run_id: Optional[UUID] = None
    run_id: UUID
    start_timestamp: str = Field(default_factory=get_iso_string)
    end_timestamp: Optional[str] = None
    parameters: Optional[dict] = {}
    trace_id: Optional[str] = None

class LlmEvent(BaseEvent):
    type: EventType = EventType.LLM
    prompts: Optional[List[str]] = []
    messages: List[ChoiceMessage] = []
    response_choices: List[Choice] = []
    usage: Optional[LlmUsage] = None

class RetrievalEvent(BaseEvent):
    type: EventType = EventType.Retrieval
    query: str
    documents: List[dict] = []

class ChainEvent(BaseEvent):
    type: EventType = EventType.Chain
    inputs: dict = {}
    outputs: dict = {}

class ToolEvent(BaseEvent):
    type: EventType = EventType.Tool
    input_str: str
    output: str

class AgentEvent(BaseEvent):
    type: EventType = EventType.Agent
    action: AgentAction
    finish: AgentFinish

class OrqClient():
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def log_event(self, event: Union[LlmEvent, RetrievalEvent]):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        httpx.post(f"{self.api_url}/v2/traces/langchain", headers=headers, json=event.model_dump(mode="json", exclude_none=True))

class OrqLangchainCallback(BaseCallbackHandler):
    """Base callback handler that can be used to handle callbacks from langchain."""

    def __init__(self, api_key: str, api_url = "https://my.orq.ai"):
        self.events: Dict[str, LlmEvent] = {}
        self.orq_client = OrqClient(api_key, api_url)
        self.chain_parent_id_mappers: Dict[str, str] = {}

    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)

            self.events[str(run_id)] = LlmEvent(
                parameters={
                    "serialized": serialized,
                    "metadata": metadata,
                    "kwargs": kwargs,
                },
                prompts=prompts,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Llm start error: {e}")

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> Any:
        try:
            normalize_messages: List[ChoiceMessage] = []

            for root_messages in messages:
                for message in root_messages:
                    if isinstance(message, HumanMessage):
                        normalize_messages.append(ChoiceMessage(role=LlmRole.USER, content=message.content))
                    elif isinstance(message, SystemMessage):
                        normalize_messages.append(ChoiceMessage(role=LlmRole.SYSTEM, content=message.content))

            trace_id = None

            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)

            self.events[str(run_id)] = LlmEvent(
                parameters={
                    "serialized": serialized,
                    "metadata": metadata,
                    "kwargs": kwargs,
                },
                messages=normalize_messages,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Chat model start error: {e}")
        
    # pylint: disable=unused-argument
    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any
    ) -> Any:
        try:
            event: LlmEvent = self.events[str(run_id)]
            event.end_timestamp = get_iso_string()

            input_tokens = 0
            output_tokens = 0

            if 'token_usage' in response.llm_output:
                token_usage = response.llm_output['token_usage']
                input_tokens = token_usage['prompt_tokens']
                output_tokens = token_usage['completion_tokens']
            elif 'usage' in response.llm_output:
                token_usage = response.llm_output['usage']
                input_tokens = token_usage['input_tokens']
                output_tokens = token_usage['output_tokens']

            event.usage = LlmUsage(input_tokens=input_tokens, output_tokens=output_tokens)
            event.response_choices = []

            for index, choice in enumerate(response.generations[0]):
                finish_reason = None

                if 'generation_info' in choice:
                    finish_reason = choice.generation_info['finish_reason']

                event.response_choices.append(Choice(index=index, message=ChoiceMessage(role=LlmRole.SYSTEM, content=choice.text), finish_reason=finish_reason))

            self.orq_client.log_event(event)
        except Exception as e:
            print(f"Llm end error: {e}")

    def get_chain_trace_id(self, run_id: str):
        parent_run_id = self.chain_parent_id_mappers[run_id] if run_id in self.chain_parent_id_mappers else None

        if parent_run_id == None:
            return run_id

        return self.get_chain_trace_id(self.chain_parent_id_mappers[run_id])


    def on_chain_start(
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
            if parent_run_id:
                self.chain_parent_id_mappers[str(run_id)] = str(parent_run_id)
            else:
                self.chain_parent_id_mappers[str(run_id)] = None

            trace_id = None

            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)


            self.events[str(run_id)] = ChainEvent(
                parameters={
                    "serialized": serialized,
                    "metadata": metadata,
                    "kwargs": kwargs,
                    "tags": tags
                },
                inputs=inputs,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Chain start error: {e}")

    # pylint: disable=unused-argument
    def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event: ChainEvent = self.events[str(run_id)]
            event.end_timestamp = get_iso_string()
            event.outputs = outputs

            self.orq_client.log_event(event)
        except Exception as e:
            print(f"Chain end error: {e}")

    def on_retriever_start(
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
            trace_id = None

            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)

            self.events[str(run_id)] = RetrievalEvent(
                parameters={
                    "serialized": serialized,
                    "tags": tags,
                    "metadata": metadata,
                    "kwargs": kwargs,
                },
                query= query,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Retriever start error: {e}")

    # pylint: disable=unused-argument
    def on_retriever_end(
        self,
        documents: Sequence[Document],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        try:
            event: RetrievalEvent = self.events[str(run_id)]
            event.end_timestamp = get_iso_string()
            event.documents = documents

            self.orq_client.log_event(event)
        except Exception as e:
            print(f"Retriever end error: {e}")

    def on_agent_action(
        self,
        action: AgentAction,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            trace_id = None

            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)

            self.events[str(run_id)] = AgentEvent(
                    parameters={
                    "kwargs": kwargs,
                },
                action= action,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Agent action error: {e}")

    # pylint: disable=unused-argument
    def on_agent_finish(
        self,
        finish: AgentFinish,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event: AgentEvent = self.events[str(run_id)]
            event.end_timestamp = get_iso_string()
            event.finish = finish

            self.orq_client.log_event(event)
        except Exception as e:
            print(f"Agent finish error: {e}")

    def on_tool_start(
        self,
        serialized: Optional[Dict[str, Any]],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            trace_id = None

            if parent_run_id:
                trace_id = self.get_chain_trace_id(str(parent_run_id))
            else:
                trace_id = str(run_id)

            self.events[str(run_id)] = ToolEvent(
                    parameters={
                    "kwargs": kwargs,
                    "tags": tags,
                    "metadata": metadata,
                    "serialized": serialized,
                },
                input_str= input_str,
                run_id=run_id,
                parent_run_id=parent_run_id,
                trace_id=trace_id
            )
        except Exception as e:
            print(f"Tool start error: {e}")

    # pylint: disable=unused-argument
    def on_tool_end(
        self,
        output: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            event: ToolEvent = self.events[str(run_id)]
            event.end_timestamp = get_iso_string()
            event.output = output

            self.orq_client.log_event(event)
        except Exception as e:
            print(f"Tool end error: {e}")

__all__ = [
    "OrqLangchainCallback"
]
