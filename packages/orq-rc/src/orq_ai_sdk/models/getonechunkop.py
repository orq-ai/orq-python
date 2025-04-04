"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Dict, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetOneChunkRequestTypedDict(TypedDict):
    chunk_id: str
    r"""The unique identifier of the chunk"""
    datasource_id: str
    r"""The unique identifier of the data source"""
    knowledge_id: str
    r"""The unique identifier of the knowledge base"""


class GetOneChunkRequest(BaseModel):
    chunk_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the chunk"""

    datasource_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the data source"""

    knowledge_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the knowledge base"""


GetOneChunkStatus = Literal["pending", "processing", "completed", "failed", "queued"]
r"""The status of the chunk"""


class GetOneChunkResponseBodyTypedDict(TypedDict):
    r"""Chunk successfully retrieved"""

    id: str
    r"""The unique identifier of the chunk"""
    text: str
    r"""The text content of the chunk"""
    enabled: bool
    r"""Whether the chunk is enabled"""
    status: GetOneChunkStatus
    r"""The status of the chunk"""
    created: str
    r"""The date and time the chunk was created"""
    updated: str
    r"""The date and time the chunk was updated"""
    metadata: NotRequired[Dict[str, str]]
    r"""Metadata of the chunk. Can include `page_number` or any other key-value pairs. Only values of type string are supported."""
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the chunk"""
    update_by_id: NotRequired[str]
    r"""The unique identifier of the user who updated the chunk"""


class GetOneChunkResponseBody(BaseModel):
    r"""Chunk successfully retrieved"""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the chunk"""

    text: str
    r"""The text content of the chunk"""

    enabled: bool
    r"""Whether the chunk is enabled"""

    status: GetOneChunkStatus
    r"""The status of the chunk"""

    created: str
    r"""The date and time the chunk was created"""

    updated: str
    r"""The date and time the chunk was updated"""

    metadata: Optional[Dict[str, str]] = None
    r"""Metadata of the chunk. Can include `page_number` or any other key-value pairs. Only values of type string are supported."""

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the chunk"""

    update_by_id: Optional[str] = None
    r"""The unique identifier of the user who updated the chunk"""
