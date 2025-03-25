"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class RetrieveDatapointRequestTypedDict(TypedDict):
    dataset_id: str
    datapoint_id: str


class RetrieveDatapointRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    datapoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


RetrieveDatapointRole = Literal[
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

RetrieveDatapoint2DatasetsType = Literal["image_url"]


class RetrieveDatapoint2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class RetrieveDatapoint2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class RetrieveDatapoint22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: RetrieveDatapoint2DatasetsType
    image_url: RetrieveDatapoint2ImageURLTypedDict


class RetrieveDatapoint22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: RetrieveDatapoint2DatasetsType

    image_url: RetrieveDatapoint2ImageURL


RetrieveDatapoint2Type = Literal["text"]


class RetrieveDatapoint21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: RetrieveDatapoint2Type
    text: str


class RetrieveDatapoint21(BaseModel):
    r"""Text content part of a prompt message"""

    type: RetrieveDatapoint2Type

    text: str


RetrieveDatapointContent2TypedDict = TypeAliasType(
    "RetrieveDatapointContent2TypedDict",
    Union[RetrieveDatapoint21TypedDict, RetrieveDatapoint22TypedDict],
)


RetrieveDatapointContent2 = TypeAliasType(
    "RetrieveDatapointContent2", Union[RetrieveDatapoint21, RetrieveDatapoint22]
)


RetrieveDatapointContentTypedDict = TypeAliasType(
    "RetrieveDatapointContentTypedDict",
    Union[str, List[RetrieveDatapointContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


RetrieveDatapointContent = TypeAliasType(
    "RetrieveDatapointContent", Union[str, List[RetrieveDatapointContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


RetrieveDatapointType = Literal["function"]


class RetrieveDatapointFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class RetrieveDatapointFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class RetrieveDatapointToolCallsTypedDict(TypedDict):
    type: RetrieveDatapointType
    function: RetrieveDatapointFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class RetrieveDatapointToolCalls(BaseModel):
    type: RetrieveDatapointType

    function: RetrieveDatapointFunction

    id: Optional[str] = None

    index: Optional[float] = None


class RetrieveDatapointMessagesTypedDict(TypedDict):
    role: RetrieveDatapointRole
    r"""The role of the prompt message"""
    content: RetrieveDatapointContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[RetrieveDatapointToolCallsTypedDict]]


class RetrieveDatapointMessages(BaseModel):
    role: RetrieveDatapointRole
    r"""The role of the prompt message"""

    content: RetrieveDatapointContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[RetrieveDatapointToolCalls]] = None


class RetrieveDatapointResponseBodyTypedDict(TypedDict):
    r"""Datapoint retrieved."""

    id: str
    r"""The unique identifier of the dataset item"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    dataset_id: str
    r"""The unique identifier of the dataset"""
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[RetrieveDatapointMessagesTypedDict]]
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


class RetrieveDatapointResponseBody(BaseModel):
    r"""Datapoint retrieved."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset item"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    dataset_id: str
    r"""The unique identifier of the dataset"""

    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[RetrieveDatapointMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-25T10:52:48.745Z")
    r"""The date and time the resource was last updated"""
