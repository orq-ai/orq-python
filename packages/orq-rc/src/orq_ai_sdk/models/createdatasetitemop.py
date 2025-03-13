"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CreateDatasetItemRole = Literal[
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

CreateDatasetItem2DatasetsType = Literal["image_url"]


class CreateDatasetItem2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreateDatasetItem2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreateDatasetItem22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreateDatasetItem2DatasetsType
    image_url: CreateDatasetItem2ImageURLTypedDict


class CreateDatasetItem22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreateDatasetItem2DatasetsType

    image_url: CreateDatasetItem2ImageURL


CreateDatasetItem2Type = Literal["text"]


class CreateDatasetItem21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreateDatasetItem2Type
    text: str


class CreateDatasetItem21(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreateDatasetItem2Type

    text: str


CreateDatasetItemContent2TypedDict = TypeAliasType(
    "CreateDatasetItemContent2TypedDict",
    Union[CreateDatasetItem21TypedDict, CreateDatasetItem22TypedDict],
)


CreateDatasetItemContent2 = TypeAliasType(
    "CreateDatasetItemContent2", Union[CreateDatasetItem21, CreateDatasetItem22]
)


CreateDatasetItemContentTypedDict = TypeAliasType(
    "CreateDatasetItemContentTypedDict",
    Union[str, List[CreateDatasetItemContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreateDatasetItemContent = TypeAliasType(
    "CreateDatasetItemContent", Union[str, List[CreateDatasetItemContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreateDatasetItemType = Literal["function"]


class CreateDatasetItemFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreateDatasetItemFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreateDatasetItemToolCallsTypedDict(TypedDict):
    type: CreateDatasetItemType
    function: CreateDatasetItemFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreateDatasetItemToolCalls(BaseModel):
    type: CreateDatasetItemType

    function: CreateDatasetItemFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreateDatasetItemMessagesTypedDict(TypedDict):
    role: CreateDatasetItemRole
    r"""The role of the prompt message"""
    content: CreateDatasetItemContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreateDatasetItemToolCallsTypedDict]]


class CreateDatasetItemMessages(BaseModel):
    role: CreateDatasetItemRole
    r"""The role of the prompt message"""

    content: CreateDatasetItemContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreateDatasetItemToolCalls]] = None


class CreateDatasetItemRequestBodyTypedDict(TypedDict):
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[CreateDatasetItemMessagesTypedDict]]
    r"""The prompt template messages"""
    expected_output: NotRequired[str]


class CreateDatasetItemRequestBody(BaseModel):
    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[CreateDatasetItemMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None


class CreateDatasetItemRequestTypedDict(TypedDict):
    dataset_id: str
    request_body: NotRequired[CreateDatasetItemRequestBodyTypedDict]


class CreateDatasetItemRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[CreateDatasetItemRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


CreateDatasetItemDatasetsRole = Literal[
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

CreateDatasetItem2DatasetsResponse200Type = Literal["image_url"]


class CreateDatasetItem2DatasetsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreateDatasetItem2DatasetsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class CreateDatasetItem2Datasets2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreateDatasetItem2DatasetsResponse200Type
    image_url: CreateDatasetItem2DatasetsImageURLTypedDict


class CreateDatasetItem2Datasets2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: CreateDatasetItem2DatasetsResponse200Type

    image_url: CreateDatasetItem2DatasetsImageURL


CreateDatasetItem2DatasetsResponseType = Literal["text"]


class CreateDatasetItem2Datasets1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: CreateDatasetItem2DatasetsResponseType
    text: str


class CreateDatasetItem2Datasets1(BaseModel):
    r"""Text content part of a prompt message"""

    type: CreateDatasetItem2DatasetsResponseType

    text: str


CreateDatasetItemContentDatasets2TypedDict = TypeAliasType(
    "CreateDatasetItemContentDatasets2TypedDict",
    Union[CreateDatasetItem2Datasets1TypedDict, CreateDatasetItem2Datasets2TypedDict],
)


CreateDatasetItemContentDatasets2 = TypeAliasType(
    "CreateDatasetItemContentDatasets2",
    Union[CreateDatasetItem2Datasets1, CreateDatasetItem2Datasets2],
)


CreateDatasetItemDatasetsContentTypedDict = TypeAliasType(
    "CreateDatasetItemDatasetsContentTypedDict",
    Union[str, List[CreateDatasetItemContentDatasets2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreateDatasetItemDatasetsContent = TypeAliasType(
    "CreateDatasetItemDatasetsContent",
    Union[str, List[CreateDatasetItemContentDatasets2]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


CreateDatasetItemDatasetsType = Literal["function"]


class CreateDatasetItemDatasetsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class CreateDatasetItemDatasetsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class CreateDatasetItemDatasetsToolCallsTypedDict(TypedDict):
    type: CreateDatasetItemDatasetsType
    function: CreateDatasetItemDatasetsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class CreateDatasetItemDatasetsToolCalls(BaseModel):
    type: CreateDatasetItemDatasetsType

    function: CreateDatasetItemDatasetsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class CreateDatasetItemDatasetsMessagesTypedDict(TypedDict):
    role: CreateDatasetItemDatasetsRole
    r"""The role of the prompt message"""
    content: CreateDatasetItemDatasetsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[CreateDatasetItemDatasetsToolCallsTypedDict]]


class CreateDatasetItemDatasetsMessages(BaseModel):
    role: CreateDatasetItemDatasetsRole
    r"""The role of the prompt message"""

    content: CreateDatasetItemDatasetsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[CreateDatasetItemDatasetsToolCalls]] = None


class CreateDatasetItemResponseBodyTypedDict(TypedDict):
    r"""Datapoint created successfully. Returns the newly created datapoint object."""

    id: str
    r"""The unique identifier of the dataset item"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    dataset_id: str
    r"""The unique identifier of the dataset"""
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[CreateDatasetItemDatasetsMessagesTypedDict]]
    r"""The prompt template messages"""
    expected_output: NotRequired[str]
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the dataset"""
    updated_by_id: NotRequired[str]
    r"""The unique identifier of the user who last updated the dataset"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class CreateDatasetItemResponseBody(BaseModel):
    r"""Datapoint created successfully. Returns the newly created datapoint object."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset item"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    dataset_id: str
    r"""The unique identifier of the dataset"""

    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[CreateDatasetItemDatasetsMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-13T18:09:35.546Z")
    r"""The date and time the resource was last updated"""
