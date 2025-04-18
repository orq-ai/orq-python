"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel
import pydantic
from typing import Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


Seventeen = Literal["jina/jina-embeddings-v3"]

Sixteen = Literal["jina/jina-clip-v2"]

Fifteen = Literal["jina/jina-embeddings-v2-base-de"]

Fourteen = Literal["jina/jina-embeddings-v2-base-code"]

Thirteen = Literal["jina/jina-embeddings-v2-base-zh"]

Twelve = Literal["jina/jina-embeddings-v2-base-en"]

Eleven = Literal["jina/jina-embeddings-v2-base-es"]

Ten = Literal["jina/jina-clip-v1"]

Nine = Literal["google-ai/text-embedding-004"]

Eight = Literal["openai/text-embedding-ada-002"]

Seven = Literal["openai/text-embedding-3-small"]

Six = Literal["openai/text-embedding-3-large"]

Five = Literal["azure/text-embedding-ada-002"]

Four = Literal["cohere/embed-english-v3.0"]

Model3 = Literal["cohere/embed-english-light-v3.0"]

Model2 = Literal["cohere/embed-multilingual-light-v3.0"]

Model1 = Literal["cohere/embed-multilingual-v3.0"]

ModelTypedDict = TypeAliasType(
    "ModelTypedDict",
    Union[
        Model1,
        Model2,
        Model3,
        Four,
        Five,
        Six,
        Seven,
        Eight,
        Nine,
        Ten,
        Eleven,
        Twelve,
        Thirteen,
        Fourteen,
        Fifteen,
        Sixteen,
        Seventeen,
    ],
)


Model = TypeAliasType(
    "Model",
    Union[
        Model1,
        Model2,
        Model3,
        Four,
        Five,
        Six,
        Seven,
        Eight,
        Nine,
        Ten,
        Eleven,
        Twelve,
        Thirteen,
        Fourteen,
        Fifteen,
        Sixteen,
        Seventeen,
    ],
)


class EmbeddingConfigTypedDict(TypedDict):
    model: ModelTypedDict


class EmbeddingConfig(BaseModel):
    model: Model


class CreateMemoryStoreRequestBodyTypedDict(TypedDict):
    key: str
    r"""The unique key of the memory store. The key is unique and inmmutable and cannot be repeated within the same workspace."""
    embedding_config: EmbeddingConfigTypedDict
    description: str
    r"""The description of the memory store. Be as precise as possible to help the AI to understand the purpose of the memory store."""
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    ttl: NotRequired[float]
    r"""The default time to live of every memory document created within the memory store. Useful to control if the documents in the memory should be store for short or long term."""


class CreateMemoryStoreRequestBody(BaseModel):
    key: str
    r"""The unique key of the memory store. The key is unique and inmmutable and cannot be repeated within the same workspace."""

    embedding_config: EmbeddingConfig

    description: str
    r"""The description of the memory store. Be as precise as possible to help the AI to understand the purpose of the memory store."""

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    ttl: Optional[float] = None
    r"""The default time to live of every memory document created within the memory store. Useful to control if the documents in the memory should be store for short or long term."""


CreateMemoryStoreModel17 = Literal["jina/jina-embeddings-v3"]

CreateMemoryStoreModel16 = Literal["jina/jina-clip-v2"]

CreateMemoryStoreModel15 = Literal["jina/jina-embeddings-v2-base-de"]

CreateMemoryStoreModel14 = Literal["jina/jina-embeddings-v2-base-code"]

CreateMemoryStoreModel13 = Literal["jina/jina-embeddings-v2-base-zh"]

CreateMemoryStoreModel12 = Literal["jina/jina-embeddings-v2-base-en"]

CreateMemoryStoreModel11 = Literal["jina/jina-embeddings-v2-base-es"]

CreateMemoryStoreModel10 = Literal["jina/jina-clip-v1"]

CreateMemoryStoreModel9 = Literal["google-ai/text-embedding-004"]

CreateMemoryStoreModel8 = Literal["openai/text-embedding-ada-002"]

CreateMemoryStoreModel7 = Literal["openai/text-embedding-3-small"]

CreateMemoryStoreModel6 = Literal["openai/text-embedding-3-large"]

CreateMemoryStoreModel5 = Literal["azure/text-embedding-ada-002"]

CreateMemoryStoreModel4 = Literal["cohere/embed-english-v3.0"]

CreateMemoryStoreModel3 = Literal["cohere/embed-english-light-v3.0"]

CreateMemoryStoreModel2 = Literal["cohere/embed-multilingual-light-v3.0"]

CreateMemoryStoreModel1 = Literal["cohere/embed-multilingual-v3.0"]

CreateMemoryStoreModelTypedDict = TypeAliasType(
    "CreateMemoryStoreModelTypedDict",
    Union[
        CreateMemoryStoreModel1,
        CreateMemoryStoreModel2,
        CreateMemoryStoreModel3,
        CreateMemoryStoreModel4,
        CreateMemoryStoreModel5,
        CreateMemoryStoreModel6,
        CreateMemoryStoreModel7,
        CreateMemoryStoreModel8,
        CreateMemoryStoreModel9,
        CreateMemoryStoreModel10,
        CreateMemoryStoreModel11,
        CreateMemoryStoreModel12,
        CreateMemoryStoreModel13,
        CreateMemoryStoreModel14,
        CreateMemoryStoreModel15,
        CreateMemoryStoreModel16,
        CreateMemoryStoreModel17,
    ],
)


CreateMemoryStoreModel = TypeAliasType(
    "CreateMemoryStoreModel",
    Union[
        CreateMemoryStoreModel1,
        CreateMemoryStoreModel2,
        CreateMemoryStoreModel3,
        CreateMemoryStoreModel4,
        CreateMemoryStoreModel5,
        CreateMemoryStoreModel6,
        CreateMemoryStoreModel7,
        CreateMemoryStoreModel8,
        CreateMemoryStoreModel9,
        CreateMemoryStoreModel10,
        CreateMemoryStoreModel11,
        CreateMemoryStoreModel12,
        CreateMemoryStoreModel13,
        CreateMemoryStoreModel14,
        CreateMemoryStoreModel15,
        CreateMemoryStoreModel16,
        CreateMemoryStoreModel17,
    ],
)


class CreateMemoryStoreEmbeddingConfigTypedDict(TypedDict):
    model: CreateMemoryStoreModelTypedDict


class CreateMemoryStoreEmbeddingConfig(BaseModel):
    model: CreateMemoryStoreModel


class CreateMemoryStoreResponseBodyTypedDict(TypedDict):
    r"""Memory store successfully created with the specified configuration."""

    id: str
    r"""The unique identifier of the memory store"""
    key: str
    r"""The unique key of the memory store. The key is unique and inmmutable and cannot be repeated within the same workspace."""
    description: str
    r"""The description of the memory store. Be as precise as possible to help the AI to understand the purpose of the memory store."""
    created: str
    r"""The creation date of the memory store"""
    updated: str
    r"""The last update date of the memory store"""
    embedding_config: CreateMemoryStoreEmbeddingConfigTypedDict
    created_by_id: NotRequired[str]
    r"""The user ID of the creator"""
    updated_by_id: NotRequired[str]
    r"""The user ID of the last updater"""
    ttl: NotRequired[float]
    r"""The default time to live of every memory document created within the memory store. Useful to control if the documents in the memory should be store for short or long term."""


class CreateMemoryStoreResponseBody(BaseModel):
    r"""Memory store successfully created with the specified configuration."""

    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the memory store"""

    key: str
    r"""The unique key of the memory store. The key is unique and inmmutable and cannot be repeated within the same workspace."""

    description: str
    r"""The description of the memory store. Be as precise as possible to help the AI to understand the purpose of the memory store."""

    created: str
    r"""The creation date of the memory store"""

    updated: str
    r"""The last update date of the memory store"""

    embedding_config: CreateMemoryStoreEmbeddingConfig

    created_by_id: Optional[str] = None
    r"""The user ID of the creator"""

    updated_by_id: Optional[str] = None
    r"""The user ID of the last updater"""

    ttl: Optional[float] = None
    r"""The default time to live of every memory document created within the memory store. Useful to control if the documents in the memory should be store for short or long term."""
