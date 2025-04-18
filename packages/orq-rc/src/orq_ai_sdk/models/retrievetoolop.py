"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET_SENTINEL
from orq_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class RetrieveToolRequestTypedDict(TypedDict):
    tool_key: str


class RetrieveToolRequest(BaseModel):
    tool_key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


RetrieveToolResponseBodyToolsResponseStatus = Literal[
    "live", "draft", "pending", "published"
]
r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

RetrieveToolResponseBodyToolsResponseType = Literal["orq_http"]

RetrieveToolResponseBodyMethod = Literal["GET", "POST", "PUT", "DELETE"]
r"""The HTTP method to use."""


class RetrieveToolResponseBodyBlueprintTypedDict(TypedDict):
    r"""The blueprint for the HTTP request. The `arguments` field will be used to replace the placeholders in the `url`, `headers`, `body`, and `arguments` fields."""

    url: str
    r"""The URL to send the request to."""
    method: RetrieveToolResponseBodyMethod
    r"""The HTTP method to use."""
    headers: NotRequired[Dict[str, str]]
    r"""The headers to send with the request."""
    body: NotRequired[Dict[str, Any]]
    r"""The body to send with the request."""


class RetrieveToolResponseBodyBlueprint(BaseModel):
    r"""The blueprint for the HTTP request. The `arguments` field will be used to replace the placeholders in the `url`, `headers`, `body`, and `arguments` fields."""

    url: str
    r"""The URL to send the request to."""

    method: RetrieveToolResponseBodyMethod
    r"""The HTTP method to use."""

    headers: Optional[Dict[str, str]] = None
    r"""The headers to send with the request."""

    body: Optional[Dict[str, Any]] = None
    r"""The body to send with the request."""


RetrieveToolResponseBodyToolsResponse200Type = Literal["string", "number", "boolean"]
r"""The type of the argument."""

RetrieveToolResponseBodyDefaultValueTypedDict = TypeAliasType(
    "RetrieveToolResponseBodyDefaultValueTypedDict", Union[str, float, bool]
)
r"""The default value of the argument."""


RetrieveToolResponseBodyDefaultValue = TypeAliasType(
    "RetrieveToolResponseBodyDefaultValue", Union[str, float, bool]
)
r"""The default value of the argument."""


class RetrieveToolResponseBodyArgumentsTypedDict(TypedDict):
    type: RetrieveToolResponseBodyToolsResponse200Type
    r"""The type of the argument."""
    description: str
    r"""A description of the argument."""
    send_to_model: NotRequired[bool]
    r"""Whether to send the argument to the model. If set to false, the argument will not be sent to the model and needs to be provided by the user or it will be left blank."""
    default_value: NotRequired[RetrieveToolResponseBodyDefaultValueTypedDict]
    r"""The default value of the argument."""


class RetrieveToolResponseBodyArguments(BaseModel):
    type: RetrieveToolResponseBodyToolsResponse200Type
    r"""The type of the argument."""

    description: str
    r"""A description of the argument."""

    send_to_model: Optional[bool] = True
    r"""Whether to send the argument to the model. If set to false, the argument will not be sent to the model and needs to be provided by the user or it will be left blank."""

    default_value: Optional[RetrieveToolResponseBodyDefaultValue] = None
    r"""The default value of the argument."""


class RetrieveToolResponseBodyHTTPTypedDict(TypedDict):
    blueprint: RetrieveToolResponseBodyBlueprintTypedDict
    r"""The blueprint for the HTTP request. The `arguments` field will be used to replace the placeholders in the `url`, `headers`, `body`, and `arguments` fields."""
    arguments: NotRequired[Dict[str, RetrieveToolResponseBodyArgumentsTypedDict]]
    r"""The arguments to send with the request. The keys will be used to replace the placeholders in the `blueprint` field."""


class RetrieveToolResponseBodyHTTP(BaseModel):
    blueprint: RetrieveToolResponseBodyBlueprint
    r"""The blueprint for the HTTP request. The `arguments` field will be used to replace the placeholders in the `url`, `headers`, `body`, and `arguments` fields."""

    arguments: Optional[Dict[str, RetrieveToolResponseBodyArguments]] = None
    r"""The arguments to send with the request. The keys will be used to replace the placeholders in the `blueprint` field."""


class RetrieveToolResponseBody3TypedDict(TypedDict):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""
    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""
    project_id: str
    workspace_id: str
    created: str
    updated: str
    status: RetrieveToolResponseBodyToolsResponseStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""
    version_hash: str
    type: RetrieveToolResponseBodyToolsResponseType
    http: RetrieveToolResponseBodyHTTPTypedDict
    id: NotRequired[str]
    created_by_id: NotRequired[str]
    r"""The id of the user that created the tool"""
    updated_by_id: NotRequired[str]
    r"""The id of the user that last updated the tool"""


class RetrieveToolResponseBody3(BaseModel):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""

    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""

    project_id: str

    workspace_id: str

    created: str

    updated: str

    status: RetrieveToolResponseBodyToolsResponseStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

    version_hash: str

    type: RetrieveToolResponseBodyToolsResponseType

    http: RetrieveToolResponseBodyHTTP

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "tool_01JS405PMNJ6DGFVRHBPP9YWAD"
    )

    created_by_id: Optional[str] = None
    r"""The id of the user that created the tool"""

    updated_by_id: Optional[str] = None
    r"""The id of the user that last updated the tool"""


RetrieveToolResponseBodyToolsStatus = Literal["live", "draft", "pending", "published"]
r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

RetrieveToolResponseBodyToolsType = Literal["json_schema"]


class RetrieveToolResponseBodyJSONSchemaTypedDict(TypedDict):
    name: str
    r"""The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""
    schema_: Dict[str, Any]
    r"""The schema for the response format, described as a JSON Schema object. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format."""
    description: NotRequired[str]
    r"""A description of what the response format is for. This will be shown to the user."""
    strict: NotRequired[Nullable[bool]]
    r"""Whether to enable strict schema adherence when generating the output. If set to true, the model will always follow the exact schema defined in the `schema` field. Only a subset of JSON Schema is supported when `strict` is `true`. Only compatible with `OpenAI` models."""


class RetrieveToolResponseBodyJSONSchema(BaseModel):
    name: str
    r"""The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]
    r"""The schema for the response format, described as a JSON Schema object. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format."""

    description: Optional[str] = None
    r"""A description of what the response format is for. This will be shown to the user."""

    strict: OptionalNullable[bool] = False
    r"""Whether to enable strict schema adherence when generating the output. If set to true, the model will always follow the exact schema defined in the `schema` field. Only a subset of JSON Schema is supported when `strict` is `true`. Only compatible with `OpenAI` models."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "strict"]
        nullable_fields = ["strict"]
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


class RetrieveToolResponseBody2TypedDict(TypedDict):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""
    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""
    project_id: str
    workspace_id: str
    created: str
    updated: str
    status: RetrieveToolResponseBodyToolsStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""
    version_hash: str
    type: RetrieveToolResponseBodyToolsType
    json_schema: RetrieveToolResponseBodyJSONSchemaTypedDict
    id: NotRequired[str]
    created_by_id: NotRequired[str]
    r"""The id of the user that created the tool"""
    updated_by_id: NotRequired[str]
    r"""The id of the user that last updated the tool"""


class RetrieveToolResponseBody2(BaseModel):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""

    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""

    project_id: str

    workspace_id: str

    created: str

    updated: str

    status: RetrieveToolResponseBodyToolsStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

    version_hash: str

    type: RetrieveToolResponseBodyToolsType

    json_schema: RetrieveToolResponseBodyJSONSchema

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "tool_01JS405PMM4BPNSCW61WEV7ZZW"
    )

    created_by_id: Optional[str] = None
    r"""The id of the user that created the tool"""

    updated_by_id: Optional[str] = None
    r"""The id of the user that last updated the tool"""


RetrieveToolResponseBodyStatus = Literal["live", "draft", "pending", "published"]
r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

RetrieveToolResponseBodyType = Literal["function"]


class RetrieveToolResponseBodyFunctionTypedDict(TypedDict):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""
    description: NotRequired[str]
    r"""A description of what the function does, used by the model to choose when and how to call the function."""
    strict: NotRequired[bool]
    r"""Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Currently only compatible with `OpenAI` models."""
    parameters: NotRequired[Dict[str, Any]]
    r"""The parameters the functions accepts, described as a JSON Schema object. See the `OpenAI` [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format."""


class RetrieveToolResponseBodyFunction(BaseModel):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""

    description: Optional[str] = None
    r"""A description of what the function does, used by the model to choose when and how to call the function."""

    strict: Optional[bool] = None
    r"""Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Currently only compatible with `OpenAI` models."""

    parameters: Optional[Dict[str, Any]] = None
    r"""The parameters the functions accepts, described as a JSON Schema object. See the `OpenAI` [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format."""


class RetrieveToolResponseBody1TypedDict(TypedDict):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""
    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""
    project_id: str
    workspace_id: str
    created: str
    updated: str
    status: RetrieveToolResponseBodyStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""
    version_hash: str
    type: RetrieveToolResponseBodyType
    function: RetrieveToolResponseBodyFunctionTypedDict
    id: NotRequired[str]
    created_by_id: NotRequired[str]
    r"""The id of the user that created the tool"""
    updated_by_id: NotRequired[str]
    r"""The id of the user that last updated the tool"""


class RetrieveToolResponseBody1(BaseModel):
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str
    r"""Unique key of the tool as it will be displayed in the UI"""

    description: str
    r"""A description of the tool, used by the model to choose when and how to call the tool. We do recommend using the `description` field as accurate as possible to give enough context to the model to make the right decision."""

    project_id: str

    workspace_id: str

    created: str

    updated: str

    status: RetrieveToolResponseBodyStatus
    r"""The status of the tool. `Live` is the latest version of the tool. `Draft` is a version that is not yet published. `Pending` is a version that is pending approval. `Published` is a version that was live and has been replaced by a new version."""

    version_hash: str

    type: RetrieveToolResponseBodyType

    function: RetrieveToolResponseBodyFunction

    id: Annotated[Optional[str], pydantic.Field(alias="_id")] = (
        "tool_01JS405PM9WE275JXGM0Q8DGXP"
    )

    created_by_id: Optional[str] = None
    r"""The id of the user that created the tool"""

    updated_by_id: Optional[str] = None
    r"""The id of the user that last updated the tool"""


RetrieveToolResponseBodyTypedDict = TypeAliasType(
    "RetrieveToolResponseBodyTypedDict",
    Union[
        RetrieveToolResponseBody1TypedDict,
        RetrieveToolResponseBody2TypedDict,
        RetrieveToolResponseBody3TypedDict,
    ],
)
r"""Successfully retrieved the tool."""


RetrieveToolResponseBody = TypeAliasType(
    "RetrieveToolResponseBody",
    Union[
        RetrieveToolResponseBody1, RetrieveToolResponseBody2, RetrieveToolResponseBody3
    ],
)
r"""Successfully retrieved the tool."""
