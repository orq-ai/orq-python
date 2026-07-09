from __future__ import annotations

from enum import Enum
from typing import Literal, Optional

import pytest

from orq_ai_sdk import models, utils
from orq_ai_sdk.function_tools import ToolFunctionWrapper, ToolSchemaError, tool, tool_schema
from orq_ai_sdk.models.create_router_responseop import CreateRouterResponseRequestBody, ToolsFunction


class Tone(str, Enum):
    WARM = "warm"
    COLD = "cold"


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

    schema = tool_schema(describe).model_dump(mode="json", exclude_none=True)
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


def test_tool_schema_marks_only_parameters_without_defaults_as_required():
    def emit_magic_token(reason: str, category: str, retries: int = 0) -> str:
        """Return a token."""

    schema = tool_schema(emit_magic_token).model_dump(mode="json", exclude_none=True)

    assert schema["parameters"]["required"] == ["reason", "category"]


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
    def emit_magic_token(metadata: dict[str, str]) -> str:
        """Return a diagnostic token."""

    with pytest.raises(ToolSchemaError, match="Unsupported annotation"):
        tool_schema(emit_magic_token)
