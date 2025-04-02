"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk import utils
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetPromptVersionRequestTypedDict(TypedDict):
    prompt_id: str
    r"""The unique identifier of the prompt"""
    version_id: str
    r"""The unique identifier of the prompt version"""


class GetPromptVersionRequest(BaseModel):
    prompt_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the prompt"""

    version_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the prompt version"""


class GetPromptVersionPromptsResponseBodyData(BaseModel):
    message: str


class GetPromptVersionPromptsResponseBody(Exception):
    r"""Not Found - The prompt or prompt version does not exist."""

    data: GetPromptVersionPromptsResponseBodyData

    def __init__(self, data: GetPromptVersionPromptsResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetPromptVersionPromptsResponseBodyData)


GetPromptVersionModelType = Literal[
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

GetPromptVersionFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

GetPromptVersionQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

GetPromptVersionResponseFormatPromptsType = Literal["json_object"]


class GetPromptVersionResponseFormat2TypedDict(TypedDict):
    type: GetPromptVersionResponseFormatPromptsType


class GetPromptVersionResponseFormat2(BaseModel):
    type: GetPromptVersionResponseFormatPromptsType


GetPromptVersionResponseFormatType = Literal["json_schema"]


class GetPromptVersionResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class GetPromptVersionResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class GetPromptVersionResponseFormat1TypedDict(TypedDict):
    type: GetPromptVersionResponseFormatType
    json_schema: GetPromptVersionResponseFormatJSONSchemaTypedDict


class GetPromptVersionResponseFormat1(BaseModel):
    type: GetPromptVersionResponseFormatType

    json_schema: GetPromptVersionResponseFormatJSONSchema


GetPromptVersionResponseFormatTypedDict = TypeAliasType(
    "GetPromptVersionResponseFormatTypedDict",
    Union[
        GetPromptVersionResponseFormat2TypedDict,
        GetPromptVersionResponseFormat1TypedDict,
    ],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


GetPromptVersionResponseFormat = TypeAliasType(
    "GetPromptVersionResponseFormat",
    Union[GetPromptVersionResponseFormat2, GetPromptVersionResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


GetPromptVersionPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

GetPromptVersionEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""

GetPromptVersionReasoningEffort = Literal["low", "medium", "high"]
r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""


class GetPromptVersionModelParametersTypedDict(TypedDict):
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
    format_: NotRequired[GetPromptVersionFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[GetPromptVersionQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[GetPromptVersionResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[GetPromptVersionPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[GetPromptVersionEncodingFormat]
    r"""The format to return the embeddings"""
    reasoning_effort: NotRequired[GetPromptVersionReasoningEffort]
    r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""
    budget_tokens: NotRequired[float]
    r"""Gives the model enhanced reasoning capabilities for complex tasks. A value of 0 disables thinking. The minimum budget tokens for thinking are 1024. The Budget Tokens should never exceed the Max Tokens parameter. Only supported by `Anthropic`"""


class GetPromptVersionModelParameters(BaseModel):
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
        Optional[GetPromptVersionFormat], pydantic.Field(alias="format")
    ] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[GetPromptVersionQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[GetPromptVersionResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[GetPromptVersionPhotoRealVersion],
        pydantic.Field(alias="photoRealVersion"),
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[GetPromptVersionEncodingFormat] = None
    r"""The format to return the embeddings"""

    reasoning_effort: Annotated[
        Optional[GetPromptVersionReasoningEffort],
        pydantic.Field(alias="reasoningEffort"),
    ] = None
    r"""Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response."""

    budget_tokens: Annotated[Optional[float], pydantic.Field(alias="budgetTokens")] = (
        None
    )
    r"""Gives the model enhanced reasoning capabilities for complex tasks. A value of 0 disables thinking. The minimum budget tokens for thinking are 1024. The Budget Tokens should never exceed the Max Tokens parameter. Only supported by `Anthropic`"""

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
            "reasoningEffort",
            "budgetTokens",
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


GetPromptVersionProvider = Literal[
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

GetPromptVersionRole = Literal[
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

GetPromptVersion2PromptsType = Literal["image_url"]


class GetPromptVersion2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class GetPromptVersion2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class GetPromptVersion22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: GetPromptVersion2PromptsType
    image_url: GetPromptVersion2ImageURLTypedDict


class GetPromptVersion22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: GetPromptVersion2PromptsType

    image_url: GetPromptVersion2ImageURL


GetPromptVersion2Type = Literal["text"]


class GetPromptVersion21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: GetPromptVersion2Type
    text: str


class GetPromptVersion21(BaseModel):
    r"""Text content part of a prompt message"""

    type: GetPromptVersion2Type

    text: str


GetPromptVersionContent2TypedDict = TypeAliasType(
    "GetPromptVersionContent2TypedDict",
    Union[GetPromptVersion21TypedDict, GetPromptVersion22TypedDict],
)


GetPromptVersionContent2 = TypeAliasType(
    "GetPromptVersionContent2", Union[GetPromptVersion21, GetPromptVersion22]
)


GetPromptVersionContentTypedDict = TypeAliasType(
    "GetPromptVersionContentTypedDict",
    Union[str, List[GetPromptVersionContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


GetPromptVersionContent = TypeAliasType(
    "GetPromptVersionContent", Union[str, List[GetPromptVersionContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


GetPromptVersionType = Literal["function"]


class GetPromptVersionFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class GetPromptVersionFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class GetPromptVersionToolCallsTypedDict(TypedDict):
    type: GetPromptVersionType
    function: GetPromptVersionFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class GetPromptVersionToolCalls(BaseModel):
    type: GetPromptVersionType

    function: GetPromptVersionFunction

    id: Optional[str] = None

    index: Optional[float] = None


class GetPromptVersionMessagesTypedDict(TypedDict):
    role: GetPromptVersionRole
    r"""The role of the prompt message"""
    content: GetPromptVersionContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[GetPromptVersionToolCallsTypedDict]]


class GetPromptVersionMessages(BaseModel):
    role: GetPromptVersionRole
    r"""The role of the prompt message"""

    content: GetPromptVersionContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[GetPromptVersionToolCalls]] = None


class GetPromptVersionPromptConfigTypedDict(TypedDict):
    r"""A list of messages compatible with the openAI schema"""

    messages: List[GetPromptVersionMessagesTypedDict]
    stream: NotRequired[bool]
    model: NotRequired[str]
    model_db_id: NotRequired[str]
    r"""The id of the resource"""
    model_type: NotRequired[GetPromptVersionModelType]
    r"""The type of the model"""
    model_parameters: NotRequired[GetPromptVersionModelParametersTypedDict]
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: NotRequired[GetPromptVersionProvider]
    integration_id: NotRequired[Nullable[str]]
    r"""The id of the resource"""
    version: NotRequired[str]


class GetPromptVersionPromptConfig(BaseModel):
    r"""A list of messages compatible with the openAI schema"""

    messages: List[GetPromptVersionMessages]

    stream: Optional[bool] = None

    model: Optional[str] = None

    model_db_id: Optional[str] = None
    r"""The id of the resource"""

    model_type: Optional[GetPromptVersionModelType] = None
    r"""The type of the model"""

    model_parameters: Optional[GetPromptVersionModelParameters] = None
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: Optional[GetPromptVersionProvider] = None

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


GetPromptVersionUseCases = Literal[
    "Agents simulations",
    "Agents",
    "API interaction",
    "Autonomous Agents",
    "Chatbots",
    "Classification",
    "Code understanding",
    "Code writing",
    "Conversation",
    "Documents QA",
    "Evaluation",
    "Extraction",
    "Multi-modal",
    "Self-checking",
    "Sentiment analysis",
    "SQL",
    "Summarization",
    "Tagging",
    "Translation (document)",
    "Translation (sentences)",
]

GetPromptVersionLanguage = Literal[
    "Chinese", "Dutch", "English", "French", "German", "Russian", "Spanish"
]
r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class GetPromptVersionMetadataTypedDict(TypedDict):
    use_cases: NotRequired[List[GetPromptVersionUseCases]]
    r"""A list of use cases that the prompt is meant to be used for. Use this field to categorize the prompt for your own purpose"""
    language: NotRequired[GetPromptVersionLanguage]
    r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class GetPromptVersionMetadata(BaseModel):
    use_cases: Optional[List[GetPromptVersionUseCases]] = None
    r"""A list of use cases that the prompt is meant to be used for. Use this field to categorize the prompt for your own purpose"""

    language: Optional[GetPromptVersionLanguage] = None
    r"""The language that the prompt is written in. Use this field to categorize the prompt for your own purpose"""


class GetPromptVersionResponseBodyTypedDict(TypedDict):
    r"""Prompt version retrieved successfully."""

    id: str
    prompt_config: GetPromptVersionPromptConfigTypedDict
    r"""A list of messages compatible with the openAI schema"""
    timestamp: str
    created_by_id: NotRequired[Nullable[str]]
    updated_by_id: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    r"""The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose"""
    metadata: NotRequired[GetPromptVersionMetadataTypedDict]


class GetPromptVersionResponseBody(BaseModel):
    r"""Prompt version retrieved successfully."""

    id: Annotated[str, pydantic.Field(alias="_id")]

    prompt_config: GetPromptVersionPromptConfig
    r"""A list of messages compatible with the openAI schema"""

    timestamp: str

    created_by_id: OptionalNullable[str] = UNSET

    updated_by_id: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET
    r"""The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose"""

    metadata: Optional[GetPromptVersionMetadata] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_by_id", "updated_by_id", "description", "metadata"]
        nullable_fields = ["created_by_id", "updated_by_id", "description"]
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
