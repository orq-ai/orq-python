"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RetrieveDatasourceRequestTypedDict(TypedDict):
    knowledge_id: str
    r"""The unique identifier of the knowledge base"""
    datasource_id: str
    r"""The unique identifier of the datasource."""


class RetrieveDatasourceRequest(BaseModel):
    knowledge_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the knowledge base"""

    datasource_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the datasource."""


RetrieveDatasourceStatus = Literal[
    "pending", "processing", "completed", "failed", "queued"
]


class RetrieveDatasourceResponseBodyTypedDict(TypedDict):
    r"""Datasource successfully retrieved"""

    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""
    status: RetrieveDatasourceStatus
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


class RetrieveDatasourceResponseBody(BaseModel):
    r"""Datasource successfully retrieved"""

    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""

    status: RetrieveDatasourceStatus

    created: str
    r"""The date and time the datasource was created"""

    updated: str
    r"""The date and time the datasource was updated"""

    knowledge_id: str
    r"""The unique identifier of the knowledge base"""

    chunks_count: float
    r"""The number of chunks in the datasource"""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "01JQYPMWQHFA1YG3BADX3Q9RCX"
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
