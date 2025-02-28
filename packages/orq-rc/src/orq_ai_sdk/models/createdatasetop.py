"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
from orq_ai_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateDatasetRequestBodyTypedDict(TypedDict):
    display_name: str
    r"""The display name of the dataset"""
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""


class CreateDatasetRequestBody(BaseModel):
    display_name: str
    r"""The display name of the dataset"""

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""


class CreateDatasetMetadataTypedDict(TypedDict):
    total_versions: float
    datapoints_count: float


class CreateDatasetMetadata(BaseModel):
    total_versions: float

    datapoints_count: float


class CreateDatasetResponseBodyTypedDict(TypedDict):
    r"""Dataset created successfully. Returns the newly created dataset object."""

    id: str
    r"""The unique identifier of the dataset"""
    display_name: str
    r"""The display name of the dataset"""
    project_id: str
    r"""The unique identifier of the project it belongs to"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    metadata: CreateDatasetMetadataTypedDict
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the dataset"""
    updated_by_id: NotRequired[str]
    r"""The unique identifier of the user who last updated the dataset"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class CreateDatasetResponseBody(BaseModel):
    r"""Dataset created successfully. Returns the newly created dataset object."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset"""

    display_name: str
    r"""The display name of the dataset"""

    project_id: str
    r"""The unique identifier of the project it belongs to"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    metadata: CreateDatasetMetadata

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-02-28T12:58:53.029Z")
    r"""The date and time the resource was last updated"""
