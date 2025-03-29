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
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateChunkMetadataTypedDict(TypedDict):
    r"""Metadata of the chunk"""

    page_number: NotRequired[float]
    r"""In case you are using PDFs, Word, PowerPoint, etc. this is the page number of the chunk."""


class CreateChunkMetadata(BaseModel):
    r"""Metadata of the chunk"""

    page_number: Optional[float] = None
    r"""In case you are using PDFs, Word, PowerPoint, etc. this is the page number of the chunk."""


class RequestBodyTypedDict(TypedDict):
    text: str
    r"""The text content of the chunk"""
    embedding: NotRequired[List[float]]
    r"""The embedding vector of the chunk. If not provided the chunk will be embedded with the knowledge base embeddings model."""
    metadata: NotRequired[CreateChunkMetadataTypedDict]
    r"""Metadata of the chunk"""


class RequestBody(BaseModel):
    text: str
    r"""The text content of the chunk"""

    embedding: Optional[List[float]] = None
    r"""The embedding vector of the chunk. If not provided the chunk will be embedded with the knowledge base embeddings model."""

    metadata: Optional[CreateChunkMetadata] = None
    r"""Metadata of the chunk"""


class CreateChunkRequestTypedDict(TypedDict):
    knowledge_id: str
    r"""Unique identifier of the knowledge"""
    datasource_id: str
    r"""Unique identifier of the datasource"""
    request_body: NotRequired[List[RequestBodyTypedDict]]


class CreateChunkRequest(BaseModel):
    knowledge_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the knowledge"""

    datasource_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the datasource"""

    request_body: Annotated[
        Optional[List[RequestBody]],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class CreateChunkKnowledgeMetadataTypedDict(TypedDict):
    filename: NotRequired[str]
    r"""Filename"""
    last_modified: NotRequired[str]
    r"""Last modified date in ISO 8601 format"""
    filetype: NotRequired[str]
    r"""File type"""
    languages: NotRequired[List[str]]
    r"""Document Languages. List is ordered by probability of being the primary language of the text."""
    page_number: NotRequired[Nullable[float]]
    r"""Page number. Optional field."""
    words_count: NotRequired[float]
    r"""Number of words in the text"""
    sentences_count: NotRequired[float]
    r"""Number of sentences in the text"""
    paragraphs_count: NotRequired[float]
    r"""Number of paragraphs in the text"""
    tokens_count: NotRequired[float]
    r"""Number of tokens in the text"""
    characters_count: NotRequired[float]
    r"""Number of characters in the text"""
    chunks_count: NotRequired[float]
    r"""Number of total chunks"""


class CreateChunkKnowledgeMetadata(BaseModel):
    filename: Optional[str] = None
    r"""Filename"""

    last_modified: Optional[str] = None
    r"""Last modified date in ISO 8601 format"""

    filetype: Optional[str] = None
    r"""File type"""

    languages: Optional[List[str]] = None
    r"""Document Languages. List is ordered by probability of being the primary language of the text."""

    page_number: OptionalNullable[float] = UNSET
    r"""Page number. Optional field."""

    words_count: Optional[float] = None
    r"""Number of words in the text"""

    sentences_count: Optional[float] = None
    r"""Number of sentences in the text"""

    paragraphs_count: Optional[float] = None
    r"""Number of paragraphs in the text"""

    tokens_count: Optional[float] = None
    r"""Number of tokens in the text"""

    characters_count: Optional[float] = None
    r"""Number of characters in the text"""

    chunks_count: Optional[float] = None
    r"""Number of total chunks"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "filename",
            "last_modified",
            "filetype",
            "languages",
            "page_number",
            "words_count",
            "sentences_count",
            "paragraphs_count",
            "tokens_count",
            "characters_count",
            "chunks_count",
        ]
        nullable_fields = ["page_number"]
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


class ErrorsTypedDict(TypedDict):
    code: float
    message: str


class Errors(BaseModel):
    code: float

    message: str


class ProcessingAttemptsTypedDict(TypedDict):
    id: str
    started_at: str
    queued_at: NotRequired[str]
    completed_at: NotRequired[str]
    errors: NotRequired[List[ErrorsTypedDict]]


class ProcessingAttempts(BaseModel):
    id: str

    started_at: str

    queued_at: Optional[str] = None

    completed_at: Optional[str] = None

    errors: Optional[List[Errors]] = None


class CreateChunkResponseBodyTypedDict(TypedDict):
    knowledge_id: str
    r"""The id of the resource"""
    workspace_id: str
    r"""The id of the resource"""
    data_source_id: str
    r"""The id of the resource"""
    text: str
    r"""Text content of the element"""
    processing_attempts: List[ProcessingAttemptsTypedDict]
    created: str
    r"""The date and time the chunk was created"""
    updated: str
    r"""The date and time the chunk was updated"""
    created_by_id: str
    r"""The unique identifier of the user who created the chunk"""
    updated_by_id: str
    r"""The unique identifier of the user who updated the chunk"""
    id: NotRequired[str]
    r"""Unique identifier for the element"""
    enabled: NotRequired[bool]
    metadata: NotRequired[CreateChunkKnowledgeMetadataTypedDict]


class CreateChunkResponseBody(BaseModel):
    knowledge_id: str
    r"""The id of the resource"""

    workspace_id: str
    r"""The id of the resource"""

    data_source_id: str
    r"""The id of the resource"""

    text: str
    r"""Text content of the element"""

    processing_attempts: List[ProcessingAttempts]

    created: str
    r"""The date and time the chunk was created"""

    updated: str
    r"""The date and time the chunk was updated"""

    created_by_id: str
    r"""The unique identifier of the user who created the chunk"""

    updated_by_id: str
    r"""The unique identifier of the user who updated the chunk"""

    id: Optional[str] = "chunk_01JQHH0YGJR4J0WCEYH8TSWS56"
    r"""Unique identifier for the element"""

    enabled: Optional[bool] = True

    metadata: Optional[CreateChunkKnowledgeMetadata] = None
