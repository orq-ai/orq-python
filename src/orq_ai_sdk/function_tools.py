from __future__ import annotations

import dataclasses
import enum
import functools
import inspect
import json
import re
import types
import warnings
from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, Literal, TypeVar, Union, cast, get_args, get_origin, get_type_hints, overload

from orq_ai_sdk.models.create_router_responseop import CreateRouterResponseResponseBody, ToolsFunction

F = TypeVar("F", bound=Callable[..., Any])

_SUPPORTED_SCALAR_TYPES: dict[type[Any], str] = {
    str: "string",
    int: "integer",
    float: "number",
    bool: "boolean",
}

# Function-calling APIs constrain tool names to this character set.
_VALID_TOOL_NAME = re.compile(r"^[a-zA-Z0-9_-]+$")


class ToolSchemaError(TypeError):
    """Raised when a Python callable cannot be converted into a Responses function tool."""


class ToolFunctionWrapper(Mapping[str, Any]):
    """Callable wrapper that also exposes a Mapping payload accepted by the SDK `tools=` field."""

    def __init__(self, func: Callable[..., Any], schema: ToolsFunction) -> None:
        # If re-wrapping an existing tool, point at the underlying function so we
        # don't nest wrappers. `updated=()` stops update_wrapper from copying
        # __dict__, which would otherwise clobber the _schema we just set.
        target = func.raw_function if isinstance(func, ToolFunctionWrapper) else func
        functools.update_wrapper(self, target, updated=())
        self._func = target
        self._schema = schema
        self._payload = schema.model_dump(mode="json", exclude_none=True)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._func(*args, **kwargs)

    def __eq__(self, other: object) -> bool:
        # Identity semantics: two tools that happen to share a schema are still
        # different tools (different callables), so they must not compare equal.
        return self is other

    def __hash__(self) -> int:
        # Restore hashability that Mapping disables (`__hash__ = None`); consistent
        # with the identity __eq__ above.
        return id(self)

    def __getitem__(self, key: str) -> Any:
        return self._payload[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._payload)

    def __len__(self) -> int:
        return len(self._payload)

    @property
    def schema(self) -> dict[str, Any]:
        return dict(self._payload)

    @property
    def raw_function(self) -> Callable[..., Any]:
        return self._func

    @property
    def type(self) -> str:
        return self._schema.type

    @property
    def name(self) -> str:
        return self._schema.name

    @property
    def description(self) -> str | None:
        return self._schema.description

    @property
    def parameters(self) -> dict[str, Any]:
        return dict(self._schema.parameters or {})

    @property
    def strict(self) -> bool | None:
        return self._schema.strict

    def as_tools_function(self) -> ToolsFunction:
        return self._schema


@overload
def tool(func: F, /) -> ToolFunctionWrapper: ...


@overload
def tool(
    func: None = None,
    *,
    name: str | None = None,
    description: str | None = None,
    strict: bool = True,
) -> Callable[[F], ToolFunctionWrapper]: ...


def tool(
    func: F | None = None,
    *,
    name: str | None = None,
    description: str | None = None,
    strict: bool = True,
) -> ToolFunctionWrapper | Callable[[F], ToolFunctionWrapper]:
    """Decorate a callable so it can be passed directly as `tools=[my_tool]`.

    The wrapped object remains callable, but also behaves like a `Mapping`
    containing the JSON payload for a Responses `type="function"` tool. The
    schema is derived from the function's name, docstring and type hints.

    Args:
        name: Override the tool name. Defaults to the function name.
        description: Override the tool description. Defaults to the docstring.
        strict: Emit a strict schema (`additionalProperties: false`). Defaults to True.

    Usage:
        @tool
        def get_weather(city: str) -> str:
            \"\"\"Return the weather for a city.\"\"\"
            ...

        # Override name/description
        @tool(name="weather", description="Look up the weather")
        def get_weather(city: str) -> str:
            ...

        response = client.responses.create(model=..., tools=[get_weather])
    """

    def decorator(inner: F) -> ToolFunctionWrapper:
        return ToolFunctionWrapper(
            inner,
            tool_schema(
                inner,
                name=name,
                description=description,
                strict=strict,
            ),
        )

    if func is None:
        return decorator

    return decorator(func)


def tool_schema(
    func: Callable[..., Any] | ToolFunctionWrapper,
    *,
    name: str | None = None,
    description: str | None = None,
    strict: bool = True,
) -> ToolsFunction:
    """Convert a Python callable into a Responses `ToolsFunction` schema.

    Use this when you need the schema object itself rather than a callable
    wrapper. `@tool` calls this internally.

    Args:
        func: The callable (or an existing `@tool` wrapper) to introspect.
        name: Override the tool name. Defaults to the function name.
        description: Override the tool description. Defaults to the docstring.
        strict: Emit a strict schema (`additionalProperties: false`). Defaults to True.

    Raises:
        ToolSchemaError: If the signature uses an unsupported parameter kind or
            an annotation that cannot be mapped to a JSON schema.
    """

    if isinstance(func, ToolFunctionWrapper):
        existing = func.as_tools_function()
        if name is None and description is None and strict == existing.strict:
            return existing
        # Carry forward the decorator-provided name/description that aren't being
        # overridden, so re-deriving from the raw function doesn't drop them.
        name = name if name is not None else existing.name
        description = description if description is not None else existing.description
        func = func.raw_function

    if not callable(func):
        raise ToolSchemaError(f"Expected a callable, got {type(func).__name__!r}.")

    display_name = getattr(func, "__name__", repr(func))

    if inspect.iscoroutinefunction(func) or inspect.isasyncgenfunction(func):
        raise ToolSchemaError(
            f"{display_name!r} is async; async tool functions are not supported. "
            "Wrap the call in a synchronous function."
        )

    try:
        signature = inspect.signature(func)
        type_hints = get_type_hints(func, include_extras=True)
    except (TypeError, NameError) as exc:
        raise ToolSchemaError(
            f"Could not introspect {display_name!r}: {exc}. functools.partial, "
            "builtins, and locally-scoped annotations are not supported."
        ) from exc

    properties: dict[str, Any] = {}
    required: list[str] = []
    defaulted_params: list[str] = []
    for index, parameter in enumerate(signature.parameters.values()):
        # Skip the implicit receiver of a method decorated directly with @tool.
        if index == 0 and parameter.name in ("self", "cls"):
            continue

        _validate_parameter(parameter)

        if parameter.name not in type_hints:
            raise ToolSchemaError(
                f"Parameter {parameter.name!r} on {display_name!r} is missing a type annotation."
            )

        annotation = type_hints[parameter.name]
        schema = _annotation_to_schema(annotation)
        has_default = parameter.default is not inspect.Signature.empty
        # Only warn about defaults the model can't reach: a `None` default round-trips
        # perfectly (the model sends null → the function receives None), so it isn't lost.
        if has_default and parameter.default is not None:
            defaulted_params.append(parameter.name)
        if has_default and strict:
            # OpenAI strict function-calling requires every property to appear in
            # `required`; optionality is expressed by making the field nullable.
            # (Non-strict schemas may simply omit the key from `required`.)
            schema = _make_nullable(schema)
        properties[parameter.name] = schema
        if strict or not has_default:
            required.append(parameter.name)

    function_name = name or getattr(func, "__name__", None)
    if not function_name:
        raise ToolSchemaError("Callable has no __name__; pass an explicit name=.")
    if not _VALID_TOOL_NAME.match(function_name):
        raise ToolSchemaError(
            f"Tool name {function_name!r} is invalid; names must match "
            f"{_VALID_TOOL_NAME.pattern} (letters, digits, underscore, hyphen). "
            "Pass an explicit name= for lambdas or other unnamed callables."
        )

    if strict and defaulted_params:
        warnings.warn(
            f"Tool {function_name!r} has parameters with defaults "
            f"({', '.join(defaulted_params)}) but strict=True. Under strict "
            "function-calling every parameter is required, so the model must send "
            "a value (or null) and these Python defaults are likely ignored. Pass "
            "strict=False to keep them optional.",
            UserWarning,
            stacklevel=2,
        )
    function_description = description if description is not None else inspect.getdoc(func)
    return ToolsFunction(
        name=function_name,
        type="function",
        description=function_description,
        parameters={
            "type": "object",
            "properties": properties,
            "required": required,
            "additionalProperties": False,
        },
        strict=strict,
    )


def _validate_parameter(parameter: inspect.Parameter) -> None:
    if parameter.kind is inspect.Parameter.POSITIONAL_ONLY:
        raise ToolSchemaError(
            f"Parameter {parameter.name!r} is positional-only; tool parameters must be named."
        )

    if parameter.kind is inspect.Parameter.VAR_POSITIONAL:
        raise ToolSchemaError(
            f"Parameter {parameter.name!r} uses *args, which is not supported for tool schemas."
        )

    if parameter.kind is inspect.Parameter.VAR_KEYWORD:
        raise ToolSchemaError(
            f"Parameter {parameter.name!r} uses **kwargs, which is not supported for tool schemas."
        )


def _make_nullable(schema: dict[str, Any]) -> dict[str, Any]:
    null_schema = {"type": "null"}
    if "anyOf" in schema:
        if null_schema in schema["anyOf"]:
            return schema
        return {"anyOf": [*schema["anyOf"], null_schema]}
    return {"anyOf": [schema, null_schema]}


def _annotation_to_schema(annotation: Any) -> dict[str, Any]:
    # Unwrap Annotated[T, ...]; get_type_hints(include_extras=True) preserves the metadata.
    if hasattr(annotation, "__metadata__"):
        annotation = annotation.__origin__
    # Unwrap NewType("X", int) to its supertype.
    if hasattr(annotation, "__supertype__"):
        annotation = annotation.__supertype__

    origin = get_origin(annotation)

    if annotation in _SUPPORTED_SCALAR_TYPES:
        return {"type": _SUPPORTED_SCALAR_TYPES[cast(type[Any], annotation)]}

    if origin is list:
        args = get_args(annotation)
        if len(args) != 1:
            raise ToolSchemaError("list annotations must declare exactly one item type.")
        return {"type": "array", "items": _annotation_to_schema(args[0])}

    if origin is Literal:
        values = list(get_args(annotation))
        if not values:
            raise ToolSchemaError("Literal annotations must declare at least one value.")
        if None in values:
            non_none = [value for value in values if value is not None]
            if not non_none:
                raise ToolSchemaError("Literal[None] is not a valid tool parameter type.")
            return _make_nullable(_literal_to_schema(non_none))
        return _literal_to_schema(values)

    if origin in (Union, types.UnionType):
        args = get_args(annotation)
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) != 1:
            raise ToolSchemaError(
                "Only Optional[T] (a single type, optionally with None) is supported; "
                "multi-branch unions are not."
            )
        inner = _annotation_to_schema(non_none_args[0])
        return _make_nullable(inner) if type(None) in args else inner

    if inspect.isclass(annotation) and issubclass(annotation, enum.Enum):
        return _enum_to_schema(annotation)

    if _is_model_like(annotation):
        raise ToolSchemaError(
            f"{annotation!r} is a Pydantic model or dataclass; nested object parameters "
            "are not supported. Flatten it into scalar parameters."
        )

    if annotation in (list, dict, set, frozenset, tuple) or origin in (dict, tuple, set, frozenset):
        raise ToolSchemaError(
            f"Annotation {annotation!r} needs a parameterized item type (e.g. list[str]); "
            "bare containers and dict/tuple/set are not supported."
        )

    raise ToolSchemaError(
        f"Unsupported annotation {annotation!r}. "
        "Supported types are str, int, float, bool, list[T], Optional[T], Literal, and Enum."
    )


def _is_model_like(annotation: Any) -> bool:
    if dataclasses.is_dataclass(annotation):
        return True
    try:
        from pydantic import BaseModel  # pylint: disable=import-outside-toplevel
    except ImportError:
        return False
    return inspect.isclass(annotation) and issubclass(annotation, BaseModel)


def _literal_to_schema(values: list[Any]) -> dict[str, Any]:
    value_types = {type(value) for value in values}
    if len(value_types) != 1:
        raise ToolSchemaError("Literal values must all share the same scalar type.")

    value_type = next(iter(value_types))
    if value_type not in _SUPPORTED_SCALAR_TYPES:
        raise ToolSchemaError(
            "Literal values must be str, int, float, or bool for V1 tool schema support."
        )

    return {
        "type": _SUPPORTED_SCALAR_TYPES[cast(type[Any], value_type)],
        "enum": values,
    }


def _enum_to_schema(enum_type: type[enum.Enum]) -> dict[str, Any]:
    values = [member.value for member in enum_type]
    if not values:
        raise ToolSchemaError(f"Enum {enum_type.__name__!r} must declare at least one member.")

    value_types = {type(value) for value in values}
    if len(value_types) != 1:
        raise ToolSchemaError(f"Enum {enum_type.__name__!r} must have homogenous value types.")

    value_type = next(iter(value_types))
    if value_type not in _SUPPORTED_SCALAR_TYPES:
        raise ToolSchemaError(
            f"Enum {enum_type.__name__!r} uses unsupported value type {value_type.__name__!r}."
        )

    return {
        "type": _SUPPORTED_SCALAR_TYPES[cast(type[Any], value_type)],
        "enum": values,
    }


# ---------------------------------------------------------------------------
# Automatic tool-call execution (RES-1096)
# ---------------------------------------------------------------------------

DEFAULT_MAX_TOOL_ITERATIONS = 8

# Kwargs that only apply to the first turn. The loop supplies input and
# previous_response_id itself, and a forced tool_choice ("required" or a named
# function) resent every turn would stop the model from ever answering.
_FIRST_TURN_ONLY = ("input", "previous_response_id", "tool_choice")


class ToolLoopError(RuntimeError):
    """Raised by the tool loop on a bad tool call (unknown tool, malformed call,
    arguments that do not fit the tool, a tool that raised), a response that did not
    complete, or a loop that did not converge. A tool's own exception is chained as
    ``__cause__``; ``response`` is the last response received, if any."""

    def __init__(self, message: str, response: Any = None) -> None:
        super().__init__(message)
        self.response = response


def _item_field(item: Any, key: str) -> Any:
    """Read a field off a response item, which may be a dict or a model."""
    if isinstance(item, Mapping):
        return item.get(key)
    return getattr(item, key, None)


def _prepare_loop(
    tools: Iterable[ToolFunctionWrapper | Mapping[str, Any]],
    max_iterations: int,
    create_kwargs: dict[str, Any],
) -> tuple[list[Any], dict[str, ToolFunctionWrapper], dict[str, Any]]:
    """Validate inputs and build the loop state before any network call."""
    if max_iterations < 1:
        raise ToolLoopError(f"max_iterations must be >= 1, got {max_iterations}")
    if create_kwargs.get("stream"):
        raise ToolLoopError(
            "the tool loop does not support streaming; call responses.create(stream=True) directly"
        )
    if create_kwargs.get("background"):
        raise ToolLoopError("the tool loop does not support background=True; it needs each response to complete")
    if create_kwargs.get("store") is False:
        raise ToolLoopError("the tool loop chains turns with previous_response_id, which requires store=True")
    if create_kwargs.get("conversation") is not None:
        raise ToolLoopError(
            "the tool loop chains turns with previous_response_id, which the router rejects together with conversation"
        )
    # Materialize first so a one-shot iterable is not drained by the registry pass.
    tool_list = list(tools)
    # Only @tool wrappers are executable. Other entries (hosted orq:* tools, mcp) are
    # forwarded as-is: the server runs them, so they never come back as function_call.
    registry: dict[str, ToolFunctionWrapper] = {}
    for t in tool_list:
        if not isinstance(t, ToolFunctionWrapper):
            if _item_field(t, "type") == "function":
                raise ToolLoopError(
                    f"function tool {_item_field(t, 'name')!r} is a plain schema; decorate it with @tool so the loop can run it"
                )
            continue
        if t.name in registry:
            raise ToolLoopError(f"two tools share the name {t.name!r}; tool names must be unique")
        registry[t.name] = t
    if not registry:
        raise ToolLoopError("run the loop with at least one @tool, or call responses.create directly")
    follow = {k: v for k, v in create_kwargs.items() if k not in _FIRST_TURN_ONLY}
    return tool_list, registry, follow


def _pending_function_calls(response: Any) -> list[Any]:
    """Return the function calls to run, or raise if the response did not complete."""
    status = _item_field(response, "status")
    error = _item_field(response, "error")
    if status != "completed" or error:
        detail = error or _item_field(response, "incomplete_details")
        raise ToolLoopError(f"response {_item_field(response, 'id')!r} ended with status {status!r}: {detail}", response)
    return [item for item in (_item_field(response, "output") or []) if _item_field(item, "type") == "function_call"]


def _tool_output_str(result: Any) -> str:
    """Serialize a tool result for the `function_call_output` payload. Values json
    cannot encode (datetimes, custom objects) are stringified in place."""
    if isinstance(result, str):
        return result
    try:
        return json.dumps(result, default=str, allow_nan=False)
    except ValueError as exc:  # circular reference or NaN/inf
        raise ToolLoopError(f"tool result could not be serialized to JSON: {exc}") from exc


@dataclasses.dataclass(frozen=True)
class ToolCallResult:
    """One tool call the loop executed: the model's call and what the tool returned."""

    name: str
    call_id: str
    arguments: dict[str, Any]
    output: str


@dataclasses.dataclass(frozen=True)
class ToolLoopUsage:
    """Token usage summed over every response in the loop. ``total_cost`` is None
    when no response reported a cost."""

    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    total_cost: float | None = None


@dataclasses.dataclass(frozen=True)
class ToolLoopResult:
    """Everything the loop produced since the caller's input.

    ``final`` is the last response. ``output`` is every item in order across all
    turns: each response's output items (messages, reasoning, function calls),
    each followed by the ``function_call_output`` items the loop sent back.
    ``usage`` is summed over all turns; ``final.usage`` covers the last turn only.
    """

    final: CreateRouterResponseResponseBody
    output: list[Any]
    tool_results: list[ToolCallResult]
    usage: ToolLoopUsage


def _execute_calls(calls: list[Any], registry: Mapping[str, ToolFunctionWrapper], response: Any) -> list[ToolCallResult]:
    """Run each function call against its registered tool. Every failure is a ``ToolLoopError``."""
    results: list[ToolCallResult] = []
    for call in calls:
        name = _item_field(call, "name")
        call_id = _item_field(call, "call_id")
        if not call_id:
            raise ToolLoopError(f"function_call for tool {name!r} has no call_id", response)
        fn = registry.get(name)
        if fn is None:
            raise ToolLoopError(f"the model called tool {name!r}, which was not passed to the loop", response)
        raw = _item_field(call, "arguments")
        try:
            args = json.loads(raw) if raw else {}
        except (TypeError, ValueError) as exc:
            raise ToolLoopError(f"tool {name!r} arguments were not valid JSON: {raw!r}", response) from exc
        if not isinstance(args, dict):
            raise ToolLoopError(f"tool {name!r} arguments must be a JSON object, got {type(args).__name__}", response)
        try:
            inspect.signature(fn).bind(**args)
        except TypeError as exc:
            raise ToolLoopError(f"tool {name!r} arguments do not match its signature: {exc}", response) from exc
        try:
            result = fn(**args)
        except Exception as exc:  # noqa: BLE001 - surface any tool failure with loop context
            raise ToolLoopError(f"tool {name!r} raised while executing: {exc}", response) from exc
        results.append(ToolCallResult(name, call_id, args, _tool_output_str(result)))
    return results


class _Transcript:
    """Collects every turn so the caller gets more than the last response."""

    def __init__(self, registry: Mapping[str, ToolFunctionWrapper]) -> None:
        self._registry = registry
        self.output: list[Any] = []
        self.tool_results: list[ToolCallResult] = []
        self._usage = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        self._cost: float | None = None

    def record(self, response: Any) -> list[Any]:
        """Add a response's items and usage; return its pending function calls."""
        calls = _pending_function_calls(response)
        self.output.extend(_item_field(response, "output") or [])
        usage = _item_field(response, "usage")
        if usage is not None:
            for key in self._usage:
                self._usage[key] += _item_field(usage, key) or 0
            cost = _item_field(usage, "total_cost")
            if cost is not None:
                self._cost = (self._cost or 0.0) + cost
        return calls

    def execute(self, calls: list[Any], response: Any) -> list[dict[str, Any]]:
        """Run the calls and return the ``function_call_output`` items to resubmit."""
        results = _execute_calls(calls, self._registry, response)
        self.tool_results.extend(results)
        items = [{"type": "function_call_output", "call_id": r.call_id, "output": r.output} for r in results]
        self.output.extend(items)
        return items

    def result(self, final: Any) -> ToolLoopResult:
        return ToolLoopResult(final, self.output, self.tool_results, ToolLoopUsage(**self._usage, total_cost=self._cost))


def run_tool_loop(
    client: Any,
    tools: Iterable[ToolFunctionWrapper | Mapping[str, Any]],
    *,
    max_iterations: int = DEFAULT_MAX_TOOL_ITERATIONS,
    **create_kwargs: Any,
) -> ToolLoopResult:
    """Call ``responses.create`` and auto-execute function tool calls until done.

    Passes ``tools`` on every turn, runs each ``function_call`` against the matching
    ``@tool``, resubmits the results as ``function_call_output`` items with
    ``previous_response_id``, and repeats until the model stops calling tools or
    ``max_iterations`` tool rounds are used. Returns a :class:`ToolLoopResult` with
    the final response, every output item across turns, the executed tool calls
    and summed usage. Non-``@tool`` entries in ``tools`` (hosted tools) are
    forwarded unchanged. ``input``, ``previous_response_id`` and ``tool_choice``
    apply to the first turn only; ``stream``, ``background``, ``store=False`` and
    ``conversation`` are rejected. Raises ``ToolLoopError`` on a bad tool call, a
    response that did not complete, or a loop that does not converge.

    Security: the loop runs your registered tools with model-chosen arguments and
    sends their return values to the model. Validate inside the tool and do not
    return secrets.
    """
    # A free function, not a client method: this hand-written module survives Speakeasy regen.
    tool_list, registry, follow = _prepare_loop(tools, max_iterations, create_kwargs)
    transcript = _Transcript(registry)
    response = client.responses.create(tools=tool_list, **create_kwargs)
    for _ in range(max_iterations):
        calls = transcript.record(response)
        if not calls:
            return transcript.result(response)
        response = client.responses.create(
            input=transcript.execute(calls, response),
            previous_response_id=_item_field(response, "id"),
            tools=tool_list,
            **follow,
        )
    if transcript.record(response):
        raise ToolLoopError(f"tool loop still calling tools after {max_iterations} rounds", response)
    return transcript.result(response)


async def run_tool_loop_async(
    client: Any,
    tools: Iterable[ToolFunctionWrapper | Mapping[str, Any]],
    *,
    max_iterations: int = DEFAULT_MAX_TOOL_ITERATIONS,
    **create_kwargs: Any,
) -> ToolLoopResult:
    """Async form of :func:`run_tool_loop`, using ``responses.create_async``.
    ``@tool`` functions are synchronous and run inline, so a slow tool still blocks
    the event loop; offload heavy work inside the tool yourself.
    """
    tool_list, registry, follow = _prepare_loop(tools, max_iterations, create_kwargs)
    transcript = _Transcript(registry)
    response = await client.responses.create_async(tools=tool_list, **create_kwargs)
    for _ in range(max_iterations):
        calls = transcript.record(response)
        if not calls:
            return transcript.result(response)
        response = await client.responses.create_async(
            input=transcript.execute(calls, response),
            previous_response_id=_item_field(response, "id"),
            tools=tool_list,
            **follow,
        )
    if transcript.record(response):
        raise ToolLoopError(f"tool loop still calling tools after {max_iterations} rounds", response)
    return transcript.result(response)


__all__ = [
    "ToolCallResult",
    "ToolFunctionWrapper",
    "ToolLoopError",
    "ToolLoopResult",
    "ToolLoopUsage",
    "ToolSchemaError",
    "run_tool_loop",
    "run_tool_loop_async",
    "tool",
    "tool_schema",
]
