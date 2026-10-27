from __future__ import annotations

import asyncio
import json
import warnings
from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Literal, NewType, Optional

import pytest
from pydantic import BaseModel

from orq_ai_sdk import models, utils
from orq_ai_sdk.function_tools import (
    ToolFunctionWrapper,
    ToolLoopError,
    ToolSchemaError,
    run_tool_loop,
    run_tool_loop_async,
    tool,
    tool_schema,
)
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


# ---------------------------------------------------------------------------
# Automatic tool-call execution (RES-1096)
# ---------------------------------------------------------------------------


class _FakeCall:
    """A function_call output item (object form, like a deserialized model)."""

    type = "function_call"

    def __init__(self, name: str, arguments: str, call_id: str) -> None:
        self.name, self.arguments, self.call_id = name, arguments, call_id


class _FakeResp:
    def __init__(self, output, id, status="completed", error=None):  # noqa: A002 - mirrors the SDK field name
        self.output, self.id, self.status, self.error = output, id, status, error
        self.incomplete_details = None


class _FakeResponses:
    def __init__(self, script):
        self._script = list(script)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self._script.pop(0)

    async def create_async(self, **kwargs):
        self.calls.append(kwargs)
        return self._script.pop(0)


class _FakeClient:
    def __init__(self, script):
        self.responses = _FakeResponses(script)


def test_run_tool_loop_executes_and_resubmits():
    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 2, "b": 3}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),  # dict item, no tool call -> done
    ])
    final = run_tool_loop(client, [add], model="m", input="2+3?")

    assert final.id == "r2"
    assert len(client.responses.calls) == 2
    resubmit = client.responses.calls[1]
    assert resubmit["previous_response_id"] == "r1"
    assert resubmit["input"] == [{"type": "function_call_output", "call_id": "c1", "output": "5"}]
    assert resubmit["model"] == "m"  # model carried over, only the original input dropped


def test_run_tool_loop_accepts_caller_previous_response_id():
    """A caller continuing a conversation passes previous_response_id; the loop must
    not collide with its own per-round previous_response_id (it would TypeError)."""

    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 2, "b": 3}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    final = run_tool_loop(client, [add], model="m", input="2+3?", previous_response_id="seed")

    assert final.id == "r2"
    # First turn uses the caller's seed; the resubmit uses the loop's latest id, not the seed.
    assert client.responses.calls[0]["previous_response_id"] == "seed"
    assert client.responses.calls[1]["previous_response_id"] == "r1"


def test_run_tool_loop_errors_on_unregistered_tool():
    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    client = _FakeClient([_FakeResp([_FakeCall("subtract", "{}", "c1")], "r1")])
    with pytest.raises(ToolLoopError, match="not passed to the loop"):
        run_tool_loop(client, [add], model="m", input="x")


def test_run_tool_loop_caps_iterations():
    @tool
    def ping() -> str:
        """Ping."""
        return "pong"

    class _AlwaysCalls:
        def __init__(self):
            self.calls: list[dict] = []

        def create(self, **kwargs):
            self.calls.append(kwargs)
            return _FakeResp([_FakeCall("ping", "{}", "c")], "r")

    client = type("C", (), {"responses": _AlwaysCalls()})()
    with pytest.raises(ToolLoopError, match="still calling tools after 2 rounds"):
        run_tool_loop(client, [ping], max_iterations=2, model="m", input="x")


def test_run_tool_loop_async_uses_the_async_client():
    # @tool functions are synchronous (the decorator rejects async), so the async
    # loop exists for the async client: it drives create_async, tools run inline.
    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 4, "b": 5}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    final = asyncio.run(run_tool_loop_async(client, [add], model="m", input="4+5?"))

    assert final.id == "r2"
    assert len(client.responses.calls) == 2  # both turns went through create_async
    assert client.responses.calls[1]["input"] == [
        {"type": "function_call_output", "call_id": "c1", "output": "9"}
    ]


def _adder():
    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    return add


def test_run_tool_loop_accepts_a_generator_of_tools():
    # A one-shot iterable must not be drained by the registry pass and then re-read
    # as an empty tool list; the tools must still reach every turn.
    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    final = run_tool_loop(client, (t for t in [_adder()]), model="m", input="1+1?")
    assert final.id == "r2"
    assert client.responses.calls[0]["tools"]  # tools were sent, not an empty list


def test_run_tool_loop_resolves_within_the_exact_round_budget():
    # max_iterations counts tool rounds; two rounds must resolve with max_iterations=2,
    # not raise (the final no-call response is returned, not discarded).
    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1"),
        _FakeResp([_FakeCall("add", '{"a": 2, "b": 2}', "c2")], "r2"),
        _FakeResp([{"type": "message"}], "r3"),
    ])
    final = run_tool_loop(client, [_adder()], max_iterations=2, model="m", input="go")
    assert final.id == "r3"


def test_run_tool_loop_rejects_streaming():
    client = _FakeClient([_FakeResp([{"type": "message"}], "r1")])
    with pytest.raises(ToolLoopError, match="does not support streaming"):
        run_tool_loop(client, [_adder()], model="m", input="x", stream=True)


def test_run_tool_loop_rejects_empty_tools():
    client = _FakeClient([_FakeResp([{"type": "message"}], "r1")])
    with pytest.raises(ToolLoopError, match="at least one @tool"):
        run_tool_loop(client, [], model="m", input="x")


def test_run_tool_loop_rejects_non_positive_max_iterations():
    client = _FakeClient([_FakeResp([{"type": "message"}], "r1")])
    with pytest.raises(ToolLoopError, match="max_iterations must be >= 1"):
        run_tool_loop(client, [_adder()], max_iterations=0, model="m", input="x")


def test_run_tool_loop_rejects_duplicate_tool_names():
    client = _FakeClient([_FakeResp([{"type": "message"}], "r1")])
    with pytest.raises(ToolLoopError, match="share the name"):
        run_tool_loop(client, [_adder(), _adder()], model="m", input="x")


def test_run_tool_loop_rejects_non_object_arguments():
    client = _FakeClient([_FakeResp([_FakeCall("add", "[1, 2]", "c1")], "r1")])
    with pytest.raises(ToolLoopError, match="must be a JSON object"):
        run_tool_loop(client, [_adder()], model="m", input="x")


def test_run_tool_loop_wraps_a_tool_exception():
    @tool
    def boom(x: int) -> int:
        """Always fails."""
        raise ValueError("kaboom")

    client = _FakeClient([_FakeResp([_FakeCall("boom", '{"x": 1}', "c1")], "r1")])
    with pytest.raises(ToolLoopError, match="raised while executing") as exc:
        run_tool_loop(client, [boom], model="m", input="x")
    assert isinstance(exc.value.__cause__, ValueError)  # original chained


def test_run_tool_loop_sends_tool_choice_on_the_first_turn_only():
    # A forced tool_choice resent every turn would make the model call tools forever.
    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    final = run_tool_loop(client, [_adder()], model="m", input="x", tool_choice="required")
    assert final.id == "r2"
    assert client.responses.calls[0]["tool_choice"] == "required"
    assert "tool_choice" not in client.responses.calls[1]


def test_run_tool_loop_forwards_hosted_tools_unregistered():
    hosted = {"type": "orq:web_search"}
    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    add = _adder()
    run_tool_loop(client, [add, hosted], model="m", input="x")
    assert client.responses.calls[1]["tools"] == [add, hosted]


def test_run_tool_loop_rejects_plain_function_schema_before_any_call():
    client = _FakeClient([])
    plain = {"type": "function", "name": "add", "parameters": {}}
    with pytest.raises(ToolLoopError, match="decorate it with @tool"):
        run_tool_loop(client, [_adder(), plain], model="m", input="x")
    assert client.responses.calls == []


def test_run_tool_loop_rejects_only_hosted_tools():
    with pytest.raises(ToolLoopError, match="at least one @tool"):
        run_tool_loop(_FakeClient([]), [{"type": "orq:web_search"}], model="m", input="x")


@pytest.mark.parametrize("kwargs", [{"background": True}, {"store": False}, {"conversation": {"id": "conv_1"}}])
def test_run_tool_loop_rejects_kwargs_that_break_chaining(kwargs):
    client = _FakeClient([])
    with pytest.raises(ToolLoopError):
        run_tool_loop(client, [_adder()], model="m", input="x", **kwargs)
    assert client.responses.calls == []


@pytest.mark.parametrize("status", ["failed", "incomplete", "queued", "in_progress"])
def test_run_tool_loop_raises_on_a_response_that_did_not_complete(status):
    # Tools must not run on (possibly truncated) calls from an unfinished response,
    # and a failed response must not be returned as if the loop finished.
    ran = []

    @tool
    def add(a: int, b: int) -> int:
        """Add two integers."""
        ran.append((a, b))
        return a + b

    resp = _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1", status=status)
    with pytest.raises(ToolLoopError, match=status) as exc:
        run_tool_loop(_FakeClient([resp]), [add], model="m", input="x")
    assert ran == []
    assert exc.value.response is resp


def test_run_tool_loop_raises_on_a_response_error():
    resp = _FakeResp([], "r1", error={"code": "server_error"})
    with pytest.raises(ToolLoopError, match="server_error"):
        run_tool_loop(_FakeClient([resp]), [_adder()], model="m", input="x")


def test_run_tool_loop_rejects_a_call_without_call_id():
    client = _FakeClient([_FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "")], "r1")])
    with pytest.raises(ToolLoopError, match="no call_id"):
        run_tool_loop(client, [_adder()], model="m", input="x")


def test_run_tool_loop_rejects_invalid_json_arguments():
    client = _FakeClient([_FakeResp([_FakeCall("add", '{"a": 1,', "c1")], "r1")])
    with pytest.raises(ToolLoopError, match="not valid JSON"):
        run_tool_loop(client, [_adder()], model="m", input="x")


def test_run_tool_loop_reports_mismatched_arguments_separately_from_tool_errors():
    client = _FakeClient([_FakeResp([_FakeCall("add", '{"a": 1, "c": 2}', "c1")], "r1")])
    with pytest.raises(ToolLoopError, match="do not match its signature"):
        run_tool_loop(client, [_adder()], model="m", input="x")


def test_run_tool_loop_serializes_non_json_results_as_valid_json():
    import datetime

    @tool
    def when() -> dict:
        """Return a timestamp."""
        return {"at": datetime.datetime(2026, 1, 1)}

    client = _FakeClient([
        _FakeResp([_FakeCall("when", "{}", "c1")], "r1"),
        _FakeResp([{"type": "message"}], "r2"),
    ])
    run_tool_loop(client, [when], model="m", input="x")
    assert json.loads(client.responses.calls[1]["input"][0]["output"]) == {"at": "2026-01-01 00:00:00"}


def test_run_tool_loop_async_raises_on_non_convergence():
    client = _FakeClient([
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c1")], "r1"),
        _FakeResp([_FakeCall("add", '{"a": 1, "b": 1}', "c2")], "r2"),
    ])
    with pytest.raises(ToolLoopError, match="after 1 rounds") as exc:
        asyncio.run(run_tool_loop_async(client, [_adder()], max_iterations=1, model="m", input="x"))
    assert exc.value.response.id == "r2"
