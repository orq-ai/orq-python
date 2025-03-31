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
from typing import Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CreateDatasourceChunkingConfigurationType = Literal["advanced"]


class ChunkingConfiguration2TypedDict(TypedDict):
    r"""Provides advanced settings for customizing chunking behavior, enabling fine-grained control to better meet specific data processing needs."""

    type: CreateDatasourceChunkingConfigurationType
    chunk_max_characters: NotRequired[float]
    r"""Defines the absolute maximum character length per chunk. Text elements exceeding this size will be automatically split into multiple chunks."""
    chunk_overlap: NotRequired[float]
    r"""Specifies the number of characters to overlap between consecutive chunks. This overlap helps maintain semantic continuity when splitting large text elements."""


class ChunkingConfiguration2(BaseModel):
    r"""Provides advanced settings for customizing chunking behavior, enabling fine-grained control to better meet specific data processing needs."""

    type: CreateDatasourceChunkingConfigurationType

    chunk_max_characters: Optional[float] = 500
    r"""Defines the absolute maximum character length per chunk. Text elements exceeding this size will be automatically split into multiple chunks."""

    chunk_overlap: Optional[float] = 0
    r"""Specifies the number of characters to overlap between consecutive chunks. This overlap helps maintain semantic continuity when splitting large text elements."""


ChunkingConfigurationType = Literal["default"]


class ChunkingConfiguration1TypedDict(TypedDict):
    r"""Optimized chunking strategy focusing on speed and avoiding duplication of content chunks."""

    type: ChunkingConfigurationType


class ChunkingConfiguration1(BaseModel):
    r"""Optimized chunking strategy focusing on speed and avoiding duplication of content chunks."""

    type: ChunkingConfigurationType


ChunkingConfigurationTypedDict = TypeAliasType(
    "ChunkingConfigurationTypedDict",
    Union[ChunkingConfiguration1TypedDict, ChunkingConfiguration2TypedDict],
)
r"""The chunking configuration settings for the datasource. Defaults to the system's standard chunking configuration if not specified."""


ChunkingConfiguration = TypeAliasType(
    "ChunkingConfiguration", Union[ChunkingConfiguration1, ChunkingConfiguration2]
)
r"""The chunking configuration settings for the datasource. Defaults to the system's standard chunking configuration if not specified."""


class ChunkingCleanupOptionsTypedDict(TypedDict):
    r"""The cleanup options applied to the datasource content. All options are enabled by default to ensure enhanced security and optimal chunk quality. Defaults to system-standard cleanup options if not specified."""

    delete_emails: NotRequired[bool]
    r"""Removes email addresses from the provided text."""
    delete_credit_cards: NotRequired[bool]
    r"""Removes credit card numbers from the provided text."""
    delete_phone_numbers: NotRequired[bool]
    r"""Removes phone numbers from the provided text."""
    clean_bullet_points: NotRequired[bool]
    r"""Removes bullet points formatting from the text."""
    clean_numbered_list: NotRequired[bool]
    r"""Removes numbered list formatting from the text."""
    clean_unicode: NotRequired[bool]
    r"""Normalizes or removes unnecessary unicode characters from the text."""
    clean_dashes: NotRequired[bool]
    r"""Normalizes or removes various dash characters to standardize the text."""
    clean_whitespaces: NotRequired[bool]
    r"""Trims and normalizes excessive whitespace throughout the text."""


class ChunkingCleanupOptions(BaseModel):
    r"""The cleanup options applied to the datasource content. All options are enabled by default to ensure enhanced security and optimal chunk quality. Defaults to system-standard cleanup options if not specified."""

    delete_emails: Optional[bool] = None
    r"""Removes email addresses from the provided text."""

    delete_credit_cards: Optional[bool] = None
    r"""Removes credit card numbers from the provided text."""

    delete_phone_numbers: Optional[bool] = None
    r"""Removes phone numbers from the provided text."""

    clean_bullet_points: Optional[bool] = None
    r"""Removes bullet points formatting from the text."""

    clean_numbered_list: Optional[bool] = None
    r"""Removes numbered list formatting from the text."""

    clean_unicode: Optional[bool] = None
    r"""Normalizes or removes unnecessary unicode characters from the text."""

    clean_dashes: Optional[bool] = None
    r"""Normalizes or removes various dash characters to standardize the text."""

    clean_whitespaces: Optional[bool] = None
    r"""Trims and normalizes excessive whitespace throughout the text."""


class ChunkingOptionsTypedDict(TypedDict):
    r"""Configuration options specifying how the datasource file is chunked. Required if `file_id` is specified. Defaults to standard chunking options if omitted."""

    chunking_configuration: NotRequired[ChunkingConfigurationTypedDict]
    r"""The chunking configuration settings for the datasource. Defaults to the system's standard chunking configuration if not specified."""
    chunking_cleanup_options: NotRequired[ChunkingCleanupOptionsTypedDict]
    r"""The cleanup options applied to the datasource content. All options are enabled by default to ensure enhanced security and optimal chunk quality. Defaults to system-standard cleanup options if not specified."""


class ChunkingOptions(BaseModel):
    r"""Configuration options specifying how the datasource file is chunked. Required if `file_id` is specified. Defaults to standard chunking options if omitted."""

    chunking_configuration: Optional[ChunkingConfiguration] = None
    r"""The chunking configuration settings for the datasource. Defaults to the system's standard chunking configuration if not specified."""

    chunking_cleanup_options: Optional[ChunkingCleanupOptions] = None
    r"""The cleanup options applied to the datasource content. All options are enabled by default to ensure enhanced security and optimal chunk quality. Defaults to system-standard cleanup options if not specified."""


class CreateDatasourceRequestBodyTypedDict(TypedDict):
    display_name: NotRequired[str]
    r"""The display name for the datasource visible in the UI. If omitted, the display name is derived from the uploaded file. When both `display_name` and `file_id` are provided, the provided `display_name` is prioritized."""
    file_id: NotRequired[str]
    r"""The unique identifier of the file used for datasource creation. If provided, the file is immediately queued for chunking."""
    chunking_options: NotRequired[ChunkingOptionsTypedDict]
    r"""Configuration options specifying how the datasource file is chunked. Required if `file_id` is specified. Defaults to standard chunking options if omitted."""


class CreateDatasourceRequestBody(BaseModel):
    display_name: Optional[str] = None
    r"""The display name for the datasource visible in the UI. If omitted, the display name is derived from the uploaded file. When both `display_name` and `file_id` are provided, the provided `display_name` is prioritized."""

    file_id: Optional[str] = None
    r"""The unique identifier of the file used for datasource creation. If provided, the file is immediately queued for chunking."""

    chunking_options: Optional[ChunkingOptions] = None
    r"""Configuration options specifying how the datasource file is chunked. Required if `file_id` is specified. Defaults to standard chunking options if omitted."""


class CreateDatasourceRequestTypedDict(TypedDict):
    knowledge_id: str
    r"""The unique identifier of the knowledge base"""
    request_body: CreateDatasourceRequestBodyTypedDict


class CreateDatasourceRequest(BaseModel):
    knowledge_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the knowledge base"""

    request_body: Annotated[
        CreateDatasourceRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


CreateDatasourceStatus = Literal[
    "pending", "processing", "completed", "failed", "queued"
]


class CreateDatasourceResponseBodyTypedDict(TypedDict):
    r"""Datasource successfully created"""

    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""
    status: CreateDatasourceStatus
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


class CreateDatasourceResponseBody(BaseModel):
    r"""Datasource successfully created"""

    display_name: str
    r"""The display name of the datasource. Normally the name of the uploaded file"""

    status: CreateDatasourceStatus

    created: str
    r"""The date and time the datasource was created"""

    updated: str
    r"""The date and time the datasource was updated"""

    knowledge_id: str
    r"""The unique identifier of the knowledge base"""

    chunks_count: float
    r"""The number of chunks in the datasource"""

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "01JQNQ1F7A1AVCYMKC0B8ZNB25"
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
