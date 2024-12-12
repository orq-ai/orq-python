"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_ai_sdk.types import BaseModel
import pydantic
from typing import List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


ValueTypedDict = TypeAliasType("ValueTypedDict", Union[str, List[str]])
r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""


Value = TypeAliasType("Value", Union[str, List[str]])
r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""


class CreateFeedbackRequestBodyTypedDict(TypedDict):
    r"""Feedback submission payload"""

    field: str
    r"""A string describing the specific property or aspect rated."""
    value: ValueTypedDict
    r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""
    trace_id: str
    r"""The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints"""


class CreateFeedbackRequestBody(BaseModel):
    r"""Feedback submission payload"""

    field: Annotated[str, pydantic.Field(alias="property")]
    r"""A string describing the specific property or aspect rated."""

    value: Value
    r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""

    trace_id: str
    r"""The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints"""


CreateFeedbackValueTypedDict = TypeAliasType(
    "CreateFeedbackValueTypedDict", Union[str, List[str]]
)
r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""


CreateFeedbackValue = TypeAliasType("CreateFeedbackValue", Union[str, List[str]])
r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""


class CreateFeedbackResponseBodyTypedDict(TypedDict):
    r"""Successful operation"""

    property: str
    r"""A string describing the specific property or aspect rated."""
    value: CreateFeedbackValueTypedDict
    r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""
    trace_id: str
    r"""The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints"""
    id: str


class CreateFeedbackResponseBody(BaseModel):
    r"""Successful operation"""

    property: str
    r"""A string describing the specific property or aspect rated."""

    value: CreateFeedbackValue
    r"""The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string."""

    trace_id: str
    r"""The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints"""

    id: str
