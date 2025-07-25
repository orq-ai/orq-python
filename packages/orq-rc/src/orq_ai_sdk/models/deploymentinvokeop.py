"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, HeaderMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class DeploymentInvokeGlobalsTypedDict(TypedDict):
    environment: NotRequired[str]
    contact_id: NotRequired[str]


class DeploymentInvokeGlobals(BaseModel):
    environment: Annotated[
        Optional[str],
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None

    contact_id: Annotated[
        Optional[str],
        pydantic.Field(alias="contactId"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None


DeploymentInvokeObject = Literal["chat", "completion", "image", "vision"]
r"""Indicates the type of model used to generate the response"""

DeploymentInvokeProvider = Literal[
    "cohere",
    "openai",
    "anthropic",
    "huggingface",
    "replicate",
    "google",
    "google-ai",
    "azure",
    "aws",
    "anyscale",
    "perplexity",
    "groq",
    "fal",
    "leonardoai",
    "nvidia",
    "jina",
    "togetherai",
    "elevenlabs",
    "litellm",
    "openailike",
    "cerebras",
]
r"""The provider used to generate the response"""


class DeploymentInvokeMetadataTypedDict(TypedDict):
    r"""Metadata of the retrieved chunk from the knowledge base"""

    file_name: str
    r"""Name of the file"""
    page_number: Nullable[float]
    r"""Page number of the chunk"""
    file_type: str
    r"""Type of the file"""
    search_score: float
    r"""Search scores are normalized to be in the range [0, 1]. Search score is calculated based on `[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)` algorithm. Scores close to 1 indicate the document is closer to the query, and scores closer to 0 indicate the document is farther from the query."""
    rerank_score: NotRequired[float]
    r"""Rerank scores are normalized to be in the range [0, 1]. Scores close to 1 indicate a high relevance to the query, and scores closer to 0 indicate low relevance. It is not accurate to assume a score of 0.9 means the document is 2x more relevant than a document with a score of 0.45"""


class DeploymentInvokeMetadata(BaseModel):
    r"""Metadata of the retrieved chunk from the knowledge base"""

    file_name: str
    r"""Name of the file"""

    page_number: Nullable[float]
    r"""Page number of the chunk"""

    file_type: str
    r"""Type of the file"""

    search_score: float
    r"""Search scores are normalized to be in the range [0, 1]. Search score is calculated based on `[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)` algorithm. Scores close to 1 indicate the document is closer to the query, and scores closer to 0 indicate the document is farther from the query."""

    rerank_score: Optional[float] = None
    r"""Rerank scores are normalized to be in the range [0, 1]. Scores close to 1 indicate a high relevance to the query, and scores closer to 0 indicate low relevance. It is not accurate to assume a score of 0.9 means the document is 2x more relevant than a document with a score of 0.45"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["rerank_score"]
        nullable_fields = ["page_number"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class RetrievalsTypedDict(TypedDict):
    document: str
    r"""Content of the retrieved chunk from the knowledge base"""
    metadata: DeploymentInvokeMetadataTypedDict
    r"""Metadata of the retrieved chunk from the knowledge base"""


class Retrievals(BaseModel):
    document: str
    r"""Content of the retrieved chunk from the knowledge base"""

    metadata: DeploymentInvokeMetadata
    r"""Metadata of the retrieved chunk from the knowledge base"""


DeploymentInvokeMessageDeploymentsType = Literal["image"]

DeploymentInvokeMessageDeploymentsRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""


class Message3TypedDict(TypedDict):
    type: DeploymentInvokeMessageDeploymentsType
    role: DeploymentInvokeMessageDeploymentsRole
    r"""The role of the prompt message"""
    url: str


class Message3(BaseModel):
    type: DeploymentInvokeMessageDeploymentsType

    role: DeploymentInvokeMessageDeploymentsRole
    r"""The role of the prompt message"""

    url: str


DeploymentInvokeMessageType = Literal["content"]

DeploymentInvokeMessageRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""


class Message2TypedDict(TypedDict):
    type: DeploymentInvokeMessageType
    role: DeploymentInvokeMessageRole
    r"""The role of the prompt message"""
    content: Nullable[str]
    reasoning: NotRequired[str]
    r"""Internal thought process of the model"""
    reasoning_signature: NotRequired[str]
    r"""The signature holds a cryptographic token which verifies that the thinking block was generated by the model, and is verified when thinking is part of a multiturn conversation. This value should not be modified and should always be sent to the API when the reasoning is redacted. Currently only supported by `Anthropic`."""
    redacted_reasoning: NotRequired[str]
    r"""Occasionally the model's internal reasoning will be flagged by the safety systems of the provider. When this occurs, the provider will encrypt the reasoning. These redacted reasoning is decrypted when passed back to the API, allowing the model to continue its response without losing context."""


class Message2(BaseModel):
    type: DeploymentInvokeMessageType

    role: DeploymentInvokeMessageRole
    r"""The role of the prompt message"""

    content: Nullable[str]

    reasoning: Optional[str] = None
    r"""Internal thought process of the model"""

    reasoning_signature: Optional[str] = None
    r"""The signature holds a cryptographic token which verifies that the thinking block was generated by the model, and is verified when thinking is part of a multiturn conversation. This value should not be modified and should always be sent to the API when the reasoning is redacted. Currently only supported by `Anthropic`."""

    redacted_reasoning: Optional[str] = None
    r"""Occasionally the model's internal reasoning will be flagged by the safety systems of the provider. When this occurs, the provider will encrypt the reasoning. These redacted reasoning is decrypted when passed back to the API, allowing the model to continue its response without losing context."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["reasoning", "reasoning_signature", "redacted_reasoning"]
        nullable_fields = ["content"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


MessageType = Literal["tool_calls"]

MessageRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""

DeploymentInvokeMessageDeploymentsResponseType = Literal["function"]


class MessageFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class MessageFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class MessageToolCallsTypedDict(TypedDict):
    type: DeploymentInvokeMessageDeploymentsResponseType
    function: MessageFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class MessageToolCalls(BaseModel):
    type: DeploymentInvokeMessageDeploymentsResponseType

    function: MessageFunction

    id: Optional[str] = None

    index: Optional[float] = None


class Message1TypedDict(TypedDict):
    type: MessageType
    role: MessageRole
    r"""The role of the prompt message"""
    tool_calls: List[MessageToolCallsTypedDict]
    content: NotRequired[Nullable[str]]
    reasoning: NotRequired[str]
    r"""Internal thought process of the model"""
    reasoning_signature: NotRequired[str]
    r"""The signature holds a cryptographic token which verifies that the thinking block was generated by the model, and is verified when thinking is part of a multiturn conversation. This value should not be modified and should always be sent to the API when the reasoning is redacted. Currently only supported by `Anthropic`."""
    redacted_reasoning: NotRequired[str]
    r"""Occasionally the model's internal reasoning will be flagged by the safety systems of the provider. When this occurs, the provider will encrypt the reasoning. These redacted reasoning is decrypted when passed back to the API, allowing the model to continue its response without losing context."""


class Message1(BaseModel):
    type: MessageType

    role: MessageRole
    r"""The role of the prompt message"""

    tool_calls: List[MessageToolCalls]

    content: OptionalNullable[str] = UNSET

    reasoning: Optional[str] = None
    r"""Internal thought process of the model"""

    reasoning_signature: Optional[str] = None
    r"""The signature holds a cryptographic token which verifies that the thinking block was generated by the model, and is verified when thinking is part of a multiturn conversation. This value should not be modified and should always be sent to the API when the reasoning is redacted. Currently only supported by `Anthropic`."""

    redacted_reasoning: Optional[str] = None
    r"""Occasionally the model's internal reasoning will be flagged by the safety systems of the provider. When this occurs, the provider will encrypt the reasoning. These redacted reasoning is decrypted when passed back to the API, allowing the model to continue its response without losing context."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "content",
            "reasoning",
            "reasoning_signature",
            "redacted_reasoning",
        ]
        nullable_fields = ["content"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


MessageTypedDict = TypeAliasType(
    "MessageTypedDict", Union[Message3TypedDict, Message2TypedDict, Message1TypedDict]
)


Message = TypeAliasType("Message", Union[Message3, Message2, Message1])


class DeploymentInvokeChoicesTypedDict(TypedDict):
    index: float
    message: MessageTypedDict
    finish_reason: NotRequired[Nullable[str]]


class DeploymentInvokeChoices(BaseModel):
    index: float

    message: Message

    finish_reason: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["finish_reason"]
        nullable_fields = ["finish_reason"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class DeploymentInvokeResponseBodyTypedDict(TypedDict):
    r"""Successful operation"""

    id: str
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""
    created: datetime
    r"""A timestamp indicating when the object was created. Usually in a standardized format like ISO 8601"""
    object: DeploymentInvokeObject
    r"""Indicates the type of model used to generate the response"""
    model: str
    r"""The model used to generate the response"""
    provider: DeploymentInvokeProvider
    r"""The provider used to generate the response"""
    is_final: bool
    r"""Indicates if the response is the final response"""
    choices: List[DeploymentInvokeChoicesTypedDict]
    r"""A list of choices generated by the model"""
    integration_id: NotRequired[str]
    r"""Indicates integration id used to generate the response"""
    finalized: NotRequired[datetime]
    r"""A timestamp indicating when the object was finalized. Usually in a standardized format like ISO 8601"""
    system_fingerprint: NotRequired[Nullable[str]]
    r"""Provider backed system fingerprint."""
    retrievals: NotRequired[List[RetrievalsTypedDict]]
    r"""List of documents retrieved from the knowledge base. This property is only available when the `include_retrievals` flag is set to `true` in the invoke settings. When stream is set to true, the `retrievals` property will be returned in the last streamed chunk where the property `is_final` is set to `true`."""
    provider_response: NotRequired[Any]
    r"""Response returned by the model provider. This functionality is only supported when streaming is not used. If streaming is used, the `provider_response` property will be set to `null`."""


class DeploymentInvokeResponseBody(BaseModel):
    r"""Successful operation"""

    id: str
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""

    created: datetime
    r"""A timestamp indicating when the object was created. Usually in a standardized format like ISO 8601"""

    object: DeploymentInvokeObject
    r"""Indicates the type of model used to generate the response"""

    model: str
    r"""The model used to generate the response"""

    provider: DeploymentInvokeProvider
    r"""The provider used to generate the response"""

    is_final: bool
    r"""Indicates if the response is the final response"""

    choices: List[DeploymentInvokeChoices]
    r"""A list of choices generated by the model"""

    integration_id: Optional[str] = None
    r"""Indicates integration id used to generate the response"""

    finalized: Optional[datetime] = None
    r"""A timestamp indicating when the object was finalized. Usually in a standardized format like ISO 8601"""

    system_fingerprint: OptionalNullable[str] = UNSET
    r"""Provider backed system fingerprint."""

    retrievals: Optional[List[Retrievals]] = None
    r"""List of documents retrieved from the knowledge base. This property is only available when the `include_retrievals` flag is set to `true` in the invoke settings. When stream is set to true, the `retrievals` property will be returned in the last streamed chunk where the property `is_final` is set to `true`."""

    provider_response: Optional[Any] = None
    r"""Response returned by the model provider. This functionality is only supported when streaming is not used. If streaming is used, the `provider_response` property will be set to `null`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "integration_id",
            "finalized",
            "system_fingerprint",
            "retrievals",
            "provider_response",
        ]
        nullable_fields = ["system_fingerprint"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
