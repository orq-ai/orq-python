"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


DeploymentGetConfigInputsTypedDict = TypeAliasType(
    "DeploymentGetConfigInputsTypedDict", Union[str, float, bool]
)


DeploymentGetConfigInputs = TypeAliasType(
    "DeploymentGetConfigInputs", Union[str, float, bool]
)


DeploymentGetConfigDeploymentsRole = Literal[
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

DeploymentGetConfig2DeploymentsRequestRequestBodyType = Literal["image_url"]


class DeploymentGetConfig2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig22InputTypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsRequestRequestBodyType
    image_url: DeploymentGetConfig2ImageURLTypedDict


class DeploymentGetConfig22Input(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsRequestRequestBodyType

    image_url: DeploymentGetConfig2ImageURL


DeploymentGetConfig2DeploymentsRequestType = Literal["text"]


class DeploymentGetConfig21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2DeploymentsRequestType
    text: str


class DeploymentGetConfig21(BaseModel):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2DeploymentsRequestType

    text: str


DeploymentGetConfigContent2TypedDict = TypeAliasType(
    "DeploymentGetConfigContent2TypedDict",
    Union[DeploymentGetConfig21TypedDict, DeploymentGetConfig22InputTypedDict],
)


DeploymentGetConfigContent2 = TypeAliasType(
    "DeploymentGetConfigContent2",
    Union[DeploymentGetConfig21, DeploymentGetConfig22Input],
)


DeploymentGetConfigContentInputTypedDict = TypeAliasType(
    "DeploymentGetConfigContentInputTypedDict",
    Union[str, List[DeploymentGetConfigContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigContentInput = TypeAliasType(
    "DeploymentGetConfigContentInput", Union[str, List[DeploymentGetConfigContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigType = Literal["function"]


class DeploymentGetConfigDeploymentsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigDeploymentsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigDeploymentsToolCallsTypedDict(TypedDict):
    type: DeploymentGetConfigType
    function: DeploymentGetConfigDeploymentsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentGetConfigDeploymentsToolCalls(BaseModel):
    type: DeploymentGetConfigType

    function: DeploymentGetConfigDeploymentsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentGetConfigPrefixMessagesTypedDict(TypedDict):
    role: DeploymentGetConfigDeploymentsRole
    r"""The role of the prompt message"""
    content: DeploymentGetConfigContentInputTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentGetConfigDeploymentsToolCallsTypedDict]]


class DeploymentGetConfigPrefixMessages(BaseModel):
    role: DeploymentGetConfigDeploymentsRole
    r"""The role of the prompt message"""

    content: DeploymentGetConfigContentInput
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentGetConfigDeploymentsToolCalls]] = None


DeploymentGetConfigRole = Literal[
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

DeploymentGetConfig2DeploymentsType = Literal["image_url"]


class DeploymentGetConfig2ImageURLInputTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig2ImageURLInput(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsType
    image_url: DeploymentGetConfig2ImageURLInputTypedDict


class DeploymentGetConfig22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsType

    image_url: DeploymentGetConfig2ImageURLInput


DeploymentGetConfig2Type = Literal["text"]


class DeploymentGetConfig2Deployments1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2Type
    text: str


class DeploymentGetConfig2Deployments1(BaseModel):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2Type

    text: str


DeploymentGetConfigContent2InputTypedDict = TypeAliasType(
    "DeploymentGetConfigContent2InputTypedDict",
    Union[DeploymentGetConfig2Deployments1TypedDict, DeploymentGetConfig22TypedDict],
)


DeploymentGetConfigContent2Input = TypeAliasType(
    "DeploymentGetConfigContent2Input",
    Union[DeploymentGetConfig2Deployments1, DeploymentGetConfig22],
)


DeploymentGetConfigContentTypedDict = TypeAliasType(
    "DeploymentGetConfigContentTypedDict",
    Union[str, List[DeploymentGetConfigContent2InputTypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigContent = TypeAliasType(
    "DeploymentGetConfigContent", Union[str, List[DeploymentGetConfigContent2Input]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigDeploymentsType = Literal["function"]


class DeploymentGetConfigFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigToolCallsTypedDict(TypedDict):
    type: DeploymentGetConfigDeploymentsType
    function: DeploymentGetConfigFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentGetConfigToolCalls(BaseModel):
    type: DeploymentGetConfigDeploymentsType

    function: DeploymentGetConfigFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentGetConfigMessagesTypedDict(TypedDict):
    role: DeploymentGetConfigRole
    r"""The role of the prompt message"""
    content: DeploymentGetConfigContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentGetConfigToolCallsTypedDict]]


class DeploymentGetConfigMessages(BaseModel):
    role: DeploymentGetConfigRole
    r"""The role of the prompt message"""

    content: DeploymentGetConfigContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentGetConfigToolCalls]] = None


class DeploymentGetConfigMetadataTypedDict(TypedDict):
    r"""Metadata about the document"""

    file_name: NotRequired[str]
    r"""Name of the file the text is from."""
    file_type: NotRequired[str]
    r"""Content type of the file the text is from."""
    page_number: NotRequired[float]
    r"""The page number the text is from."""


class DeploymentGetConfigMetadata(BaseModel):
    r"""Metadata about the document"""

    file_name: Optional[str] = None
    r"""Name of the file the text is from."""

    file_type: Optional[str] = None
    r"""Content type of the file the text is from."""

    page_number: Optional[float] = None
    r"""The page number the text is from."""


class DeploymentGetConfigDocumentsTypedDict(TypedDict):
    text: str
    r"""The text content of the document"""
    metadata: NotRequired[DeploymentGetConfigMetadataTypedDict]
    r"""Metadata about the document"""


class DeploymentGetConfigDocuments(BaseModel):
    text: str
    r"""The text content of the document"""

    metadata: Optional[DeploymentGetConfigMetadata] = None
    r"""Metadata about the document"""


class DeploymentGetConfigInvokeOptionsTypedDict(TypedDict):
    include_retrievals: NotRequired[bool]
    r"""Whether to include the retrieved knowledge chunks in the response."""


class DeploymentGetConfigInvokeOptions(BaseModel):
    include_retrievals: Optional[bool] = False
    r"""Whether to include the retrieved knowledge chunks in the response."""


class DeploymentGetConfigRequestBodyTypedDict(TypedDict):
    key: str
    r"""The deployment key to invoke"""
    inputs: NotRequired[Dict[str, DeploymentGetConfigInputsTypedDict]]
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""
    context: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""
    prefix_messages: NotRequired[List[DeploymentGetConfigPrefixMessagesTypedDict]]
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""
    messages: NotRequired[List[DeploymentGetConfigMessagesTypedDict]]
    r"""A list of messages to send to the deployment."""
    file_ids: NotRequired[List[str]]
    r"""A list of file IDs that are associated with the deployment request."""
    metadata: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that you want to attach to the log generated by this request."""
    extra_params: NotRequired[Dict[str, Any]]
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""
    documents: NotRequired[List[DeploymentGetConfigDocumentsTypedDict]]
    r"""A list of relevant documents that evaluators and guardrails can cite to evaluate the user input or the model response based on your deployment settings."""
    invoke_options: NotRequired[DeploymentGetConfigInvokeOptionsTypedDict]


class DeploymentGetConfigRequestBody(BaseModel):
    key: str
    r"""The deployment key to invoke"""

    inputs: Optional[Dict[str, DeploymentGetConfigInputs]] = None
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""

    context: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""

    prefix_messages: Optional[List[DeploymentGetConfigPrefixMessages]] = None
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""

    messages: Optional[List[DeploymentGetConfigMessages]] = None
    r"""A list of messages to send to the deployment."""

    file_ids: Optional[List[str]] = None
    r"""A list of file IDs that are associated with the deployment request."""

    metadata: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that you want to attach to the log generated by this request."""

    extra_params: Optional[Dict[str, Any]] = None
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""

    documents: Optional[List[DeploymentGetConfigDocuments]] = None
    r"""A list of relevant documents that evaluators and guardrails can cite to evaluate the user input or the model response based on your deployment settings."""

    invoke_options: Optional[DeploymentGetConfigInvokeOptions] = None


DeploymentGetConfigDeploymentsResponseType = Literal[
    "chat",
    "completion",
    "embedding",
    "vision",
    "image",
    "tts",
    "stt",
    "rerank",
    "moderations",
]
r"""The type of the model. Current `chat`,`completion` and `image` are supported"""

DeploymentGetConfigDeploymentsResponseRole = Literal[
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

DeploymentGetConfig2DeploymentsResponse200Type = Literal["image_url"]


class DeploymentGetConfig2DeploymentsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig2DeploymentsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class DeploymentGetConfig2Deployments2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsResponse200Type
    image_url: DeploymentGetConfig2DeploymentsImageURLTypedDict


class DeploymentGetConfig2Deployments2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: DeploymentGetConfig2DeploymentsResponse200Type

    image_url: DeploymentGetConfig2DeploymentsImageURL


DeploymentGetConfig2DeploymentsResponseType = Literal["text"]


class DeploymentGetConfig2DeploymentsResponse1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2DeploymentsResponseType
    text: str


class DeploymentGetConfig2DeploymentsResponse1(BaseModel):
    r"""Text content part of a prompt message"""

    type: DeploymentGetConfig2DeploymentsResponseType

    text: str


DeploymentGetConfigContentDeployments2TypedDict = TypeAliasType(
    "DeploymentGetConfigContentDeployments2TypedDict",
    Union[
        DeploymentGetConfig2DeploymentsResponse1TypedDict,
        DeploymentGetConfig2Deployments2TypedDict,
    ],
)


DeploymentGetConfigContentDeployments2 = TypeAliasType(
    "DeploymentGetConfigContentDeployments2",
    Union[DeploymentGetConfig2DeploymentsResponse1, DeploymentGetConfig2Deployments2],
)


DeploymentGetConfigDeploymentsContentTypedDict = TypeAliasType(
    "DeploymentGetConfigDeploymentsContentTypedDict",
    Union[str, List[DeploymentGetConfigContentDeployments2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigDeploymentsContent = TypeAliasType(
    "DeploymentGetConfigDeploymentsContent",
    Union[str, List[DeploymentGetConfigContentDeployments2]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentGetConfigDeploymentsResponse200ApplicationJSONType = Literal["function"]


class DeploymentGetConfigDeploymentsResponse200FunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigDeploymentsResponse200Function(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentGetConfigDeploymentsResponseToolCallsTypedDict(TypedDict):
    type: DeploymentGetConfigDeploymentsResponse200ApplicationJSONType
    function: DeploymentGetConfigDeploymentsResponse200FunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentGetConfigDeploymentsResponseToolCalls(BaseModel):
    type: DeploymentGetConfigDeploymentsResponse200ApplicationJSONType

    function: DeploymentGetConfigDeploymentsResponse200Function

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentGetConfigDeploymentsMessagesTypedDict(TypedDict):
    role: DeploymentGetConfigDeploymentsResponseRole
    r"""The role of the prompt message"""
    content: DeploymentGetConfigDeploymentsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[
        List[DeploymentGetConfigDeploymentsResponseToolCallsTypedDict]
    ]


class DeploymentGetConfigDeploymentsMessages(BaseModel):
    role: DeploymentGetConfigDeploymentsResponseRole
    r"""The role of the prompt message"""

    content: DeploymentGetConfigDeploymentsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentGetConfigDeploymentsResponseToolCalls]] = None


DeploymentGetConfigFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

DeploymentGetConfigQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

DeploymentGetConfigResponseFormatType = Literal["json_object"]


class DeploymentGetConfigResponseFormat2TypedDict(TypedDict):
    type: DeploymentGetConfigResponseFormatType


class DeploymentGetConfigResponseFormat2(BaseModel):
    type: DeploymentGetConfigResponseFormatType


DeploymentGetConfigResponseFormatDeploymentsType = Literal["json_schema"]


class DeploymentGetConfigResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class DeploymentGetConfigResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class DeploymentGetConfigResponseFormat1TypedDict(TypedDict):
    type: DeploymentGetConfigResponseFormatDeploymentsType
    json_schema: DeploymentGetConfigResponseFormatJSONSchemaTypedDict


class DeploymentGetConfigResponseFormat1(BaseModel):
    type: DeploymentGetConfigResponseFormatDeploymentsType

    json_schema: DeploymentGetConfigResponseFormatJSONSchema


DeploymentGetConfigResponseFormatTypedDict = TypeAliasType(
    "DeploymentGetConfigResponseFormatTypedDict",
    Union[
        DeploymentGetConfigResponseFormat2TypedDict,
        DeploymentGetConfigResponseFormat1TypedDict,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


DeploymentGetConfigResponseFormat = TypeAliasType(
    "DeploymentGetConfigResponseFormat",
    Union[DeploymentGetConfigResponseFormat2, DeploymentGetConfigResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


DeploymentGetConfigPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

DeploymentGetConfigEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class ParametersTypedDict(TypedDict):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    max_tokens: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_k: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_p: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    frequency_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    presence_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    num_images: NotRequired[float]
    r"""Only supported on `image` models."""
    seed: NotRequired[float]
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""
    format_: NotRequired[DeploymentGetConfigFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[DeploymentGetConfigQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[DeploymentGetConfigResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[DeploymentGetConfigPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[DeploymentGetConfigEncodingFormat]
    r"""The format to return the embeddings"""


class Parameters(BaseModel):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: Optional[float] = None
    r"""Only supported on `chat` and `completion` models."""

    max_tokens: Annotated[Optional[float], pydantic.Field(alias="maxTokens")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_k: Annotated[Optional[float], pydantic.Field(alias="topK")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_p: Annotated[Optional[float], pydantic.Field(alias="topP")] = None
    r"""Only supported on `chat` and `completion` models."""

    frequency_penalty: Annotated[
        Optional[float], pydantic.Field(alias="frequencyPenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    presence_penalty: Annotated[
        Optional[float], pydantic.Field(alias="presencePenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    num_images: Annotated[Optional[float], pydantic.Field(alias="numImages")] = None
    r"""Only supported on `image` models."""

    seed: Optional[float] = None
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""

    format_: Annotated[
        Optional[DeploymentGetConfigFormat], pydantic.Field(alias="format")
    ] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[DeploymentGetConfigQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[DeploymentGetConfigResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[DeploymentGetConfigPhotoRealVersion],
        pydantic.Field(alias="photoRealVersion"),
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[DeploymentGetConfigEncodingFormat] = None
    r"""The format to return the embeddings"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "temperature",
            "maxTokens",
            "topK",
            "topP",
            "frequencyPenalty",
            "presencePenalty",
            "numImages",
            "seed",
            "format",
            "dimensions",
            "quality",
            "style",
            "responseFormat",
            "photoRealVersion",
            "encoding_format",
        ]
        nullable_fields = ["responseFormat"]
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


DeploymentGetConfigDeploymentsResponse200Type = Literal["function"]
r"""The type of the tool. Currently, only `function` is supported."""


class DeploymentGetConfigDeploymentsResponseFunctionTypedDict(TypedDict):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""
    description: NotRequired[str]
    r"""A description of what the function does, used by the model to choose when and how to call the function."""
    parameters: NotRequired[Dict[str, Any]]
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """


class DeploymentGetConfigDeploymentsResponseFunction(BaseModel):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""

    description: Optional[str] = None
    r"""A description of what the function does, used by the model to choose when and how to call the function."""

    parameters: Optional[Dict[str, Any]] = None
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """


class ToolsTypedDict(TypedDict):
    type: DeploymentGetConfigDeploymentsResponse200Type
    r"""The type of the tool. Currently, only `function` is supported."""
    function: DeploymentGetConfigDeploymentsResponseFunctionTypedDict


class Tools(BaseModel):
    type: DeploymentGetConfigDeploymentsResponse200Type
    r"""The type of the tool. Currently, only `function` is supported."""

    function: DeploymentGetConfigDeploymentsResponseFunction


class DeploymentGetConfigResponseBodyTypedDict(TypedDict):
    r"""The deployment configuration"""

    id: str
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""
    provider: str
    r"""The provider of the model"""
    model: str
    r"""The model of the configuration"""
    version: str
    r"""The current version of the deployment"""
    messages: List[DeploymentGetConfigDeploymentsMessagesTypedDict]
    parameters: ParametersTypedDict
    r"""Model Parameters: Not all parameters apply to every model"""
    type: NotRequired[DeploymentGetConfigDeploymentsResponseType]
    r"""The type of the model. Current `chat`,`completion` and `image` are supported"""
    tools: NotRequired[List[ToolsTypedDict]]
    r"""A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for."""


class DeploymentGetConfigResponseBody(BaseModel):
    r"""The deployment configuration"""

    id: str
    r"""A unique identifier for the response. Can be used to add metrics to the transaction."""

    provider: str
    r"""The provider of the model"""

    model: str
    r"""The model of the configuration"""

    version: str
    r"""The current version of the deployment"""

    messages: List[DeploymentGetConfigDeploymentsMessages]

    parameters: Parameters
    r"""Model Parameters: Not all parameters apply to every model"""

    type: Optional[DeploymentGetConfigDeploymentsResponseType] = None
    r"""The type of the model. Current `chat`,`completion` and `image` are supported"""

    tools: Optional[List[Tools]] = None
    r"""A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for."""
