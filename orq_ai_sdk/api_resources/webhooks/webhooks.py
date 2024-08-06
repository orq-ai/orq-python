import hashlib
import hmac
import json
from typing import List, Optional, Union, Literal

from pydantic import Json, BaseModel


class LLMCallPromptConfig(BaseModel):
    stream: bool
    model: str
    model_type: str
    model_parameters: dict
    provider: str
    messages: List[dict]

    class Config:
        protected_namespaces = ()


class MessageChoiceContent(BaseModel):
    role: str
    content: str


class MessageChoiceImage(BaseModel):
    role: str
    url: str


class ToolCallFunction(BaseModel):
    name: str
    arguments: str


class MessageChoiceToolCall(BaseModel):
    id: Optional[str] = None
    index: Optional[int] = None
    type: Literal['function'] = 'function'
    function: ToolCallFunction


class MessageChoiceToolCalls(BaseModel):
    role: str
    content: Optional[str] = None
    tool_calls: List[MessageChoiceToolCall]


class MessageChoice(BaseModel):
    index: int
    message: Union[MessageChoiceContent, MessageChoiceImage, MessageChoiceToolCalls]
    finish_reason: str


class LLMCallPerformance(BaseModel):
    latency: float


class LLMCallUsage(BaseModel):
    total_tokens: int
    prompt_tokens: int
    completion_tokens: int


class LLMCallBilling(BaseModel):
    total_cost: float
    input_cost: float
    output_cost: float


class DeploymentInvokedData(BaseModel):
    prompt_config: LLMCallPromptConfig
    choices: List[MessageChoice]
    variables: List
    performance: LLMCallPerformance
    usage: LLMCallUsage
    billing: LLMCallBilling
    tools: List


class DeploymentInvokedMetadata(BaseModel):
    deployment_id: str
    deployment_variant_id: str
    deployment_log_id: str
    deployment_url: str
    deployment_variant_url: str
    deployment_log_url: str


class WebhookDeploymentInvokedEvent(BaseModel):
    id: str
    created: str
    type: str
    metadata: DeploymentInvokedMetadata
    data: DeploymentInvokedData


class Webhooks:
    def _generate_signature(self, payload: Json, secret: str):
        event_id = payload['id']
        created = payload['created']
        event_type = payload['type']

        payload_string = json.dumps(
            {"id": event_id, "created": created, "type": event_type},
            separators=(',', ':'),
            ensure_ascii=False
        )
        hmac_obj = hmac.new(secret.encode('utf-8'), payload_string.encode('utf-8'), hashlib.sha256)
        return hmac_obj.hexdigest()

    def construct_event(self, payload: Json, signature: str, secret: str):
        expected_signature = self._generate_signature(payload, secret)
        equal = hmac.compare_digest(signature.encode('utf-8'), expected_signature.encode('utf-8'))

        if not equal:
            from orq_ai_sdk.exceptions import SignatureVerificationException

            raise SignatureVerificationException

        return payload
