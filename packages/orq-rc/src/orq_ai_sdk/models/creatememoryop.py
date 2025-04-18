"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateMemoryRequestBodyTypedDict(TypedDict):
    entity_id: str
    tags: Dict[str, str]


class CreateMemoryRequestBody(BaseModel):
    entity_id: str

    tags: Dict[str, str]


class CreateMemoryRequestTypedDict(TypedDict):
    memory_store_key: str
    r"""The unique key identifier of the memory store"""
    request_body: NotRequired[CreateMemoryRequestBodyTypedDict]


class CreateMemoryRequest(BaseModel):
    memory_store_key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique key identifier of the memory store"""

    request_body: Annotated[
        Optional[CreateMemoryRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateMemoryResponseBodyTypedDict(TypedDict):
    r"""Memory successfully created."""

    id: str
    entity_id: str
    created: str
    updated: str
    store_id: str
    tags: Dict[str, str]
    workspace_id: str
    created_by_id: NotRequired[Nullable[str]]
    updated_by_id: NotRequired[Nullable[str]]


class CreateMemoryResponseBody(BaseModel):
    r"""Memory successfully created."""

    id: Annotated[str, pydantic.Field(alias="_id")]

    entity_id: str

    created: str

    updated: str

    store_id: str

    tags: Dict[str, str]

    workspace_id: str

    created_by_id: OptionalNullable[str] = UNSET

    updated_by_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_by_id", "updated_by_id"]
        nullable_fields = ["created_by_id", "updated_by_id"]
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
