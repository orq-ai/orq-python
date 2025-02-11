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
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class DeploymentStreamGlobalsTypedDict(TypedDict):
    environment: NotRequired[str]
    contact_id: NotRequired[str]


class DeploymentStreamGlobals(BaseModel):
    environment: Annotated[
        Optional[str],
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None

    contact_id: Annotated[
        Optional[str],
        pydantic.Field(alias="contactId"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None


DeploymentStreamInputsTypedDict = TypeAliasType(
    "DeploymentStreamInputsTypedDict", Union[str, float, bool]
)


DeploymentStreamInputs = TypeAliasType(
    "DeploymentStreamInputs", Union[str, float, bool]
)


DeploymentStreamRole = Literal[
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

DeploymentStream2DeploymentsType = Literal["image_url"]


class DeploymentStream2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentStream2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentStream22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentStream2DeploymentsType
    image_url: DeploymentStream2ImageURLTypedDict


class DeploymentStream22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentStream2DeploymentsType

    image_url: DeploymentStream2ImageURL


DeploymentStream2Type = Literal["text"]


class DeploymentStream21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: DeploymentStream2Type
    text: str


class DeploymentStream21(BaseModel):
    r"""Text content part of a prompt message"""

    type: DeploymentStream2Type

    text: str


DeploymentStreamContent2TypedDict = TypeAliasType(
    "DeploymentStreamContent2TypedDict",
    Union[DeploymentStream21TypedDict, DeploymentStream22TypedDict],
)


DeploymentStreamContent2 = TypeAliasType(
    "DeploymentStreamContent2", Union[DeploymentStream21, DeploymentStream22]
)


DeploymentStreamContentTypedDict = TypeAliasType(
    "DeploymentStreamContentTypedDict",
    Union[str, List[DeploymentStreamContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentStreamContent = TypeAliasType(
    "DeploymentStreamContent", Union[str, List[DeploymentStreamContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentStreamType = Literal["function"]


class DeploymentStreamFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamToolCallsTypedDict(TypedDict):
    type: DeploymentStreamType
    function: DeploymentStreamFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentStreamToolCalls(BaseModel):
    type: DeploymentStreamType

    function: DeploymentStreamFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentStreamPrefixMessagesTypedDict(TypedDict):
    role: DeploymentStreamRole
    r"""The role of the prompt message"""
    content: DeploymentStreamContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentStreamToolCallsTypedDict]]


class DeploymentStreamPrefixMessages(BaseModel):
    role: DeploymentStreamRole
    r"""The role of the prompt message"""

    content: DeploymentStreamContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentStreamToolCalls]] = None


DeploymentStreamDeploymentsRole = Literal[
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

DeploymentStream2DeploymentsRequestRequestBodyType = Literal["image_url"]


class DeploymentStream2ImageURLInputTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentStream2ImageURLInput(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentStream22InputTypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentStream2DeploymentsRequestRequestBodyType
    image_url: DeploymentStream2ImageURLInputTypedDict


class DeploymentStream22Input(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentStream2DeploymentsRequestRequestBodyType

    image_url: DeploymentStream2ImageURLInput


DeploymentStream2DeploymentsRequestType = Literal["text"]


class DeploymentStream2Deployments1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: DeploymentStream2DeploymentsRequestType
    text: str


class DeploymentStream2Deployments1(BaseModel):
    r"""Text content part of a prompt message"""

    type: DeploymentStream2DeploymentsRequestType

    text: str


DeploymentStreamContent2InputTypedDict = TypeAliasType(
    "DeploymentStreamContent2InputTypedDict",
    Union[DeploymentStream2Deployments1TypedDict, DeploymentStream22InputTypedDict],
)


DeploymentStreamContent2Input = TypeAliasType(
    "DeploymentStreamContent2Input",
    Union[DeploymentStream2Deployments1, DeploymentStream22Input],
)


DeploymentStreamContentInputTypedDict = TypeAliasType(
    "DeploymentStreamContentInputTypedDict",
    Union[str, List[DeploymentStreamContent2InputTypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentStreamContentInput = TypeAliasType(
    "DeploymentStreamContentInput", Union[str, List[DeploymentStreamContent2Input]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentStreamDeploymentsType = Literal["function"]


class DeploymentStreamDeploymentsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamDeploymentsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamDeploymentsToolCallsTypedDict(TypedDict):
    type: DeploymentStreamDeploymentsType
    function: DeploymentStreamDeploymentsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentStreamDeploymentsToolCalls(BaseModel):
    type: DeploymentStreamDeploymentsType

    function: DeploymentStreamDeploymentsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentStreamMessagesTypedDict(TypedDict):
    role: DeploymentStreamDeploymentsRole
    r"""The role of the prompt message"""
    content: DeploymentStreamContentInputTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentStreamDeploymentsToolCallsTypedDict]]


class DeploymentStreamMessages(BaseModel):
    role: DeploymentStreamDeploymentsRole
    r"""The role of the prompt message"""

    content: DeploymentStreamContentInput
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentStreamDeploymentsToolCalls]] = None


class DeploymentStreamMetadataTypedDict(TypedDict):
    r"""Metadata about the document"""

    file_name: NotRequired[str]
    r"""Name of the file the text is from."""
    file_type: NotRequired[str]
    r"""Content type of the file the text is from."""
    page_number: NotRequired[float]
    r"""The page number the text is from."""


class DeploymentStreamMetadata(BaseModel):
    r"""Metadata about the document"""

    file_name: Optional[str] = None
    r"""Name of the file the text is from."""

    file_type: Optional[str] = None
    r"""Content type of the file the text is from."""

    page_number: Optional[float] = None
    r"""The page number the text is from."""


class DeploymentStreamDocumentsTypedDict(TypedDict):
    text: str
    r"""The text content of the document"""
    metadata: NotRequired[DeploymentStreamMetadataTypedDict]
    r"""Metadata about the document"""


class DeploymentStreamDocuments(BaseModel):
    text: str
    r"""The text content of the document"""

    metadata: Optional[DeploymentStreamMetadata] = None
    r"""Metadata about the document"""


class DeploymentStreamInvokeOptionsTypedDict(TypedDict):
    include_retrievals: NotRequired[bool]
    r"""Whether to include the retrieved knowledge chunks in the response."""


class DeploymentStreamInvokeOptions(BaseModel):
    include_retrievals: Optional[bool] = False
    r"""Whether to include the retrieved knowledge chunks in the response."""


class DeploymentStreamRequestBodyTypedDict(TypedDict):
    key: str
    r"""The deployment key to invoke"""
    inputs: NotRequired[Dict[str, DeploymentStreamInputsTypedDict]]
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""
    context: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""
    prefix_messages: NotRequired[List[DeploymentStreamPrefixMessagesTypedDict]]
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""
    messages: NotRequired[List[DeploymentStreamMessagesTypedDict]]
    r"""A list of messages to send to the deployment."""
    file_ids: NotRequired[List[str]]
    r"""A list of file IDs that are associated with the deployment request."""
    metadata: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that you want to attach to the log generated by this request."""
    extra_params: NotRequired[Dict[str, Any]]
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""
    documents: NotRequired[List[DeploymentStreamDocumentsTypedDict]]
    r"""A list of relevant documents that evaluators and guardrails can cite to evaluate the user input or the model response based on your deployment settings."""
    invoke_options: NotRequired[DeploymentStreamInvokeOptionsTypedDict]


class DeploymentStreamRequestBody(BaseModel):
    key: str
    r"""The deployment key to invoke"""

    inputs: Optional[Dict[str, DeploymentStreamInputs]] = None
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""

    context: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""

    prefix_messages: Optional[List[DeploymentStreamPrefixMessages]] = None
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""

    messages: Optional[List[DeploymentStreamMessages]] = None
    r"""A list of messages to send to the deployment."""

    file_ids: Optional[List[str]] = None
    r"""A list of file IDs that are associated with the deployment request."""

    metadata: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that you want to attach to the log generated by this request."""

    extra_params: Optional[Dict[str, Any]] = None
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""

    documents: Optional[List[DeploymentStreamDocuments]] = None
    r"""A list of relevant documents that evaluators and guardrails can cite to evaluate the user input or the model response based on your deployment settings."""

    invoke_options: Optional[DeploymentStreamInvokeOptions] = None


DeploymentStreamObject = Literal["chat", "completion", "image", "vision"]
r"""Indicates the type of model used to generate the response"""

DeploymentStreamProvider = Literal[
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
]
r"""The provider used to generate the response"""

DeploymentStreamMessageDeploymentsResponseRole = Literal[
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


class DeploymentStreamMessage3TypedDict(TypedDict):
    role: DeploymentStreamMessageDeploymentsResponseRole
    r"""The role of the prompt message"""
    url: str


class DeploymentStreamMessage3(BaseModel):
    role: DeploymentStreamMessageDeploymentsResponseRole
    r"""The role of the prompt message"""

    url: str


DeploymentStreamMessageDeploymentsRole = Literal[
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


class DeploymentStreamMessage2TypedDict(TypedDict):
    role: DeploymentStreamMessageDeploymentsRole
    r"""The role of the prompt message"""
    content: Nullable[str]


class DeploymentStreamMessage2(BaseModel):
    role: DeploymentStreamMessageDeploymentsRole
    r"""The role of the prompt message"""

    content: Nullable[str]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["content"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


DeploymentStreamMessageRole = Literal[
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

DeploymentStreamMessageType = Literal["function"]


class DeploymentStreamMessageFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamMessageFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentStreamMessageToolCallsTypedDict(TypedDict):
    type: DeploymentStreamMessageType
    function: DeploymentStreamMessageFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentStreamMessageToolCalls(BaseModel):
    type: DeploymentStreamMessageType

    function: DeploymentStreamMessageFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentStreamMessage1TypedDict(TypedDict):
    role: DeploymentStreamMessageRole
    r"""The role of the prompt message"""
    tool_calls: List[DeploymentStreamMessageToolCallsTypedDict]
    content: NotRequired[Nullable[str]]


class DeploymentStreamMessage1(BaseModel):
    role: DeploymentStreamMessageRole
    r"""The role of the prompt message"""

    tool_calls: List[DeploymentStreamMessageToolCalls]

    content: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["content"]
        nullable_fields = ["content"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


DeploymentStreamMessageTypedDict = TypeAliasType(
    "DeploymentStreamMessageTypedDict",
    Union[
        DeploymentStreamMessage2TypedDict,
        DeploymentStreamMessage3TypedDict,
        DeploymentStreamMessage1TypedDict,
    ],
)


DeploymentStreamMessage = TypeAliasType(
    "DeploymentStreamMessage",
    Union[DeploymentStreamMessage2, DeploymentStreamMessage3, DeploymentStreamMessage1],
)


class DeploymentStreamChoicesTypedDict(TypedDict):
    index: float
    message: NotRequired[DeploymentStreamMessageTypedDict]
    finish_reason: NotRequired[Nullable[str]]


class DeploymentStreamChoices(BaseModel):
    index: float

    message: Optional[DeploymentStreamMessage] = None

    finish_reason: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["message", "finish_reason"]
        nullable_fields = ["finish_reason"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class DeploymentStreamDeploymentsMetadataTypedDict(TypedDict):
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


class DeploymentStreamDeploymentsMetadata(BaseModel):
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

        for n, f in self.model_fields.items():
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


class DeploymentStreamRetrievalsTypedDict(TypedDict):
    document: str
    r"""Content of the retrieved chunk from the knowledge base"""
    metadata: DeploymentStreamDeploymentsMetadataTypedDict
    r"""Metadata of the retrieved chunk from the knowledge base"""


class DeploymentStreamRetrievals(BaseModel):
    document: str
    r"""Content of the retrieved chunk from the knowledge base"""

    metadata: DeploymentStreamDeploymentsMetadata
    r"""Metadata of the retrieved chunk from the knowledge base"""


class DeploymentStreamDataTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""
    created: NotRequired[datetime]
    r"""A timestamp indicating when the object was created. Usually in a standardized format like ISO 8601"""
    object: NotRequired[DeploymentStreamObject]
    r"""Indicates the type of model used to generate the response"""
    model: NotRequired[str]
    r"""The model used to generate the response"""
    provider: NotRequired[DeploymentStreamProvider]
    r"""The provider used to generate the response"""
    is_final: NotRequired[bool]
    r"""Indicates if the response is the final response"""
    integration_id: NotRequired[str]
    r"""Indicates integration id used to generate the response"""
    finalized: NotRequired[datetime]
    r"""A timestamp indicating when the object was finalized. Usually in a standardized format like ISO 8601"""
    system_fingerprint: NotRequired[Nullable[str]]
    r"""Provider backed system fingerprint."""
    choices: NotRequired[List[DeploymentStreamChoicesTypedDict]]
    r"""A list of choices generated by the model"""
    retrievals: NotRequired[List[DeploymentStreamRetrievalsTypedDict]]
    r"""List of documents retrieved from the knowledge base. This property is only available when the `include_retrievals` flag is set to `true` in the invoke settings. When stream is set to true, the `retrievals` property will be returned in the last streamed chunk where the property `is_final` is set to `true`."""
    provider_response: NotRequired[Any]
    r"""Response returned by the model provider. This functionality is only supported when streaming is not used. If streaming is used, the `provider_response` property will be set to `null`."""


class DeploymentStreamData(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""

    created: Optional[datetime] = None
    r"""A timestamp indicating when the object was created. Usually in a standardized format like ISO 8601"""

    object: Optional[DeploymentStreamObject] = None
    r"""Indicates the type of model used to generate the response"""

    model: Optional[str] = None
    r"""The model used to generate the response"""

    provider: Optional[DeploymentStreamProvider] = None
    r"""The provider used to generate the response"""

    is_final: Optional[bool] = None
    r"""Indicates if the response is the final response"""

    integration_id: Optional[str] = None
    r"""Indicates integration id used to generate the response"""

    finalized: Optional[datetime] = None
    r"""A timestamp indicating when the object was finalized. Usually in a standardized format like ISO 8601"""

    system_fingerprint: OptionalNullable[str] = UNSET
    r"""Provider backed system fingerprint."""

    choices: Optional[List[DeploymentStreamChoices]] = None
    r"""A list of choices generated by the model"""

    retrievals: Optional[List[DeploymentStreamRetrievals]] = None
    r"""List of documents retrieved from the knowledge base. This property is only available when the `include_retrievals` flag is set to `true` in the invoke settings. When stream is set to true, the `retrievals` property will be returned in the last streamed chunk where the property `is_final` is set to `true`."""

    provider_response: Optional[Any] = None
    r"""Response returned by the model provider. This functionality is only supported when streaming is not used. If streaming is used, the `provider_response` property will be set to `null`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "created",
            "object",
            "model",
            "provider",
            "is_final",
            "integration_id",
            "finalized",
            "system_fingerprint",
            "choices",
            "retrievals",
            "provider_response",
        ]
        nullable_fields = ["system_fingerprint"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class DeploymentStreamResponseBodyTypedDict(TypedDict):
    r"""Response from the gateway"""

    data: NotRequired[DeploymentStreamDataTypedDict]


class DeploymentStreamResponseBody(BaseModel):
    r"""Response from the gateway"""

    data: Optional[DeploymentStreamData] = None
