"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListDatasetsRequestTypedDict(TypedDict):
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


class ListDatasetsRequest(BaseModel):
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


ListDatasetsObject = Literal["list"]


class ListDatasetsMetadataTypedDict(TypedDict):
    total_versions: float
    datapoints_count: float


class ListDatasetsMetadata(BaseModel):
    total_versions: float

    datapoints_count: float


class ListDatasetsDataTypedDict(TypedDict):
    id: str
    r"""The unique identifier of the dataset"""
    display_name: str
    r"""The display name of the dataset"""
    project_id: str
    r"""The unique identifier of the project it belongs to"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    metadata: ListDatasetsMetadataTypedDict
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the dataset"""
    updated_by_id: NotRequired[str]
    r"""The unique identifier of the user who last updated the dataset"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class ListDatasetsData(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset"""

    display_name: str
    r"""The display name of the dataset"""

    project_id: str
    r"""The unique identifier of the project it belongs to"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    metadata: ListDatasetsMetadata

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-27T14:19:18.505Z")
    r"""The date and time the resource was last updated"""


class ListDatasetsResponseBodyTypedDict(TypedDict):
    r"""Datasets Retrieved Successfully"""

    object: ListDatasetsObject
    data: List[ListDatasetsDataTypedDict]
    has_more: bool


class ListDatasetsResponseBody(BaseModel):
    r"""Datasets Retrieved Successfully"""

    object: ListDatasetsObject

    data: List[ListDatasetsData]

    has_more: bool
