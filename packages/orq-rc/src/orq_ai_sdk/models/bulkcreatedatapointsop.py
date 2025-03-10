"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


BulkCreateDatapointsRole = Literal[
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

BulkCreateDatapoints2DatasetsType = Literal["image_url"]


class BulkCreateDatapoints2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class BulkCreateDatapoints2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class BulkCreateDatapoints22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: BulkCreateDatapoints2DatasetsType
    image_url: BulkCreateDatapoints2ImageURLTypedDict


class BulkCreateDatapoints22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: BulkCreateDatapoints2DatasetsType

    image_url: BulkCreateDatapoints2ImageURL


BulkCreateDatapoints2Type = Literal["text"]


class BulkCreateDatapoints21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: BulkCreateDatapoints2Type
    text: str


class BulkCreateDatapoints21(BaseModel):
    r"""Text content part of a prompt message"""

    type: BulkCreateDatapoints2Type

    text: str


BulkCreateDatapointsContent2TypedDict = TypeAliasType(
    "BulkCreateDatapointsContent2TypedDict",
    Union[BulkCreateDatapoints21TypedDict, BulkCreateDatapoints22TypedDict],
)


BulkCreateDatapointsContent2 = TypeAliasType(
    "BulkCreateDatapointsContent2",
    Union[BulkCreateDatapoints21, BulkCreateDatapoints22],
)


BulkCreateDatapointsContentTypedDict = TypeAliasType(
    "BulkCreateDatapointsContentTypedDict",
    Union[str, List[BulkCreateDatapointsContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


BulkCreateDatapointsContent = TypeAliasType(
    "BulkCreateDatapointsContent", Union[str, List[BulkCreateDatapointsContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


BulkCreateDatapointsType = Literal["function"]


class BulkCreateDatapointsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class BulkCreateDatapointsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class BulkCreateDatapointsToolCallsTypedDict(TypedDict):
    type: BulkCreateDatapointsType
    function: BulkCreateDatapointsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class BulkCreateDatapointsToolCalls(BaseModel):
    type: BulkCreateDatapointsType

    function: BulkCreateDatapointsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class BulkCreateDatapointsMessagesTypedDict(TypedDict):
    role: BulkCreateDatapointsRole
    r"""The role of the prompt message"""
    content: BulkCreateDatapointsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[BulkCreateDatapointsToolCallsTypedDict]]


class BulkCreateDatapointsMessages(BaseModel):
    role: BulkCreateDatapointsRole
    r"""The role of the prompt message"""

    content: BulkCreateDatapointsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[BulkCreateDatapointsToolCalls]] = None


class ItemsTypedDict(TypedDict):
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[BulkCreateDatapointsMessagesTypedDict]]
    r"""The prompt template messages"""
    expected_output: NotRequired[str]


class Items(BaseModel):
    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[BulkCreateDatapointsMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None


class BulkCreateDatapointsRequestBodyTypedDict(TypedDict):
    items: List[ItemsTypedDict]


class BulkCreateDatapointsRequestBody(BaseModel):
    items: List[Items]


class BulkCreateDatapointsRequestTypedDict(TypedDict):
    dataset_id: str
    request_body: NotRequired[BulkCreateDatapointsRequestBodyTypedDict]


class BulkCreateDatapointsRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[BulkCreateDatapointsRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


BulkCreateDatapointsDatasetsRole = Literal[
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

BulkCreateDatapoints2DatasetsResponse200Type = Literal["image_url"]


class BulkCreateDatapoints2DatasetsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class BulkCreateDatapoints2DatasetsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class BulkCreateDatapoints2Datasets2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: BulkCreateDatapoints2DatasetsResponse200Type
    image_url: BulkCreateDatapoints2DatasetsImageURLTypedDict


class BulkCreateDatapoints2Datasets2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: BulkCreateDatapoints2DatasetsResponse200Type

    image_url: BulkCreateDatapoints2DatasetsImageURL


BulkCreateDatapoints2DatasetsResponseType = Literal["text"]


class BulkCreateDatapoints2Datasets1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: BulkCreateDatapoints2DatasetsResponseType
    text: str


class BulkCreateDatapoints2Datasets1(BaseModel):
    r"""Text content part of a prompt message"""

    type: BulkCreateDatapoints2DatasetsResponseType

    text: str


BulkCreateDatapointsContentDatasets2TypedDict = TypeAliasType(
    "BulkCreateDatapointsContentDatasets2TypedDict",
    Union[
        BulkCreateDatapoints2Datasets1TypedDict, BulkCreateDatapoints2Datasets2TypedDict
    ],
)


BulkCreateDatapointsContentDatasets2 = TypeAliasType(
    "BulkCreateDatapointsContentDatasets2",
    Union[BulkCreateDatapoints2Datasets1, BulkCreateDatapoints2Datasets2],
)


BulkCreateDatapointsDatasetsContentTypedDict = TypeAliasType(
    "BulkCreateDatapointsDatasetsContentTypedDict",
    Union[str, List[BulkCreateDatapointsContentDatasets2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


BulkCreateDatapointsDatasetsContent = TypeAliasType(
    "BulkCreateDatapointsDatasetsContent",
    Union[str, List[BulkCreateDatapointsContentDatasets2]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


BulkCreateDatapointsDatasetsType = Literal["function"]


class BulkCreateDatapointsDatasetsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class BulkCreateDatapointsDatasetsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class BulkCreateDatapointsDatasetsToolCallsTypedDict(TypedDict):
    type: BulkCreateDatapointsDatasetsType
    function: BulkCreateDatapointsDatasetsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class BulkCreateDatapointsDatasetsToolCalls(BaseModel):
    type: BulkCreateDatapointsDatasetsType

    function: BulkCreateDatapointsDatasetsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class BulkCreateDatapointsDatasetsMessagesTypedDict(TypedDict):
    role: BulkCreateDatapointsDatasetsRole
    r"""The role of the prompt message"""
    content: BulkCreateDatapointsDatasetsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[BulkCreateDatapointsDatasetsToolCallsTypedDict]]


class BulkCreateDatapointsDatasetsMessages(BaseModel):
    role: BulkCreateDatapointsDatasetsRole
    r"""The role of the prompt message"""

    content: BulkCreateDatapointsDatasetsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[BulkCreateDatapointsDatasetsToolCalls]] = None


class ResponseBodyTypedDict(TypedDict):
    id: str
    r"""The unique identifier of the dataset item"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    dataset_id: str
    r"""The unique identifier of the dataset"""
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[BulkCreateDatapointsDatasetsMessagesTypedDict]]
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


class ResponseBody(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset item"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    dataset_id: str
    r"""The unique identifier of the dataset"""

    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[BulkCreateDatapointsDatasetsMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-10T11:10:33.958Z")
    r"""The date and time the resource was last updated"""
