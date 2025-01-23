"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class FileDeleteRequestTypedDict(TypedDict):
    file_id: str
    r"""The ID of the file"""


class FileDeleteRequest(BaseModel):
    file_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the file"""
