"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CreatePromptVersionModelType = Literal[
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
r"""The type of the model"""

CreatePromptVersionFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

CreatePromptVersionQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

CreatePromptVersionResponseFormatPromptsType = Literal["json_object"]


class CreatePromptVersionResponseFormat2TypedDict(TypedDict):
    type: CreatePromptVersionResponseFormatPromptsType


class CreatePromptVersionResponseFormat2(BaseModel):
    type: CreatePromptVersionResponseFormatPromptsType


CreatePromptVersionResponseFormatType = Literal["json_schema"]


class ResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class ResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class CreatePromptVersionResponseFormat1TypedDict(TypedDict):
    type: CreatePromptVersionResponseFormatType
    json_schema: ResponseFormatJSONSchemaTypedDict


class CreatePromptVersionResponseFormat1(BaseModel):
    type: CreatePromptVersionResponseFormatType

    json_schema: ResponseFormatJSONSchema


CreatePromptVersionResponseFormatTypedDict = TypeAliasType(
    "CreatePromptVersionResponseFormatTypedDict",
    Union[
        CreatePromptVersionResponseFormat2TypedDict,
        CreatePromptVersionResponseFormat1TypedDict,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptVersionResponseFormat = TypeAliasType(
    "CreatePromptVersionResponseFormat",
    Union[CreatePromptVersionResponseFormat2, CreatePromptVersionResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptVersionPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

CreatePromptVersionEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class CreatePromptVersionModelParametersTypedDict(TypedDict):
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
    format_: NotRequired[CreatePromptVersionFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[CreatePromptVersionQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[CreatePromptVersionResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[CreatePromptVersionPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[CreatePromptVersionEncodingFormat]
    r"""The format to return the embeddings"""


class CreatePromptVersionModelParameters(BaseModel):
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
        Optional[CreatePromptVersionFormat], pydantic.Field(alias="format")
    ] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[CreatePromptVersionQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[CreatePromptVersionResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[CreatePromptVersionPhotoRealVersion],
        pydantic.Field(alias="photoRealVersion"),
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[CreatePromptVersionEncodingFormat] = None
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


CreatePromptVersionProvider = Literal[
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

CreatePromptVersionRole = Literal[
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

CreatePromptVersion2PromptsType = Literal["image_url"]


class CreatePromptVersion2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePromptVersion2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePromptVersion22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePromptVersion2PromptsType
    image_url: CreatePromptVersion2ImageURLTypedDict


class CreatePromptVersion22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePromptVersion2PromptsType

    image_url: CreatePromptVersion2ImageURL


CreatePromptVersion2Type = Literal["text"]


class CreatePromptVersion21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreatePromptVersion2Type
    text: str


class CreatePromptVersion21(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreatePromptVersion2Type

    text: str


CreatePromptVersionContent2TypedDict = TypeAliasType(
    "CreatePromptVersionContent2TypedDict",
    Union[CreatePromptVersion21TypedDict, CreatePromptVersion22TypedDict],
)


CreatePromptVersionContent2 = TypeAliasType(
    "CreatePromptVersionContent2", Union[CreatePromptVersion21, CreatePromptVersion22]
)


CreatePromptVersionContentTypedDict = TypeAliasType(
    "CreatePromptVersionContentTypedDict",
    Union[str, List[CreatePromptVersionContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptVersionContent = TypeAliasType(
    "CreatePromptVersionContent", Union[str, List[CreatePromptVersionContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptVersionType = Literal["function"]


class CreatePromptVersionFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptVersionFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptVersionToolCallsTypedDict(TypedDict):
    type: CreatePromptVersionType
    function: CreatePromptVersionFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreatePromptVersionToolCalls(BaseModel):
    type: CreatePromptVersionType

    function: CreatePromptVersionFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreatePromptVersionMessagesTypedDict(TypedDict):
    role: CreatePromptVersionRole
    r"""The role of the prompt message"""
    content: CreatePromptVersionContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreatePromptVersionToolCallsTypedDict]]


class CreatePromptVersionMessages(BaseModel):
    role: CreatePromptVersionRole
    r"""The role of the prompt message"""

    content: CreatePromptVersionContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreatePromptVersionToolCalls]] = None


class CreatePromptVersionPromptConfigTypedDict(TypedDict):
    messages: List[CreatePromptVersionMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_type: NotRequired[CreatePromptVersionModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[CreatePromptVersionModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[CreatePromptVersionProvider]
    version: NotRequired[str]


class CreatePromptVersionPromptConfig(BaseModel):
    messages: List[CreatePromptVersionMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_type: Optional[CreatePromptVersionModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[CreatePromptVersionModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[CreatePromptVersionProvider] = None

    version: Optional[str] = None


class CreatePromptVersionMetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[str]]
    language: NotRequired[str]


class CreatePromptVersionMetadata(BaseModel):
    use_cases: Optional[List[str]] = None

    language: Optional[str] = None


class CreatePromptVersionRequestBodyTypedDict(TypedDict):
    id: str
    display_name: str
    prompt_config: CreatePromptVersionPromptConfigTypedDict
    metadata: CreatePromptVersionMetadataTypedDict
    commit: str
    timestamp: str
    description: NotRequired[Nullable[str]]


class CreatePromptVersionRequestBody(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    display_name: str

    prompt_config: CreatePromptVersionPromptConfig

    metadata: CreatePromptVersionMetadata

    commit: str

    timestamp: str

    description: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description"]
        nullable_fields = ["description"]
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


class CreatePromptVersionRequestTypedDict(TypedDict):
    id_param: str
    r"""Prompt ID"""
    request_body: NotRequired[CreatePromptVersionRequestBodyTypedDict]


class CreatePromptVersionRequest(BaseModel):
    id_param: Annotated[
        str,
        pydantic.Field(alias="id"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Prompt ID"""

    request_body: Annotated[
        Optional[CreatePromptVersionRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


CreatePromptVersionPromptsModelType = Literal[
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
r"""The type of the model"""

CreatePromptVersionPromptsFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

CreatePromptVersionPromptsQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

CreatePromptVersionResponseFormatPromptsResponse200Type = Literal["json_object"]


class CreatePromptVersionResponseFormatPrompts2TypedDict(TypedDict):
    type: CreatePromptVersionResponseFormatPromptsResponse200Type


class CreatePromptVersionResponseFormatPrompts2(BaseModel):
    type: CreatePromptVersionResponseFormatPromptsResponse200Type


CreatePromptVersionResponseFormatPromptsResponseType = Literal["json_schema"]


class CreatePromptVersionResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class CreatePromptVersionResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class CreatePromptVersionResponseFormatPrompts1TypedDict(TypedDict):
    type: CreatePromptVersionResponseFormatPromptsResponseType
    json_schema: CreatePromptVersionResponseFormatJSONSchemaTypedDict


class CreatePromptVersionResponseFormatPrompts1(BaseModel):
    type: CreatePromptVersionResponseFormatPromptsResponseType

    json_schema: CreatePromptVersionResponseFormatJSONSchema


CreatePromptVersionPromptsResponseFormatTypedDict = TypeAliasType(
    "CreatePromptVersionPromptsResponseFormatTypedDict",
    Union[
        CreatePromptVersionResponseFormatPrompts2TypedDict,
        CreatePromptVersionResponseFormatPrompts1TypedDict,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptVersionPromptsResponseFormat = TypeAliasType(
    "CreatePromptVersionPromptsResponseFormat",
    Union[
        CreatePromptVersionResponseFormatPrompts2,
        CreatePromptVersionResponseFormatPrompts1,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptVersionPromptsPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

CreatePromptVersionPromptsEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class CreatePromptVersionPromptsModelParametersTypedDict(TypedDict):
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
    format_: NotRequired[CreatePromptVersionPromptsFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[CreatePromptVersionPromptsQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[
        Nullable[CreatePromptVersionPromptsResponseFormatTypedDict]
    ]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[CreatePromptVersionPromptsPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[CreatePromptVersionPromptsEncodingFormat]
    r"""The format to return the embeddings"""


class CreatePromptVersionPromptsModelParameters(BaseModel):
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
        Optional[CreatePromptVersionPromptsFormat], pydantic.Field(alias="format")
    ] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[CreatePromptVersionPromptsQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[CreatePromptVersionPromptsResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[CreatePromptVersionPromptsPhotoRealVersion],
        pydantic.Field(alias="photoRealVersion"),
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[CreatePromptVersionPromptsEncodingFormat] = None
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


CreatePromptVersionPromptsProvider = Literal[
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

CreatePromptVersionPromptsRole = Literal[
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

CreatePromptVersion2PromptsResponse200Type = Literal["image_url"]


class CreatePromptVersion2PromptsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePromptVersion2PromptsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePromptVersion2Prompts2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePromptVersion2PromptsResponse200Type
    image_url: CreatePromptVersion2PromptsImageURLTypedDict


class CreatePromptVersion2Prompts2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePromptVersion2PromptsResponse200Type

    image_url: CreatePromptVersion2PromptsImageURL


CreatePromptVersion2PromptsResponseType = Literal["text"]


class CreatePromptVersion2Prompts1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreatePromptVersion2PromptsResponseType
    text: str


class CreatePromptVersion2Prompts1(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreatePromptVersion2PromptsResponseType

    text: str


CreatePromptVersionContentPrompts2TypedDict = TypeAliasType(
    "CreatePromptVersionContentPrompts2TypedDict",
    Union[CreatePromptVersion2Prompts1TypedDict, CreatePromptVersion2Prompts2TypedDict],
)


CreatePromptVersionContentPrompts2 = TypeAliasType(
    "CreatePromptVersionContentPrompts2",
    Union[CreatePromptVersion2Prompts1, CreatePromptVersion2Prompts2],
)


CreatePromptVersionPromptsContentTypedDict = TypeAliasType(
    "CreatePromptVersionPromptsContentTypedDict",
    Union[str, List[CreatePromptVersionContentPrompts2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptVersionPromptsContent = TypeAliasType(
    "CreatePromptVersionPromptsContent",
    Union[str, List[CreatePromptVersionContentPrompts2]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptVersionPromptsType = Literal["function"]


class CreatePromptVersionPromptsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptVersionPromptsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptVersionPromptsToolCallsTypedDict(TypedDict):
    type: CreatePromptVersionPromptsType
    function: CreatePromptVersionPromptsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreatePromptVersionPromptsToolCalls(BaseModel):
    type: CreatePromptVersionPromptsType

    function: CreatePromptVersionPromptsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreatePromptVersionPromptsMessagesTypedDict(TypedDict):
    role: CreatePromptVersionPromptsRole
    r"""The role of the prompt message"""
    content: CreatePromptVersionPromptsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreatePromptVersionPromptsToolCallsTypedDict]]


class CreatePromptVersionPromptsMessages(BaseModel):
    role: CreatePromptVersionPromptsRole
    r"""The role of the prompt message"""

    content: CreatePromptVersionPromptsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreatePromptVersionPromptsToolCalls]] = None


class CreatePromptVersionPromptsPromptConfigTypedDict(TypedDict):
    messages: List[CreatePromptVersionPromptsMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_db_id: NotRequired[str]
    r"""The id of the resource"""
    model_type: NotRequired[CreatePromptVersionPromptsModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[CreatePromptVersionPromptsModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[CreatePromptVersionPromptsProvider]
    integration_id: NotRequired[Nullable[str]]
    r"""The id of the resource"""
    version: NotRequired[str]


class CreatePromptVersionPromptsPromptConfig(BaseModel):
    messages: List[CreatePromptVersionPromptsMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_db_id: Optional[str] = None
    r"""The id of the resource"""

    model_type: Optional[CreatePromptVersionPromptsModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[CreatePromptVersionPromptsModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[CreatePromptVersionPromptsProvider] = None

    integration_id: OptionalNullable[str] = UNSET
    r"""The id of the resource"""

    version: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "stream",
            "model",
            "model_db_id",
            "model_type",
            "model_parameters",
            "provider",
            "integration_id",
            "version",
        ]
        nullable_fields = ["integration_id"]
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


class CreatePromptVersionPromptsMetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[str]]
    language: NotRequired[str]


class CreatePromptVersionPromptsMetadata(BaseModel):
    use_cases: Optional[List[str]] = None

    language: Optional[str] = None


class CreatePromptVersionResponseBodyTypedDict(TypedDict):
    r"""Prompt version created."""

    id: str
    display_name: str
    prompt_config: CreatePromptVersionPromptsPromptConfigTypedDict
    metadata: CreatePromptVersionPromptsMetadataTypedDict
    commit: str
    timestamp: str
    description: NotRequired[Nullable[str]]


class CreatePromptVersionResponseBody(BaseModel):
    r"""Prompt version created."""

    id: Annotated[str, pydantic.Field(alias="_id")]

    display_name: str

    prompt_config: CreatePromptVersionPromptsPromptConfig

    metadata: CreatePromptVersionPromptsMetadata

    commit: str

    timestamp: str

    description: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description"]
        nullable_fields = ["description"]
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
