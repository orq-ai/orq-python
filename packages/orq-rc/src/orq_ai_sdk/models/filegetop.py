"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FileGetGlobalsTypedDict(TypedDict):
    contact_id: NotRequired[str]


class FileGetGlobals(BaseModel):
    contact_id: Annotated[
        Optional[str],
        pydantic.Field(alias="contactId"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None


class FileGetRequestTypedDict(TypedDict):
    file_id: str
    r"""The ID of the file"""


class FileGetRequest(BaseModel):
    file_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the file"""


FileGetPurpose = Literal["retrieval", "knowledge_datasource"]
r"""The intended purpose of the uploaded file."""


class FileGetResponseBodyTypedDict(TypedDict):
    r"""File details retrieved successfully"""

    id: str
    object_name: str
    r"""path to the file in the storage"""
    purpose: FileGetPurpose
    r"""The intended purpose of the uploaded file."""
    bytes_: float
    file_name: str
    workspace_id: str
    r"""The id of the resource"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""


class FileGetResponseBody(BaseModel):
    r"""File details retrieved successfully"""

    id: Annotated[str, pydantic.Field(alias="_id")]

    object_name: str
    r"""path to the file in the storage"""

    purpose: FileGetPurpose
    r"""The intended purpose of the uploaded file."""

    bytes_: Annotated[float, pydantic.Field(alias="bytes")]

    file_name: str

    workspace_id: str
    r"""The id of the resource"""

    created: Optional[datetime] = dateutil.parser.isoparse("2025-02-02T16:01:08.536Z")
    r"""The date and time the resource was created"""
