"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from orq_ai_sdk.models import OrqError
from orq_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class EvalsPiiRequestBodyTypedDict(TypedDict):
    query: str
    output: str
    model: str


class EvalsPiiRequestBody(BaseModel):
    query: str

    output: str

    model: str


class EvalsPiiEvalsResponseResponseBodyData(BaseModel):
    message: str


class EvalsPiiEvalsResponseResponseBody(OrqError):
    r"""Internal server error"""

    data: EvalsPiiEvalsResponseResponseBodyData

    def __init__(
        self,
        data: EvalsPiiEvalsResponseResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        fallback = body or raw_response.text
        message = str(data.message) or fallback
        super().__init__(message, raw_response, body)
        self.data = data


class EvalsPiiEvalsResponseBodyData(BaseModel):
    message: str


class EvalsPiiEvalsResponseBody(OrqError):
    r"""Evaluator not found"""

    data: EvalsPiiEvalsResponseBodyData

    def __init__(
        self,
        data: EvalsPiiEvalsResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        fallback = body or raw_response.text
        message = str(data.message) or fallback
        super().__init__(message, raw_response, body)
        self.data = data


EvalsPiiEvalsValueTypedDict = TypeAliasType(
    "EvalsPiiEvalsValueTypedDict", Union[float, bool, str]
)


EvalsPiiEvalsValue = TypeAliasType("EvalsPiiEvalsValue", Union[float, bool, str])


class EvalsPiiValueTypedDict(TypedDict):
    value: EvalsPiiEvalsValueTypedDict
    explanation: NotRequired[Nullable[str]]


class EvalsPiiValue(BaseModel):
    value: EvalsPiiEvalsValue

    explanation: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["explanation"]
        nullable_fields = ["explanation"]
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


class EvalsPiiResponseBodyTypedDict(TypedDict):
    r"""Returns the result of the evaluator run"""

    value: Nullable[EvalsPiiValueTypedDict]


class EvalsPiiResponseBody(BaseModel):
    r"""Returns the result of the evaluator run"""

    value: Nullable[EvalsPiiValue]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["value"]
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
