from datetime import datetime, timezone
from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

import httpx

try:
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
    parent_run_id: Optional[str] = None
    run_id: str
    start_timestamp: str = Field(default_factory=get_iso_string)
    end_timestamp: Optional[str] = None
    parameters: Optional[dict] = {}

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

class OrqClient():
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def log_event(self, event: Union[LlmEvent, RetrievalEvent]):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        print('log_event')
        print(event.model_dump())
        
        # httpx.post(f"{self.api_url}/v2/traces/langchain", headers=headers, json=event.model_dump())

from langchain_core.documents import Document
from typing import Sequence

class OrqLangchainCallback(BaseCallbackHandler):
    """Base callback handler that can be used to handle callbacks from langchain."""

    def __init__(self, api_key: str, api_url = "https://my.orq.ai"):
        self.events: Dict[str, LlmEvent] = {}
        self.orq_client = OrqClient(api_key, api_url)

    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        *,
        run_id: UUID,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        print('llm start')
        self.events[str(run_id)] = LlmEvent(parameters={
            "serialized": serialized,
            "metadata": metadata,
            "kwargs": kwargs,
        }, prompts=prompts, run_id=str(run_id))

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
        print('on chat model start')
        print('run_id', run_id)
        print('parent_run_id', parent_run_id)
        print()
        normalize_messages: List[ChoiceMessage] = []

        for root_messages in messages:
            for message in root_messages:
                if isinstance(message, HumanMessage):
                    normalize_messages.append(ChoiceMessage(role=LlmRole.USER, content=message.content))
                elif isinstance(message, SystemMessage):
                    normalize_messages.append(ChoiceMessage(role=LlmRole.SYSTEM, content=message.content))

        self.events[str(run_id)] = LlmEvent(parameters={
            "serialized": serialized,
            "metadata": metadata,
            "kwargs": kwargs,
        }, messages=normalize_messages, run_id=str(run_id), parent_run_id=str(parent_run_id))

        print(self.events[str(run_id)])
        
    # pylint: disable=unused-argument
    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any
    ) -> Any:
        print('on llm end')
        print('run_id', run_id)
        print('parent_run_id', parent_run_id)
        print()
        event: LlmEvent = self.events[str(run_id)]
        event.end_timestamp = get_iso_string()
        # print(response)

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
        # print(event.usage)
        event.response_choices = []

        # print(response)
        # print(len(response.generations))

        for index, choice in enumerate(response.generations[0]):
            finish_reason = None

            if 'generation_info' in choice:
                finish_reason = choice.generation_info['finish_reason']

            event.response_choices.append(Choice(index=index, message=ChoiceMessage(role=LlmRole.SYSTEM, content=choice.text), finish_reason=finish_reason))

        # print('events')

        print(self.events[str(run_id)])

        self.orq_client.log_event(event)

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
        print('onchainstart')
        print('parent_run_id', parent_run_id)
        print('run_id', run_id)
        # print('serialized')
        # print(serialized)
        print('inputs')
        print(inputs)
        # print('tags')
        # print(tags)
        # print('metadata')
        # print(metadata)
        print('kwargs')
        print(kwargs)
        print('-onchainstart')
        print()

        self.events[str(run_id)] = ChainEvent(parameters={
            "serialized": serialized,
            "metadata": metadata,
            "kwargs": kwargs,
            "tags": tags
        }, inputs=inputs, run_id=str(run_id), parent_run_id=str(parent_run_id))

    def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        print('onchainend')
        print(str(run_id))
        print('ouputs')
        print(outputs)
        print(parent_run_id)
        print('-onchainend')
        print()

        event: ChainEvent = self.events[str(run_id)]
        event.end_timestamp = get_iso_string()
        event.outputs = outputs

        self.orq_client.log_event(event)

    # def on_chain_error(
    #     self,
    #     error: BaseException,
    #     *,
    #     run_id: UUID,
    #     parent_run_id: Optional[UUID] = None,
    #     **kwargs: Any,
    # ) -> Any:
    #     print('onchainerror')
    #     print(str(run_id))
    #     print(error)
    #     print(parent_run_id)
    #     print('-onchainerror')

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
        print('retrieverstart')
        print('parent_run_id', parent_run_id)
        print('run_id', run_id)
        print(query)
        print(tags)
        print(metadata)
        print(kwargs)
        print('-retrieverstart')
        print()

        self.events[str(run_id)] = RetrievalEvent(parameters={
            "serialized": serialized,
            "tags": tags,
            "metadata": metadata,
            "kwargs": kwargs,
        }, query= query, run_id=str(run_id), parent_run_id=str(parent_run_id))

    def on_retriever_end(
        self,
        documents: Sequence[Document],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        print('on_retriever_end')
        # print('parent_run_id', parent_run_id)
        # print('run_id', run_id)
        print(documents)
        print(tags)
        print(kwargs)
        # print('-on_retriever_end')
        # print()

        event: RetrievalEvent = self.events[str(run_id)]
        event.end_timestamp = get_iso_string()
        event.documents = documents

        self.orq_client.log_event(event)

    # def on_retriever_error(
    #     self,
    #     error: BaseException,
    #     *,
    #     run_id: UUID,
    #     parent_run_id: Optional[UUID] = None,
    #     tags: Optional[List[str]] = None,
    #     **kwargs: Any,
    # ) -> None:
    #     action_event: ActionEvent = self.events.retriever[str(run_id)]
    #     error_event = ErrorEvent(trigger_event=action_event, exception=error)
    #     self.ao_client.record(error_event)


__all__ = [
    "OrqLangchainCallback"
]