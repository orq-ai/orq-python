"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateDatasetRequestBodyTypedDict(TypedDict):
    display_name: NotRequired[str]
    r"""The display name of the dataset"""
    project_id: NotRequired[str]
    r"""The unique identifier of the project it belongs to"""
    path: NotRequired[str]
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""


class UpdateDatasetRequestBody(BaseModel):
    display_name: Optional[str] = None
    r"""The display name of the dataset"""

    project_id: Optional[str] = None
    r"""The unique identifier of the project it belongs to"""

    path: Optional[str] = None
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""


class UpdateDatasetRequestTypedDict(TypedDict):
    dataset_id: str
    request_body: NotRequired[UpdateDatasetRequestBodyTypedDict]


class UpdateDatasetRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Optional[UpdateDatasetRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class UpdateDatasetMetadataTypedDict(TypedDict):
    total_versions: float
    datapoints_count: float


class UpdateDatasetMetadata(BaseModel):
    total_versions: float

    datapoints_count: float


class UpdateDatasetResponseBodyTypedDict(TypedDict):
    r"""Dataset updated."""

    id: str
    r"""The unique identifier of the dataset"""
    display_name: str
    r"""The display name of the dataset"""
    project_id: str
    r"""The unique identifier of the project it belongs to"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    metadata: UpdateDatasetMetadataTypedDict
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the dataset"""
    updated_by_id: NotRequired[str]
    r"""The unique identifier of the user who last updated the dataset"""
    parent_id: NotRequired[str]
    r"""The unique identifier for the parent of the committed version"""
    version: NotRequired[str]
    r"""The version of the dataset"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class UpdateDatasetResponseBody(BaseModel):
    r"""Dataset updated."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset"""

    display_name: str
    r"""The display name of the dataset"""

    project_id: str
    r"""The unique identifier of the project it belongs to"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    metadata: UpdateDatasetMetadata

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    parent_id: Optional[str] = None
    r"""The unique identifier for the parent of the committed version"""

    version: Optional[str] = None
    r"""The version of the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-04-13T09:16:27.047Z")
    r"""The date and time the resource was last updated"""
