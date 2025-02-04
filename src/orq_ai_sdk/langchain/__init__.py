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

class LlmEvent(BaseModel):
    type: EventType
    run_id: str
    parameters: Optional[dict] = {}
    prompts: Optional[List[str]] = []
    messages: List[ChoiceMessage] = [] 
    start_timestamp: str = Field(default_factory=get_iso_string)
    end_timestamp: Optional[str] = None
    response_choices: List[Choice] = []
    usage: Optional[LlmUsage] = None

class OrqClient():
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url

    def log_event(self, event: LlmEvent):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        httpx.post(f"{self.api_url}/v2/traces/langchain", headers=headers, json=event.model_dump())

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
        self.events[str(run_id)] = LlmEvent(type=EventType.LLM, parameters={
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
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> Any:
        normalize_messages: List[ChoiceMessage] = []

        for root_messages in messages:
            for message in root_messages:
                if isinstance(message, HumanMessage):
                    normalize_messages.append(ChoiceMessage(role=LlmRole.USER, content=message.content))
                elif isinstance(message, SystemMessage):
                    normalize_messages.append(ChoiceMessage(role=LlmRole.SYSTEM, content=message.content))

        self.events[str(run_id)] = LlmEvent(type=EventType.LLM, parameters={
            "serialized": serialized,
            "metadata": metadata,
            "kwargs": kwargs,
        }, messages=normalize_messages, run_id=str(run_id))
        
    # pylint: disable=unused-argument
    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any
    ) -> Any:
        event: LlmEvent = self.events[str(run_id)]
        event.end_timestamp = get_iso_string()
        token_usage = response.llm_output['token_usage']
        event.usage = LlmUsage(input_tokens=token_usage['prompt_tokens'], output_tokens=token_usage['completion_tokens'])
        event.response_choices = []

        for index, choice in enumerate(response.generations[0]):
            event.response_choices.append(Choice(index=index, message=ChoiceMessage(role=LlmRole.SYSTEM, content=choice.text), finish_reason=choice.generation_info['finish_reason']))

        self.orq_client.log_event(event)

__all__ = [
    "OrqLangchainCallback"
]
