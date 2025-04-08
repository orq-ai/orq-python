"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


StatusTypedDict = TypeAliasType("StatusTypedDict", Union[List[str], str])
r"""Filter datasources by status."""


Status = TypeAliasType("Status", Union[List[str], str])
r"""Filter datasources by status."""


class ListDatasourcesRequestTypedDict(TypedDict):
    knowledge_id: str
    r"""Unique identifier of the knowledge base"""
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""
    q: NotRequired[str]
    r"""Search query to find datasources by name."""
    status: NotRequired[StatusTypedDict]
    r"""Filter datasources by status."""


class ListDatasourcesRequest(BaseModel):
    knowledge_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the knowledge base"""

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

    q: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Search query to find datasources by name."""

    status: Annotated[
        Optional[Status],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter datasources by status."""


ListDatasourcesObject = Literal["list"]

ListDatasourcesStatus = Literal[
    "pending", "processing", "completed", "failed", "queued"
]


class ListDatasourcesDataTypedDict(TypedDict):
    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""
    status: ListDatasourcesStatus
    created: str
    r"""The date and time the datasource was created"""
    updated: str
    r"""The date and time the datasource was updated"""
    knowledge_id: str
    r"""The unique identifier of the knowledge base"""
    chunks_count: float
    r"""The number of chunks in the datasource"""
    id: NotRequired[str]
    r"""The id of the resource"""
    description: NotRequired[str]
    r"""The description of the knowledge base"""
    file_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the file used to create the datasource."""
    created_by_id: NotRequired[str]
    r"""The id of the resource"""
    update_by_id: NotRequired[str]
    r"""The id of the resource"""


class ListDatasourcesData(BaseModel):
    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""

    status: ListDatasourcesStatus

    created: str
    r"""The date and time the datasource was created"""

    updated: str
    r"""The date and time the datasource was updated"""

    knowledge_id: str
    r"""The unique identifier of the knowledge base"""

    chunks_count: float
    r"""The number of chunks in the datasource"""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "01JRA4NJP83ZKJQPVT4N99YMNV"
    )
    r"""The id of the resource"""

    description: Optional[str] = None
    r"""The description of the knowledge base"""

    file_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the file used to create the datasource."""

    created_by_id: Optional[str] = None
    r"""The id of the resource"""

    update_by_id: Optional[str] = None
    r"""The id of the resource"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "_id",
            "description",
            "file_id",
            "created_by_id",
            "update_by_id",
        ]
        nullable_fields = ["file_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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


class ListDatasourcesResponseBodyTypedDict(TypedDict):
    r"""Datasources successfully retrieved"""

    object: ListDatasourcesObject
    data: List[ListDatasourcesDataTypedDict]
    has_more: bool


class ListDatasourcesResponseBody(BaseModel):
    r"""Datasources successfully retrieved"""

    object: ListDatasourcesObject

    data: List[ListDatasourcesData]

    has_more: bool
