"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FileListRequestTypedDict(TypedDict):
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


class FileListRequest(BaseModel):
    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""

    starting_after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""

    ending_before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


FileListObject = Literal["list"]

FileListPurpose = Literal["retrieval", "knowledge_datasource"]
r"""The intended purpose of the uploaded file."""


class FileListDataTypedDict(TypedDict):
    id: str
    object_name: str
    r"""path to the file in the storage"""
    purpose: FileListPurpose
    r"""The intended purpose of the uploaded file."""
    bytes_: float
    file_name: str
    workspace_id: str
    r"""The id of the resource"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""


class FileListData(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    object_name: str
    r"""path to the file in the storage"""

    purpose: FileListPurpose
    r"""The intended purpose of the uploaded file."""

    bytes_: Annotated[float, pydantic.Field(alias="bytes")]

    file_name: str

    workspace_id: str
    r"""The id of the resource"""

    created: Optional[datetime] = dateutil.parser.isoparse("2025-02-25T11:29:26.431Z")
    r"""The date and time the resource was created"""


class FileListResponseBodyTypedDict(TypedDict):
    r"""Files retrieved successfully"""

    object: FileListObject
    data: List[FileListDataTypedDict]
    has_more: bool


class FileListResponseBody(BaseModel):
    r"""Files retrieved successfully"""

    object: FileListObject

    data: List[FileListData]

    has_more: bool
