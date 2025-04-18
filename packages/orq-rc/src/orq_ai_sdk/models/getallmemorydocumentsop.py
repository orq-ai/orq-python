"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Dict, List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAllMemoryDocumentsRequestTypedDict(TypedDict):
    memory_store_key: str
    r"""The unique key identifier of the memory store"""
    memory_id: str
    r"""The unique identifier of the memory"""
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


class GetAllMemoryDocumentsRequest(BaseModel):
    memory_store_key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique key identifier of the memory store"""

    memory_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the memory"""

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


GetAllMemoryDocumentsObject = Literal["list"]


class GetAllMemoryDocumentsDataTypedDict(TypedDict):
    id: str
    memory_id: str
    store_id: str
    text: str
    created: str
    updated: str
    workspace_id: str
    created_by_id: NotRequired[str]
    updated_by_id: NotRequired[str]
    tags: NotRequired[Dict[str, str]]


class GetAllMemoryDocumentsData(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    memory_id: str

    store_id: str

    text: str

    created: str

    updated: str

    workspace_id: str

    created_by_id: Optional[str] = None

    updated_by_id: Optional[str] = None

    tags: Optional[Dict[str, str]] = None


class GetAllMemoryDocumentsResponseBodyTypedDict(TypedDict):
    r"""Successfully retrieved the list of memory documents."""

    object: GetAllMemoryDocumentsObject
    data: List[GetAllMemoryDocumentsDataTypedDict]
    has_more: bool


class GetAllMemoryDocumentsResponseBody(BaseModel):
    r"""Successfully retrieved the list of memory documents."""

    object: GetAllMemoryDocumentsObject

    data: List[GetAllMemoryDocumentsData]

    has_more: bool
