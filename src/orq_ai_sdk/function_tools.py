from __future__ import annotations

import enum
import functools
import inspect
import types
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


class ToolSchemaError(TypeError):
    """Raised when a Python callable cannot be converted into a Responses function tool."""


class ToolFunctionWrapper(Mapping[str, Any]):
    """Callable wrapper that also exposes a Mapping payload accepted by the SDK `tools=` field."""

    def __init__(self, func: Callable[..., Any], schema: ToolsFunction) -> None:
        self._func = func
        self._schema = schema
        self._payload = schema.model_dump(mode="json", exclude_none=True)
        functools.update_wrapper(self, func)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._func(*args, **kwargs)

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
        return dict(self._schema.parameters)

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
    containing the JSON payload for a Responses `type="function"` tool.
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
    """Convert a Python callable into a Responses `ToolsFunction` schema."""

    if isinstance(func, ToolFunctionWrapper):
        if name is None and description is None:
            return func.as_tools_function()
        func = func.raw_function

    if not callable(func):
        raise ToolSchemaError(f"Expected a callable, got {type(func).__name__!r}.")

    signature = inspect.signature(func)
    type_hints = get_type_hints(func, include_extras=True)

    properties: dict[str, Any] = {}
    required: list[str] = []
    for parameter in signature.parameters.values():
        _validate_parameter(parameter)

        if parameter.name not in type_hints:
            raise ToolSchemaError(
                f"Parameter {parameter.name!r} on {func.__name__!r} is missing a type annotation."
            )

        annotation = type_hints[parameter.name]
        properties[parameter.name] = _annotation_to_schema(annotation)
        if parameter.default is inspect.Signature.empty:
            required.append(parameter.name)

    function_name = name or func.__name__
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


def _annotation_to_schema(annotation: Any) -> dict[str, Any]:
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
        return _literal_to_schema(values)

    if _is_optional_union(annotation):
        non_none_args = [arg for arg in get_args(annotation) if arg is not type(None)]
        if len(non_none_args) != 1:
            raise ToolSchemaError(
                "Only Optional[T] unions are supported. Nested or multi-branch unions are not."
            )
        return {
            "anyOf": [
                _annotation_to_schema(non_none_args[0]),
                {"type": "null"},
            ],
        }

    if inspect.isclass(annotation) and issubclass(annotation, enum.Enum):
        return _enum_to_schema(annotation)

    raise ToolSchemaError(
        f"Unsupported annotation {annotation!r}. "
        "Supported types are str, int, float, bool, list[T], Optional[T], Literal, and Enum."
    )


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


def _is_optional_union(annotation: Any) -> bool:
    origin = get_origin(annotation)
    if origin not in (Union, types.UnionType):
        return False
    args = get_args(annotation)
    return any(arg is type(None) for arg in args)


__all__ = [
    "ToolFunctionWrapper",
    "ToolSchemaError",
    "tool",
    "tool_schema",
]
