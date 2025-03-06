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
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class CreateContactRequestBodyTypedDict(TypedDict):
    r"""Update user information payload"""

    external_id: str
    r"""Unique string value to identify the contact user in the customer's system"""
    display_name: NotRequired[Nullable[str]]
    r"""Display name or nickname of the user"""
    email: NotRequired[Nullable[str]]
    r"""Email address of the user"""
    avatar_url: NotRequired[Nullable[str]]
    r"""URL linking to the user's avatar image"""
    tags: NotRequired[List[str]]
    r"""Array of UUIDs representing tags associated with the user"""
    metadata: NotRequired[Dict[str, Any]]
    r"""Additional custom metadata associated with the user as key-value pairs"""


class CreateContactRequestBody(BaseModel):
    r"""Update user information payload"""

    external_id: str
    r"""Unique string value to identify the contact user in the customer's system"""

    display_name: OptionalNullable[str] = UNSET
    r"""Display name or nickname of the user"""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the user"""

    avatar_url: OptionalNullable[str] = UNSET
    r"""URL linking to the user's avatar image"""

    tags: Optional[List[str]] = None
    r"""Array of UUIDs representing tags associated with the user"""

    metadata: Optional[Dict[str, Any]] = None
    r"""Additional custom metadata associated with the user as key-value pairs"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["display_name", "email", "avatar_url", "tags", "metadata"]
        nullable_fields = ["display_name", "email", "avatar_url"]
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


class CreateContactResponseBodyTypedDict(TypedDict):
    r"""Successful operation"""

    id: str
    r"""Unique ULID (Universally Unique Lexicographically Sortable Identifier) for the user"""
    external_id: str
    r"""Unique string value to identify the contact user in the customer's system"""
    display_name: NotRequired[Nullable[str]]
    r"""Display name or nickname of the user"""
    email: NotRequired[Nullable[str]]
    r"""Email address of the user"""
    avatar_url: NotRequired[Nullable[str]]
    r"""URL linking to the user's avatar image"""
    tags: NotRequired[List[str]]
    r"""Array of UUIDs representing tags associated with the user"""
    metadata: NotRequired[Dict[str, Any]]
    r"""Additional custom metadata associated with the user as key-value pairs"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class CreateContactResponseBody(BaseModel):
    r"""Successful operation"""

    id: str
    r"""Unique ULID (Universally Unique Lexicographically Sortable Identifier) for the user"""

    external_id: str
    r"""Unique string value to identify the contact user in the customer's system"""

    display_name: OptionalNullable[str] = UNSET
    r"""Display name or nickname of the user"""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the user"""

    avatar_url: OptionalNullable[str] = UNSET
    r"""URL linking to the user's avatar image"""

    tags: Optional[List[str]] = None
    r"""Array of UUIDs representing tags associated with the user"""

    metadata: Optional[Dict[str, Any]] = None
    r"""Additional custom metadata associated with the user as key-value pairs"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = dateutil.parser.isoparse("2025-03-06T14:57:05.845Z")
    r"""The date and time the resource was last updated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "display_name",
            "email",
            "avatar_url",
            "tags",
            "metadata",
            "created",
            "updated",
        ]
        nullable_fields = ["display_name", "email", "avatar_url"]
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
