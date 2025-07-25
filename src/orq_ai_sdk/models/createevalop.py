"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from orq_ai_sdk.models import OrqError
from orq_ai_sdk.types import BaseModel
import pydantic
from typing import Any, Dict, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CreateEvalGuardrailConfigEvalsRequestRequestBody42Type = Literal["number"]

CreateEvalGuardrailConfigEvalsOperator = Literal["eq", "ne", "gt", "gte", "lt", "lte"]


class CreateEvalGuardrailConfigEvalsNumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsRequestRequestBody42Type
    value: float
    operator: CreateEvalGuardrailConfigEvalsOperator


class CreateEvalGuardrailConfigEvalsNumber(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsRequestRequestBody42Type

    value: float

    operator: CreateEvalGuardrailConfigEvalsOperator


CreateEvalGuardrailConfigEvalsRequestRequestBody4Type = Literal["boolean"]


class CreateEvalGuardrailConfigEvalsBooleanTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsRequestRequestBody4Type
    value: bool


class CreateEvalGuardrailConfigEvalsBoolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsRequestRequestBody4Type

    value: bool


CreateEvalRequestBodyEvalsGuardrailConfigTypedDict = TypeAliasType(
    "CreateEvalRequestBodyEvalsGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigEvalsBooleanTypedDict,
        CreateEvalGuardrailConfigEvalsNumberTypedDict,
    ],
)


CreateEvalRequestBodyEvalsGuardrailConfig = TypeAliasType(
    "CreateEvalRequestBodyEvalsGuardrailConfig",
    Union[CreateEvalGuardrailConfigEvalsBoolean, CreateEvalGuardrailConfigEvalsNumber],
)


CreateEvalRequestBodyEvalsRequestType = Literal["python_eval"]


class PythonTypedDict(TypedDict):
    code: str
    type: CreateEvalRequestBodyEvalsRequestType
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    guardrail_config: NotRequired[CreateEvalRequestBodyEvalsGuardrailConfigTypedDict]
    description: NotRequired[str]


class Python(BaseModel):
    code: str

    type: CreateEvalRequestBodyEvalsRequestType

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str

    guardrail_config: Optional[CreateEvalRequestBodyEvalsGuardrailConfig] = None

    description: Optional[str] = ""


CreateEvalGuardrailConfigEvalsRequestRequestBody3Type = Literal["number"]

CreateEvalGuardrailConfigOperator = Literal["eq", "ne", "gt", "gte", "lt", "lte"]


class CreateEvalGuardrailConfigNumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsRequestRequestBody3Type
    value: float
    operator: CreateEvalGuardrailConfigOperator


class CreateEvalGuardrailConfigNumber(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsRequestRequestBody3Type

    value: float

    operator: CreateEvalGuardrailConfigOperator


CreateEvalGuardrailConfigEvalsRequestRequestBodyType = Literal["boolean"]


class CreateEvalGuardrailConfigBooleanTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsRequestRequestBodyType
    value: bool


class CreateEvalGuardrailConfigBoolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsRequestRequestBodyType

    value: bool


CreateEvalRequestBodyGuardrailConfigTypedDict = TypeAliasType(
    "CreateEvalRequestBodyGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigBooleanTypedDict,
        CreateEvalGuardrailConfigNumberTypedDict,
    ],
)


CreateEvalRequestBodyGuardrailConfig = TypeAliasType(
    "CreateEvalRequestBodyGuardrailConfig",
    Union[CreateEvalGuardrailConfigBoolean, CreateEvalGuardrailConfigNumber],
)


CreateEvalRequestBodyEvalsType = Literal["http_eval"]

Method = Literal["GET", "POST"]


class HTTPTypedDict(TypedDict):
    type: CreateEvalRequestBodyEvalsType
    url: str
    method: Method
    headers: Dict[str, str]
    payload: Dict[str, Any]
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    guardrail_config: NotRequired[CreateEvalRequestBodyGuardrailConfigTypedDict]
    description: NotRequired[str]


class HTTP(BaseModel):
    type: CreateEvalRequestBodyEvalsType

    url: str

    method: Method

    headers: Dict[str, str]

    payload: Dict[str, Any]

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str

    guardrail_config: Optional[CreateEvalRequestBodyGuardrailConfig] = None

    description: Optional[str] = ""


CreateEvalGuardrailConfigEvalsRequestType = Literal["number"]

GuardrailConfigOperator = Literal["eq", "ne", "gt", "gte", "lt", "lte"]


class GuardrailConfigNumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsRequestType
    value: float
    operator: GuardrailConfigOperator


class GuardrailConfigNumber(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsRequestType

    value: float

    operator: GuardrailConfigOperator


CreateEvalGuardrailConfigEvalsType = Literal["boolean"]


class GuardrailConfigBooleanTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsType
    value: bool


class GuardrailConfigBoolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsType

    value: bool


RequestBodyGuardrailConfigTypedDict = TypeAliasType(
    "RequestBodyGuardrailConfigTypedDict",
    Union[GuardrailConfigBooleanTypedDict, GuardrailConfigNumberTypedDict],
)


RequestBodyGuardrailConfig = TypeAliasType(
    "RequestBodyGuardrailConfig", Union[GuardrailConfigBoolean, GuardrailConfigNumber]
)


CreateEvalRequestBodyType = Literal["json_schema"]


class JSONTypedDict(TypedDict):
    type: CreateEvalRequestBodyType
    schema_: str
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    key: str
    guardrail_config: NotRequired[RequestBodyGuardrailConfigTypedDict]
    description: NotRequired[str]


class JSON(BaseModel):
    type: CreateEvalRequestBodyType

    schema_: Annotated[str, pydantic.Field(alias="schema")]

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    key: str

    guardrail_config: Optional[RequestBodyGuardrailConfig] = None

    description: Optional[str] = ""


CreateEvalGuardrailConfigType = Literal["number"]

Operator = Literal["eq", "ne", "gt", "gte", "lt", "lte"]


class NumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigType
    value: float
    operator: Operator


class Number(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigType

    value: float

    operator: Operator


GuardrailConfigType = Literal["boolean"]


class BooleanTypedDict(TypedDict):
    enabled: bool
    type: GuardrailConfigType
    value: bool


class Boolean(BaseModel):
    enabled: bool

    type: GuardrailConfigType

    value: bool


GuardrailConfigTypedDict = TypeAliasType(
    "GuardrailConfigTypedDict", Union[BooleanTypedDict, NumberTypedDict]
)


GuardrailConfig = TypeAliasType("GuardrailConfig", Union[Boolean, Number])


RequestBodyType = Literal["llm_eval"]


class LlmTypedDict(TypedDict):
    type: RequestBodyType
    prompt: str
    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""
    model: str
    key: str
    guardrail_config: NotRequired[GuardrailConfigTypedDict]
    description: NotRequired[str]


class Llm(BaseModel):
    type: RequestBodyType

    prompt: str

    path: str
    r"""The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists."""

    model: str

    key: str

    guardrail_config: Optional[GuardrailConfig] = None

    description: Optional[str] = ""


CreateEvalRequestBodyTypedDict = TypeAliasType(
    "CreateEvalRequestBodyTypedDict",
    Union[JSONTypedDict, PythonTypedDict, LlmTypedDict, HTTPTypedDict],
)


CreateEvalRequestBody = TypeAliasType(
    "CreateEvalRequestBody", Union[JSON, Python, Llm, HTTP]
)


class CreateEvalEvalsResponseBodyData(BaseModel):
    message: str


class CreateEvalEvalsResponseBody(OrqError):
    r"""Workspace ID is not found on the request"""

    data: CreateEvalEvalsResponseBodyData

    def __init__(
        self,
        data: CreateEvalEvalsResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        fallback = body or raw_response.text
        message = str(data.message) or fallback
        super().__init__(message, raw_response, body)
        self.data = data


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody42Type = Literal[
    "number"
]

CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyOperator = Literal[
    "eq", "ne", "gt", "gte", "lt", "lte"
]


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyNumberTypedDict(
    TypedDict
):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody42Type
    value: float
    operator: (
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyOperator
    )


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyNumber(
    BaseModel
):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody42Type

    value: float

    operator: (
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyOperator
    )


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody4Type = Literal[
    "boolean"
]


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyBooleanTypedDict(
    TypedDict
):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody4Type
    value: bool


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyBoolean(
    BaseModel
):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody4Type

    value: bool


CreateEvalResponseBodyEvalsResponseGuardrailConfigTypedDict = TypeAliasType(
    "CreateEvalResponseBodyEvalsResponseGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyBooleanTypedDict,
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyNumberTypedDict,
    ],
)


CreateEvalResponseBodyEvalsResponseGuardrailConfig = TypeAliasType(
    "CreateEvalResponseBodyEvalsResponseGuardrailConfig",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyBoolean,
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyNumber,
    ],
)


CreateEvalResponseBodyEvalsResponseType = Literal["python_eval"]


class ResponseBodyPythonTypedDict(TypedDict):
    id: str
    description: str
    code: str
    type: CreateEvalResponseBodyEvalsResponseType
    key: str
    created: NotRequired[str]
    updated: NotRequired[str]
    guardrail_config: NotRequired[
        CreateEvalResponseBodyEvalsResponseGuardrailConfigTypedDict
    ]


class ResponseBodyPython(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    description: str

    code: str

    type: CreateEvalResponseBodyEvalsResponseType

    key: str

    created: Optional[str] = "2025-07-25T10:00:02.717Z"

    updated: Optional[str] = "2025-07-25T10:00:02.717Z"

    guardrail_config: Optional[CreateEvalResponseBodyEvalsResponseGuardrailConfig] = (
        None
    )


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody32Type = Literal[
    "number"
]

CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONOperator = Literal[
    "eq", "ne", "gt", "gte", "lt", "lte"
]


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONNumberTypedDict(
    TypedDict
):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody32Type
    value: float
    operator: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONOperator


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONNumber(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody32Type

    value: float

    operator: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONOperator


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody3Type = Literal[
    "boolean"
]


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONBooleanTypedDict(
    TypedDict
):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody3Type
    value: bool


class CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONBoolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBody3Type

    value: bool


CreateEvalResponseBodyEvalsGuardrailConfigTypedDict = TypeAliasType(
    "CreateEvalResponseBodyEvalsGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONBooleanTypedDict,
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONNumberTypedDict,
    ],
)


CreateEvalResponseBodyEvalsGuardrailConfig = TypeAliasType(
    "CreateEvalResponseBodyEvalsGuardrailConfig",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONBoolean,
        CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONNumber,
    ],
)


CreateEvalResponseBodyEvalsType = Literal["http_eval"]

ResponseBodyMethod = Literal["GET", "POST"]


class ResponseBodyHTTPTypedDict(TypedDict):
    id: str
    description: str
    type: CreateEvalResponseBodyEvalsType
    url: str
    method: ResponseBodyMethod
    headers: Dict[str, str]
    payload: Dict[str, Any]
    key: str
    created: NotRequired[str]
    updated: NotRequired[str]
    guardrail_config: NotRequired[CreateEvalResponseBodyEvalsGuardrailConfigTypedDict]


class ResponseBodyHTTP(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    description: str

    type: CreateEvalResponseBodyEvalsType

    url: str

    method: ResponseBodyMethod

    headers: Dict[str, str]

    payload: Dict[str, Any]

    key: str

    created: Optional[str] = "2025-07-25T10:00:02.717Z"

    updated: Optional[str] = "2025-07-25T10:00:02.717Z"

    guardrail_config: Optional[CreateEvalResponseBodyEvalsGuardrailConfig] = None


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyType = Literal[
    "number"
]

CreateEvalGuardrailConfigEvalsResponse200Operator = Literal[
    "eq", "ne", "gt", "gte", "lt", "lte"
]


class CreateEvalGuardrailConfigEvalsResponse200NumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyType
    value: float
    operator: CreateEvalGuardrailConfigEvalsResponse200Operator


class CreateEvalGuardrailConfigEvalsResponse200Number(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONResponseBodyType

    value: float

    operator: CreateEvalGuardrailConfigEvalsResponse200Operator


CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONType = Literal["boolean"]


class CreateEvalGuardrailConfigEvalsResponse200BooleanTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONType
    value: bool


class CreateEvalGuardrailConfigEvalsResponse200Boolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200ApplicationJSONType

    value: bool


CreateEvalResponseBodyGuardrailConfigTypedDict = TypeAliasType(
    "CreateEvalResponseBodyGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200BooleanTypedDict,
        CreateEvalGuardrailConfigEvalsResponse200NumberTypedDict,
    ],
)


CreateEvalResponseBodyGuardrailConfig = TypeAliasType(
    "CreateEvalResponseBodyGuardrailConfig",
    Union[
        CreateEvalGuardrailConfigEvalsResponse200Boolean,
        CreateEvalGuardrailConfigEvalsResponse200Number,
    ],
)


CreateEvalResponseBodyType = Literal["json_schema"]


class ResponseBodyJSONTypedDict(TypedDict):
    id: str
    description: str
    type: CreateEvalResponseBodyType
    schema_: str
    key: str
    created: NotRequired[str]
    updated: NotRequired[str]
    guardrail_config: NotRequired[CreateEvalResponseBodyGuardrailConfigTypedDict]


class ResponseBodyJSON(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    description: str

    type: CreateEvalResponseBodyType

    schema_: Annotated[str, pydantic.Field(alias="schema")]

    key: str

    created: Optional[str] = "2025-07-25T10:00:02.717Z"

    updated: Optional[str] = "2025-07-25T10:00:02.717Z"

    guardrail_config: Optional[CreateEvalResponseBodyGuardrailConfig] = None


CreateEvalGuardrailConfigEvalsResponse200Type = Literal["number"]

CreateEvalGuardrailConfigEvalsResponseOperator = Literal[
    "eq", "ne", "gt", "gte", "lt", "lte"
]


class CreateEvalGuardrailConfigEvalsResponseNumberTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponse200Type
    value: float
    operator: CreateEvalGuardrailConfigEvalsResponseOperator


class CreateEvalGuardrailConfigEvalsResponseNumber(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponse200Type

    value: float

    operator: CreateEvalGuardrailConfigEvalsResponseOperator


CreateEvalGuardrailConfigEvalsResponseType = Literal["boolean"]


class CreateEvalGuardrailConfigEvalsResponseBooleanTypedDict(TypedDict):
    enabled: bool
    type: CreateEvalGuardrailConfigEvalsResponseType
    value: bool


class CreateEvalGuardrailConfigEvalsResponseBoolean(BaseModel):
    enabled: bool

    type: CreateEvalGuardrailConfigEvalsResponseType

    value: bool


ResponseBodyGuardrailConfigTypedDict = TypeAliasType(
    "ResponseBodyGuardrailConfigTypedDict",
    Union[
        CreateEvalGuardrailConfigEvalsResponseBooleanTypedDict,
        CreateEvalGuardrailConfigEvalsResponseNumberTypedDict,
    ],
)


ResponseBodyGuardrailConfig = TypeAliasType(
    "ResponseBodyGuardrailConfig",
    Union[
        CreateEvalGuardrailConfigEvalsResponseBoolean,
        CreateEvalGuardrailConfigEvalsResponseNumber,
    ],
)


ResponseBodyType = Literal["llm_eval"]


class ResponseBodyLLMTypedDict(TypedDict):
    id: str
    description: str
    type: ResponseBodyType
    prompt: str
    key: str
    model: str
    created: NotRequired[str]
    updated: NotRequired[str]
    guardrail_config: NotRequired[ResponseBodyGuardrailConfigTypedDict]


class ResponseBodyLLM(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    description: str

    type: ResponseBodyType

    prompt: str

    key: str

    model: str

    created: Optional[str] = "2025-07-25T10:00:02.717Z"

    updated: Optional[str] = "2025-07-25T10:00:02.717Z"

    guardrail_config: Optional[ResponseBodyGuardrailConfig] = None


CreateEvalResponseBodyTypedDict = TypeAliasType(
    "CreateEvalResponseBodyTypedDict",
    Union[
        ResponseBodyJSONTypedDict,
        ResponseBodyPythonTypedDict,
        ResponseBodyLLMTypedDict,
        ResponseBodyHTTPTypedDict,
    ],
)
r"""Successfully created an evaluator"""


CreateEvalResponseBody = TypeAliasType(
    "CreateEvalResponseBody",
    Union[ResponseBodyJSON, ResponseBodyPython, ResponseBodyLLM, ResponseBodyHTTP],
)
r"""Successfully created an evaluator"""
