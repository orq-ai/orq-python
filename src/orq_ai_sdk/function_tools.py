from __future__ import annotations

import dataclasses
import enum
import functools
import inspect
import re
import types
import warnings
from collections.abc import Callable, Iterator, Mapping
from typing import Any, Literal, TypeVar, Union, cast, get_args, get_origin, get_type_hints, overload

from orq_ai_sdk.models.create_router_responseop import ToolsFunction

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


__all__ = [
    "ToolFunctionWrapper",
    "ToolSchemaError",
    "tool",
    "tool_schema",
]
