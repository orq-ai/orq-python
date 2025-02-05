"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FileListGlobalsTypedDict(TypedDict):
    contact_id: NotRequired[str]


class FileListGlobals(BaseModel):
    contact_id: Annotated[
        Optional[str],
        pydantic.Field(alias="contactId"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None


class FileListRequestTypedDict(TypedDict):
    page: NotRequired[float]
    limit: NotRequired[float]
    last_id: NotRequired[Nullable[str]]
    first_id: NotRequired[Nullable[str]]


class FileListRequest(BaseModel):
    page: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50

    last_id: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="lastId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    first_id: Annotated[
        OptionalNullable[str],
        pydantic.Field(alias="firstId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["page", "limit", "lastId", "firstId"]
        nullable_fields = ["lastId", "firstId"]
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

    created: Optional[datetime] = dateutil.parser.isoparse("2025-02-05T11:00:11.228Z")
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
