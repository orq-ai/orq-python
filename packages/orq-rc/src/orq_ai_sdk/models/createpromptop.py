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


ModelType = Literal[
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

Format = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

Quality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

CreatePromptResponseFormatType = Literal["json_object"]


class ResponseFormat2TypedDict(TypedDict):
    type: CreatePromptResponseFormatType


class ResponseFormat2(BaseModel):
    type: CreatePromptResponseFormatType


ResponseFormatType = Literal["json_schema"]


class JSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class JSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class ResponseFormat1TypedDict(TypedDict):
    type: ResponseFormatType
    json_schema: JSONSchemaTypedDict


class ResponseFormat1(BaseModel):
    type: ResponseFormatType

    json_schema: JSONSchema


ResponseFormatTypedDict = TypeAliasType(
    "ResponseFormatTypedDict", Union[ResponseFormat2TypedDict, ResponseFormat1TypedDict]
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


ResponseFormat = TypeAliasType(
    "ResponseFormat", Union[ResponseFormat2, ResponseFormat1]
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


PhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

EncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class ModelParametersTypedDict(TypedDict):
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
    format_: NotRequired[Format]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[Quality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[ResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[PhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[EncodingFormat]
    r"""The format to return the embeddings"""


class ModelParameters(BaseModel):
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

    format_: Annotated[Optional[Format], pydantic.Field(alias="format")] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[Quality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[ResponseFormat], pydantic.Field(alias="responseFormat")
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[PhotoRealVersion], pydantic.Field(alias="photoRealVersion")
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[EncodingFormat] = None
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


Provider = Literal[
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
]

CreatePromptRole = Literal[
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

CreatePrompt2PromptsType = Literal["image_url"]


class CreatePrompt2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePrompt2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePrompt22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePrompt2PromptsType
    image_url: CreatePrompt2ImageURLTypedDict


class CreatePrompt22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePrompt2PromptsType

    image_url: CreatePrompt2ImageURL


CreatePrompt2Type = Literal["text"]


class CreatePrompt21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreatePrompt2Type
    text: str


class CreatePrompt21(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreatePrompt2Type

    text: str


CreatePromptContent2TypedDict = TypeAliasType(
    "CreatePromptContent2TypedDict",
    Union[CreatePrompt21TypedDict, CreatePrompt22TypedDict],
)


CreatePromptContent2 = TypeAliasType(
    "CreatePromptContent2", Union[CreatePrompt21, CreatePrompt22]
)


CreatePromptContentTypedDict = TypeAliasType(
    "CreatePromptContentTypedDict", Union[str, List[CreatePromptContent2TypedDict]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptContent = TypeAliasType(
    "CreatePromptContent", Union[str, List[CreatePromptContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptType = Literal["function"]


class CreatePromptFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptToolCallsTypedDict(TypedDict):
    type: CreatePromptType
    function: CreatePromptFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreatePromptToolCalls(BaseModel):
    type: CreatePromptType

    function: CreatePromptFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreatePromptMessagesTypedDict(TypedDict):
    role: CreatePromptRole
    r"""The role of the prompt message"""
    content: CreatePromptContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreatePromptToolCallsTypedDict]]


class CreatePromptMessages(BaseModel):
    role: CreatePromptRole
    r"""The role of the prompt message"""

    content: CreatePromptContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreatePromptToolCalls]] = None


class PromptConfigTypedDict(TypedDict):
    messages: List[CreatePromptMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_type: NotRequired[ModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[ModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[Provider]
    version: NotRequired[str]


class PromptConfig(BaseModel):
    messages: List[CreatePromptMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_type: Optional[ModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[ModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[Provider] = None

    version: Optional[str] = None


class MetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[str]]
    language: NotRequired[str]


class Metadata(BaseModel):
    use_cases: Optional[List[str]] = None

    language: Optional[str] = None


CreatePromptPromptsType = Literal["prompt", "snippet", "template"]


class CreatePromptRequestBodyTypedDict(TypedDict):
    display_name: str
    type: CreatePromptPromptsType
    description: NotRequired[Nullable[str]]
    prompt_config: NotRequired[PromptConfigTypedDict]
    metadata: NotRequired[MetadataTypedDict]
    key: NotRequired[str]


class CreatePromptRequestBody(BaseModel):
    display_name: str

    type: CreatePromptPromptsType

    description: OptionalNullable[str] = UNSET

    prompt_config: Optional[PromptConfig] = None

    metadata: Optional[Metadata] = None

    key: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "prompt_config", "metadata", "key"]
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


CreatePromptModelType = Literal[
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

CreatePromptFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

CreatePromptQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

CreatePromptResponseFormatPromptsResponseType = Literal["json_object"]


class CreatePromptResponseFormat2TypedDict(TypedDict):
    type: CreatePromptResponseFormatPromptsResponseType


class CreatePromptResponseFormat2(BaseModel):
    type: CreatePromptResponseFormatPromptsResponseType


CreatePromptResponseFormatPromptsType = Literal["json_schema"]


class CreatePromptResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class CreatePromptResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class CreatePromptResponseFormat1TypedDict(TypedDict):
    type: CreatePromptResponseFormatPromptsType
    json_schema: CreatePromptResponseFormatJSONSchemaTypedDict


class CreatePromptResponseFormat1(BaseModel):
    type: CreatePromptResponseFormatPromptsType

    json_schema: CreatePromptResponseFormatJSONSchema


CreatePromptResponseFormatTypedDict = TypeAliasType(
    "CreatePromptResponseFormatTypedDict",
    Union[CreatePromptResponseFormat2TypedDict, CreatePromptResponseFormat1TypedDict],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptResponseFormat = TypeAliasType(
    "CreatePromptResponseFormat",
    Union[CreatePromptResponseFormat2, CreatePromptResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


CreatePromptPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

CreatePromptEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class CreatePromptModelParametersTypedDict(TypedDict):
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
    format_: NotRequired[CreatePromptFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[CreatePromptQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[CreatePromptResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[CreatePromptPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[CreatePromptEncodingFormat]
    r"""The format to return the embeddings"""


class CreatePromptModelParameters(BaseModel):
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

    format_: Annotated[Optional[CreatePromptFormat], pydantic.Field(alias="format")] = (
        None
    )
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[CreatePromptQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[CreatePromptResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[CreatePromptPhotoRealVersion], pydantic.Field(alias="photoRealVersion")
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[CreatePromptEncodingFormat] = None
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


CreatePromptProvider = Literal[
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
]

CreatePromptPromptsRole = Literal[
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

CreatePrompt2PromptsResponse200Type = Literal["image_url"]


class CreatePrompt2PromptsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePrompt2PromptsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreatePrompt2Prompts2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePrompt2PromptsResponse200Type
    image_url: CreatePrompt2PromptsImageURLTypedDict


class CreatePrompt2Prompts2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreatePrompt2PromptsResponse200Type

    image_url: CreatePrompt2PromptsImageURL


CreatePrompt2PromptsResponseType = Literal["text"]


class CreatePrompt2Prompts1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreatePrompt2PromptsResponseType
    text: str


class CreatePrompt2Prompts1(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreatePrompt2PromptsResponseType

    text: str


CreatePromptContentPrompts2TypedDict = TypeAliasType(
    "CreatePromptContentPrompts2TypedDict",
    Union[CreatePrompt2Prompts1TypedDict, CreatePrompt2Prompts2TypedDict],
)


CreatePromptContentPrompts2 = TypeAliasType(
    "CreatePromptContentPrompts2", Union[CreatePrompt2Prompts1, CreatePrompt2Prompts2]
)


CreatePromptPromptsContentTypedDict = TypeAliasType(
    "CreatePromptPromptsContentTypedDict",
    Union[str, List[CreatePromptContentPrompts2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptPromptsContent = TypeAliasType(
    "CreatePromptPromptsContent", Union[str, List[CreatePromptContentPrompts2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreatePromptPromptsResponse200Type = Literal["function"]


class CreatePromptPromptsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptPromptsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreatePromptPromptsToolCallsTypedDict(TypedDict):
    type: CreatePromptPromptsResponse200Type
    function: CreatePromptPromptsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreatePromptPromptsToolCalls(BaseModel):
    type: CreatePromptPromptsResponse200Type

    function: CreatePromptPromptsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreatePromptPromptsMessagesTypedDict(TypedDict):
    role: CreatePromptPromptsRole
    r"""The role of the prompt message"""
    content: CreatePromptPromptsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreatePromptPromptsToolCallsTypedDict]]


class CreatePromptPromptsMessages(BaseModel):
    role: CreatePromptPromptsRole
    r"""The role of the prompt message"""

    content: CreatePromptPromptsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreatePromptPromptsToolCalls]] = None


class CreatePromptPromptConfigTypedDict(TypedDict):
    messages: List[CreatePromptPromptsMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_db_id: NotRequired[str]
    r"""The id of the resource"""
    model_type: NotRequired[CreatePromptModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[CreatePromptModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[CreatePromptProvider]
    integration_id: NotRequired[Nullable[str]]
    r"""The id of the resource"""
    version: NotRequired[str]


class CreatePromptPromptConfig(BaseModel):
    messages: List[CreatePromptPromptsMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_db_id: Optional[str] = None
    r"""The id of the resource"""

    model_type: Optional[CreatePromptModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[CreatePromptModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[CreatePromptProvider] = None

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


class CreatePromptMetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[str]]
    language: NotRequired[str]


class CreatePromptMetadata(BaseModel):
    use_cases: Optional[List[str]] = None

    language: Optional[str] = None


CreatePromptPromptsResponseType = Literal["prompt", "snippet", "template"]


class CreatePromptResponseBodyTypedDict(TypedDict):
    r"""Prompt created."""

    id: str
    r"""The id of the resource"""
    display_name: str
    domain_id: str
    r"""The id of the resource"""
    type: CreatePromptPromptsResponseType
    description: NotRequired[Nullable[str]]
    prompt_config: NotRequired[CreatePromptPromptConfigTypedDict]
    metadata: NotRequired[CreatePromptMetadataTypedDict]
    key: NotRequired[str]


class CreatePromptResponseBody(BaseModel):
    r"""Prompt created."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The id of the resource"""

    display_name: str

    domain_id: str
    r"""The id of the resource"""

    type: CreatePromptPromptsResponseType

    description: OptionalNullable[str] = UNSET

    prompt_config: Optional[CreatePromptPromptConfig] = None

    metadata: Optional[CreatePromptMetadata] = None

    key: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "prompt_config", "metadata", "key"]
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
