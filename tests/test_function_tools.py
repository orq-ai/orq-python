from __future__ import annotations

import json
import warnings
from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Literal, NewType, Optional

import pytest
from pydantic import BaseModel

from orq_ai_sdk import models, utils
from orq_ai_sdk.function_tools import ToolFunctionWrapper, ToolSchemaError, tool, tool_schema
from orq_ai_sdk.models.create_router_responseop import CreateRouterResponseRequestBody, ToolsFunction


class Tone(str, Enum):
    WARM = "warm"
    COLD = "cold"


UserId = NewType("UserId", int)


class GuestInfo(BaseModel):
    name: str


@dataclass
class Point:
    x: int
    y: int


def test_tool_decorator_uses_function_name_and_docstring():
    @tool
    def emit_magic_token(reason: str) -> str:
        """Return a diagnostic token."""

    schema = tool_schema(emit_magic_token).model_dump(mode="json", exclude_none=True)

    assert schema == {
        "name": "emit_magic_token",
        "type": "function",
        "description": "Return a diagnostic token.",
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {"type": "string"},
            },
            "required": ["reason"],
            "additionalProperties": False,
        },
        "strict": True,
    }


def test_tool_empty_call_form_matches_bare_decorator():
    @tool
    def bare(reason: str) -> str:
        """Bare decorator."""

    @tool()
    def called(reason: str) -> str:
        """Called decorator."""

    assert bare.schema["name"] == "bare"
    assert bare.schema["description"] == "Bare decorator."
    assert called.schema["name"] == "called"
    assert called.schema["description"] == "Called decorator."
    assert bare.schema["strict"] is True
    assert called.schema["strict"] is True


def test_tool_decorator_override_replaces_name_and_description():
    @tool(name="custom_emit", description="Decorator override description.")
    def emit_magic_token(reason: str) -> str:
        """Original docstring."""

    assert emit_magic_token.schema["name"] == "custom_emit"
    assert emit_magic_token.schema["description"] == "Decorator override description."


def test_tool_schema_override_can_rebuild_wrapped_function_schema():
    @tool(name="decorated_name", description="Decorated description.")
    def emit_magic_token(reason: str) -> str:
        """Original docstring."""

    overridden = tool_schema(
        emit_magic_token,
        name="runtime_override",
        description="Runtime override description.",
    ).model_dump(mode="json", exclude_none=True)

    assert overridden["name"] == "runtime_override"
    assert overridden["description"] == "Runtime override description."
    assert overridden["strict"] is True


def test_tool_schema_supports_optional_literal_enum_and_list():
    def describe(
        reason: str,
        tags: list[str] | None = None,
        mode: Literal["short", "long"] = "short",
        tone: Tone = Tone.WARM,
        retries: int = 1,
        temperature: float = 0.5,
        *,
        enabled: bool = True,
    ) -> str:
        """Describe a request."""

    schema = tool_schema(describe, strict=False).model_dump(mode="json", exclude_none=True)
    properties = schema["parameters"]["properties"]

    assert properties["reason"] == {"type": "string"}
    assert properties["tags"] == {
        "anyOf": [
            {"type": "array", "items": {"type": "string"}},
            {"type": "null"},
        ],
    }
    assert properties["mode"] == {"type": "string", "enum": ["short", "long"]}
    assert properties["tone"] == {"type": "string", "enum": ["warm", "cold"]}
    assert properties["retries"] == {"type": "integer"}
    assert properties["temperature"] == {"type": "number"}
    assert properties["enabled"] == {"type": "boolean"}
    assert schema["parameters"]["required"] == ["reason"]


def test_non_strict_schema_marks_only_parameters_without_defaults_as_required():
    def emit_magic_token(reason: str, category: str, retries: int = 0) -> str:
        """Return a token."""

    schema = tool_schema(emit_magic_token, strict=False).model_dump(mode="json", exclude_none=True)

    assert schema["parameters"]["required"] == ["reason", "category"]


def test_strict_schema_requires_all_params_and_makes_defaulted_ones_nullable():
    # OpenAI's strict function-calling spec 400s unless every property is in
    # `required`; defaulted params must instead be expressed as nullable.
    def emit_magic_token(reason: str, retries: int = 0, tags: list[str] | None = None) -> str:
        """Return a token."""

    schema = tool_schema(emit_magic_token).model_dump(mode="json", exclude_none=True)
    props = schema["parameters"]["properties"]

    assert schema["strict"] is True
    assert schema["parameters"]["required"] == ["reason", "retries", "tags"]
    assert props["reason"] == {"type": "string"}
    assert props["retries"] == {"anyOf": [{"type": "integer"}, {"type": "null"}]}
    # Already-optional defaulted params don't get a duplicate null branch.
    assert props["tags"] == {
        "anyOf": [
            {"type": "array", "items": {"type": "string"}},
            {"type": "null"},
        ],
    }


def test_strict_schema_warns_when_parameters_have_defaults():
    def emit_magic_token(reason: str, retries: int = 0) -> str:
        """Return a token."""

    with pytest.warns(UserWarning, match="Python defaults are likely ignored") as record:
        tool_schema(emit_magic_token)

    assert "retries" in str(record[0].message)


def test_non_strict_schema_does_not_warn_about_defaults(recwarn):
    def emit_magic_token(reason: str, retries: int = 0) -> str:
        """Return a token."""

    tool_schema(emit_magic_token, strict=False)

    assert not recwarn.list


def test_strict_schema_without_defaults_does_not_warn(recwarn):
    def emit_magic_token(reason: str) -> str:
        """Return a token."""

    tool_schema(emit_magic_token)

    assert not recwarn.list


def test_strict_schema_does_not_warn_for_none_default():
    # An Optional param defaulting to None round-trips (model sends null -> None),
    # so the default isn't lost and no warning should fire.
    def emit_magic_token(reason: str, tags: list[str] | None = None) -> str:
        """Return a token."""

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        tool_schema(emit_magic_token)


def test_tool_schema_on_wrapper_respects_strict_override():
    @tool  # strict=True by default
    def emit_magic_token(reason: str, retries: int = 0) -> str:
        """Return a token."""

    reschema = tool_schema(emit_magic_token, strict=False)

    assert reschema.strict is False
    # strict=False drops defaulted params from `required` instead of nullable-ing them.
    assert reschema.parameters["required"] == ["reason"]


def test_annotated_parameters_are_unwrapped():
    def emit_magic_token(reason: Annotated[str, "why"], retries: Annotated[int, "count"] = 0) -> str:
        """Return a token."""

    props = tool_schema(emit_magic_token, strict=False).model_dump(mode="json")["parameters"][
        "properties"
    ]

    assert props["reason"] == {"type": "string"}
    assert props["retries"] == {"type": "integer"}


def test_tool_schema_on_wrapper_with_override_keeps_existing_description():
    @tool(description="Custom decorator description.")
    def emit_magic_token(reason: str) -> str:
        """Docstring that should be ignored."""

    reschema = tool_schema(emit_magic_token, name="renamed")

    assert reschema.name == "renamed"
    assert reschema.description == "Custom decorator description."


def test_tool_wrapper_remains_callable_and_exposes_schema_attributes():
    @tool
    def emit_magic_token(reason: str) -> str:
        """Return a diagnostic token."""

        return f"magic:{reason}"

    assert isinstance(emit_magic_token, ToolFunctionWrapper)
    assert emit_magic_token("check") == "magic:check"
    assert emit_magic_token.raw_function("check") == "magic:check"
    assert emit_magic_token.__name__ == "emit_magic_token"
    assert emit_magic_token.type == "function"
    assert emit_magic_token.name == "emit_magic_token"
    assert emit_magic_token.description == "Return a diagnostic token."
    assert emit_magic_token.parameters == {
        "type": "object",
        "properties": {"reason": {"type": "string"}},
        "required": ["reason"],
        "additionalProperties": False,
    }
    assert emit_magic_token.strict is True


def test_wrapped_tool_is_coerced_by_generated_sdk_tools_union():
    @tool
    def emit_magic_token(reason: str) -> str:
        """Return a diagnostic token."""

    coerced = utils.get_pydantic_model(
        [emit_magic_token],
        Optional[list[models.CreateRouterResponseTools]],
    )

    assert isinstance(coerced, list)
    assert len(coerced) == 1
    assert isinstance(coerced[0], ToolsFunction)
    assert coerced[0].model_dump(mode="json", exclude_none=True) == emit_magic_token.schema


def test_wrapped_tool_can_be_used_in_request_body_model():
    @tool
    def emit_magic_token(reason: str) -> str:
        """Return a diagnostic token."""

    request = CreateRouterResponseRequestBody(
        model="google-ai/gemini-2.5-flash",
        input="Call the tool.",
        tools=[emit_magic_token],
    )

    assert request.model_dump(mode="json", exclude_none=True)["tools"] == [
        emit_magic_token.schema,
    ]


def test_tool_schema_rejects_missing_parameter_annotations():
    def emit_magic_token(reason, category: str) -> str:
        """Return a diagnostic token."""

    with pytest.raises(ToolSchemaError, match="missing a type annotation"):
        tool_schema(emit_magic_token)


def test_tool_schema_rejects_positional_only_parameters():
    def emit_magic_token(reason: str, /) -> str:
        """Return a diagnostic token."""

    with pytest.raises(ToolSchemaError, match="positional-only"):
        tool_schema(emit_magic_token)


def test_tool_schema_rejects_var_args_and_var_kwargs():
    def with_args(reason: str, *extras: str) -> str:
        """Return a diagnostic token."""

    def with_kwargs(reason: str, **metadata: str) -> str:
        """Return a diagnostic token."""

    with pytest.raises(ToolSchemaError, match="\\*args"):
        tool_schema(with_args)

    with pytest.raises(ToolSchemaError, match="\\*\\*kwargs"):
        tool_schema(with_kwargs)


def test_tool_schema_rejects_unsupported_annotations():
    def emit_magic_token(metadata: complex) -> str:
        """Return a diagnostic token."""

    with pytest.raises(ToolSchemaError, match="Unsupported annotation"):
        tool_schema(emit_magic_token)


def test_bare_and_mapping_containers_give_clear_error():
    def bare_list(items: list) -> str:
        """Bare list."""

    def mapping(m: dict[str, int]) -> str:
        """Mapping."""

    with pytest.raises(ToolSchemaError, match="parameterized item type"):
        tool_schema(bare_list)
    with pytest.raises(ToolSchemaError, match="parameterized item type"):
        tool_schema(mapping)


def test_async_functions_are_rejected():
    async def emit_magic_token(reason: str) -> str:
        """Async tool."""

    with pytest.raises(ToolSchemaError, match="async"):
        tool_schema(emit_magic_token)


def test_partial_is_normalized_to_tool_schema_error():
    from functools import partial

    def base(a: int, b: int) -> int:
        """Base."""
        return a + b

    with pytest.raises(ToolSchemaError):
        tool_schema(partial(base, b=1))


def test_method_self_parameter_is_skipped():
    class Service:
        @tool
        def lookup(self, city: str) -> str:
            """Look up a city."""
            return city

    assert Service.lookup.schema["parameters"]["required"] == ["city"]
    assert "self" not in Service.lookup.schema["parameters"]["properties"]


def test_lambda_name_is_rejected_but_explicit_name_works():
    f = lambda city: city  # noqa: E731
    f.__annotations__ = {"city": str, "return": str}

    with pytest.raises(ToolSchemaError, match="invalid"):
        tool_schema(f)

    assert tool_schema(f, name="lookup").name == "lookup"


def test_literal_with_none_becomes_nullable():
    def describe(mode: Literal["short", "long", None] = None) -> str:
        """Describe."""

    props = tool_schema(describe, strict=False).model_dump(mode="json")["parameters"]["properties"]

    assert props["mode"] == {
        "anyOf": [{"type": "string", "enum": ["short", "long"]}, {"type": "null"}],
    }


def test_multi_branch_union_is_rejected():
    def describe(value: int | str) -> str:
        """Describe."""

    with pytest.raises(ToolSchemaError, match="multi-branch"):
        tool_schema(describe)


def test_newtype_is_unwrapped_to_supertype():
    def get(user: UserId) -> str:
        """Get user."""

    props = tool_schema(get).model_dump(mode="json")["parameters"]["properties"]

    assert props["user"] == {"type": "integer"}


def test_pydantic_and_dataclass_params_are_rejected_clearly():
    def book(guest: GuestInfo) -> str:
        """Book."""

    def plot(point: Point) -> str:
        """Plot."""

    with pytest.raises(ToolSchemaError, match="Pydantic model or dataclass"):
        tool_schema(book)
    with pytest.raises(ToolSchemaError, match="Pydantic model or dataclass"):
        tool_schema(plot)


def test_wrapper_is_hashable_with_identity_semantics():
    @tool(name="shared", description="Shared.")
    def a(x: int) -> int:
        """A."""
        return x + 1

    @tool(name="shared", description="Shared.")
    def b(x: int) -> int:
        """B."""
        return x - 1

    # Same schema payload, but different tools -> not equal, both hashable.
    assert a.schema == b.schema
    assert a != b
    assert a == a
    assert len({a, b}) == 2


def test_redecorating_wrapper_applies_new_override():
    @tool
    def emit(reason: str) -> str:
        """Original."""
        return reason

    redecorated = tool(name="outer", description="Outer desc.")(emit)

    assert redecorated.schema["name"] == "outer"
    assert redecorated.schema["description"] == "Outer desc."
    assert redecorated("hi") == "hi"  # still points at the real function


def test_wrapper_forwards_null_instead_of_applying_default():
    @tool
    def get_weather(city: str, units: str = "celsius") -> str:
        """Weather."""
        return f"{city}:{units}"

    args = json.loads('{"city": "Paris", "units": null}')

    # Under strict the model sends null; the Python default is NOT substituted.
    assert get_weather(**args) == "Paris:None"


def test_wrapper_applies_default_on_omission_under_non_strict():
    @tool(strict=False)
    def get_weather(city: str, units: str = "celsius") -> str:
        """Weather."""
        return f"{city}:{units}"

    args = json.loads('{"city": "Paris"}')  # non-strict lets the model omit units

    assert get_weather(**args) == "Paris:celsius"
