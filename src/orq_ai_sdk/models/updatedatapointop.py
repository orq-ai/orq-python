"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


UpdateDatapointRole = Literal[
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

UpdateDatapoint2DatasetsType = Literal["image_url"]


class UpdateDatapoint2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class UpdateDatapoint2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class UpdateDatapoint22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: UpdateDatapoint2DatasetsType
    image_url: UpdateDatapoint2ImageURLTypedDict


class UpdateDatapoint22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: UpdateDatapoint2DatasetsType

    image_url: UpdateDatapoint2ImageURL


UpdateDatapoint2Type = Literal["text"]


class UpdateDatapoint21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: UpdateDatapoint2Type
    text: str


class UpdateDatapoint21(BaseModel):
    r"""Text content part of a prompt message"""

    type: UpdateDatapoint2Type

    text: str


UpdateDatapointContent2TypedDict = TypeAliasType(
    "UpdateDatapointContent2TypedDict",
    Union[UpdateDatapoint21TypedDict, UpdateDatapoint22TypedDict],
)


UpdateDatapointContent2 = TypeAliasType(
    "UpdateDatapointContent2", Union[UpdateDatapoint21, UpdateDatapoint22]
)


UpdateDatapointContentTypedDict = TypeAliasType(
    "UpdateDatapointContentTypedDict",
    Union[str, List[UpdateDatapointContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


UpdateDatapointContent = TypeAliasType(
    "UpdateDatapointContent", Union[str, List[UpdateDatapointContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


UpdateDatapointType = Literal["function"]


class UpdateDatapointFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class UpdateDatapointFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class UpdateDatapointToolCallsTypedDict(TypedDict):
    type: UpdateDatapointType
    function: UpdateDatapointFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class UpdateDatapointToolCalls(BaseModel):
    type: UpdateDatapointType

    function: UpdateDatapointFunction

    id: Optional[str] = None

    index: Optional[float] = None


class UpdateDatapointMessagesTypedDict(TypedDict):
    role: UpdateDatapointRole
    r"""The role of the prompt message"""
    content: UpdateDatapointContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[UpdateDatapointToolCallsTypedDict]]


class UpdateDatapointMessages(BaseModel):
    role: UpdateDatapointRole
    r"""The role of the prompt message"""

    content: UpdateDatapointContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[UpdateDatapointToolCalls]] = None


class UpdateDatapointRequestBodyTypedDict(TypedDict):
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[UpdateDatapointMessagesTypedDict]]
    r"""The prompt template messages"""
    expected_output: NotRequired[str]


class UpdateDatapointRequestBody(BaseModel):
    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[UpdateDatapointMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None


class UpdateDatapointRequestTypedDict(TypedDict):
    dataset_id: str
    datapoint_id: str
    request_body: NotRequired[UpdateDatapointRequestBodyTypedDict]


class UpdateDatapointRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    datapoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[UpdateDatapointRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


UpdateDatapointDatasetsRole = Literal[
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

UpdateDatapoint2DatasetsResponse200Type = Literal["image_url"]


class UpdateDatapoint2DatasetsImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class UpdateDatapoint2DatasetsImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class UpdateDatapoint2Datasets2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: UpdateDatapoint2DatasetsResponse200Type
    image_url: UpdateDatapoint2DatasetsImageURLTypedDict


class UpdateDatapoint2Datasets2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: UpdateDatapoint2DatasetsResponse200Type

    image_url: UpdateDatapoint2DatasetsImageURL


UpdateDatapoint2DatasetsResponseType = Literal["text"]


class UpdateDatapoint2Datasets1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: UpdateDatapoint2DatasetsResponseType
    text: str


class UpdateDatapoint2Datasets1(BaseModel):
    r"""Text content part of a prompt message"""

    type: UpdateDatapoint2DatasetsResponseType

    text: str


UpdateDatapointContentDatasets2TypedDict = TypeAliasType(
    "UpdateDatapointContentDatasets2TypedDict",
    Union[UpdateDatapoint2Datasets1TypedDict, UpdateDatapoint2Datasets2TypedDict],
)


UpdateDatapointContentDatasets2 = TypeAliasType(
    "UpdateDatapointContentDatasets2",
    Union[UpdateDatapoint2Datasets1, UpdateDatapoint2Datasets2],
)


UpdateDatapointDatasetsContentTypedDict = TypeAliasType(
    "UpdateDatapointDatasetsContentTypedDict",
    Union[str, List[UpdateDatapointContentDatasets2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


UpdateDatapointDatasetsContent = TypeAliasType(
    "UpdateDatapointDatasetsContent", Union[str, List[UpdateDatapointContentDatasets2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


UpdateDatapointDatasetsType = Literal["function"]


class UpdateDatapointDatasetsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class UpdateDatapointDatasetsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class UpdateDatapointDatasetsToolCallsTypedDict(TypedDict):
    type: UpdateDatapointDatasetsType
    function: UpdateDatapointDatasetsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class UpdateDatapointDatasetsToolCalls(BaseModel):
    type: UpdateDatapointDatasetsType

    function: UpdateDatapointDatasetsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class UpdateDatapointDatasetsMessagesTypedDict(TypedDict):
    role: UpdateDatapointDatasetsRole
    r"""The role of the prompt message"""
    content: UpdateDatapointDatasetsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[UpdateDatapointDatasetsToolCallsTypedDict]]


class UpdateDatapointDatasetsMessages(BaseModel):
    role: UpdateDatapointDatasetsRole
    r"""The role of the prompt message"""

    content: UpdateDatapointDatasetsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[UpdateDatapointDatasetsToolCalls]] = None


class UpdateDatapointResponseBodyTypedDict(TypedDict):
    r"""Dataset item updated."""

    id: str
    r"""The unique identifier of the dataset item"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    dataset_id: str
    r"""The unique identifier of the dataset"""
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[UpdateDatapointDatasetsMessagesTypedDict]]
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


class UpdateDatapointResponseBody(BaseModel):
    r"""Dataset item updated."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset item"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    dataset_id: str
    r"""The unique identifier of the dataset"""

    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[UpdateDatapointDatasetsMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-20T14:51:11.226Z")
    r"""The date and time the resource was last updated"""
