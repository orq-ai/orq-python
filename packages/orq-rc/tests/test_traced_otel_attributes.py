"""Attributes @traced writes on its OpenTelemetry span when a global SDK provider is set."""

import enum
import json
from unittest.mock import MagicMock

import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.trace import StatusCode
from opentelemetry.util._once import Once

from orq_ai_sdk.traced.config import Config, set_config
from orq_ai_sdk.traced.context import current_span
from orq_ai_sdk.traced.decorators import traced
from orq_ai_sdk.traced.span import Span
from orq_ai_sdk.traced.utils import to_json_safe


@pytest.fixture
def exporter():
    """Install a real global TracerProvider, then restore OTel's unset global state."""
    set_config(Config(api_key="test-key", enabled=True))
    memory = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(memory))
    trace.set_tracer_provider(provider)
    yield memory
    provider.shutdown()
    # OTel allows setting the global provider once per process; reset it so
    # other test modules keep exercising the non-OTel path.
    trace._TRACER_PROVIDER_SET_ONCE = Once()  # pylint: disable=protected-access
    trace._TRACER_PROVIDER = None  # pylint: disable=protected-access
    set_config(Config(enabled=False))


def _only_span(memory):
    spans = memory.get_finished_spans()
    assert len(spans) == 1
    return dict(spans[0].attributes)


class Opaque:
    __slots__ = ()

    def __repr__(self):
        return "<Opaque>"


def test_input_and_output_are_json(exporter):
    @traced(name="run", type="agent")
    def run(question, limit=180):
        return {"stale": ["u-002"], "limit": limit}

    run("Which accounts are stale?")
    attrs = _only_span(exporter)

    assert attrs["type"] == "agent"
    assert json.loads(attrs["input"]) == {"question": "Which accounts are stale?", "limit": 180}
    assert json.loads(attrs["output"]) == {"stale": ["u-002"], "limit": 180}
    # Function args are not chat messages; the backend derives these keys itself.
    assert "gen_ai.input.messages" not in attrs
    assert "gen_ai.output.messages" not in attrs
    assert "gen_ai.tool.call.arguments" not in attrs


def test_string_output_is_kept_verbatim(exporter):
    @traced
    def answer():
        return "u-002 is stale"

    answer()
    attrs = _only_span(exporter)

    assert attrs["output"] == "u-002 is stale"


def test_tool_span_sets_tool_call_arguments_and_result(exporter):
    @traced(type="tool")
    def lookup(user_id):
        return {"user_id": user_id, "role": "approver"}

    lookup("u-002")
    attrs = _only_span(exporter)

    assert json.loads(attrs["gen_ai.tool.call.arguments"]) == {"user_id": "u-002"}
    assert json.loads(attrs["gen_ai.tool.call.result"]) == {"user_id": "u-002", "role": "approver"}


def test_unserializable_values_fall_back_to_repr(exporter):
    @traced
    def handle(thing):
        return thing

    handle(Opaque())
    attrs = _only_span(exporter)

    assert json.loads(attrs["input"]) == {"thing": "<Opaque>"}



def test_error_span_keeps_input_without_output(exporter):
    @traced
    def failing(user_id):
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        failing("u-002")
    attrs = _only_span(exporter)

    assert json.loads(attrs["input"]) == {"user_id": "u-002"}
    assert "output" not in attrs


def test_capture_flags_disable_io_attributes(exporter):
    @traced(capture_input=False, capture_output=False)
    def quiet(secret):
        return secret

    quiet("hunter2")
    attrs = _only_span(exporter)

    for key in ("input", "output"):
        assert key not in attrs


def test_span_log_dicts_become_dotted_keys(exporter):
    @traced(type="llm", attributes={"tenant": "acme", "tags": ["audit", "q4"]})
    def generate():
        current_span().log(
            metrics={
                "prompt_tokens": 76,
                "completion_tokens": 425,
                "tokens": 501,
                "completion_tokens_details": {"reasoning_tokens": 412},
            },
            request={"provider": "anthropic", "model": "claude-haiku-5-5", "temperature": 0.2},
            metadata={"thing": Opaque(), "cached": False, "skipped": None},
        )
        return "ok"

    generate()
    attrs = _only_span(exporter)

    assert attrs["gen_ai.usage.input_tokens"] == 76
    assert attrs["gen_ai.usage.output_tokens"] == 425
    assert attrs["metrics.tokens"] == 501
    assert attrs["gen_ai.usage.reasoning.output_tokens"] == 412
    assert attrs["gen_ai.provider.name"] == "anthropic"
    assert attrs["gen_ai.request.model"] == "claude-haiku-5-5"
    assert attrs["gen_ai.request.temperature"] == 0.2
    assert attrs["metadata.thing"] == "<Opaque>"
    assert attrs["metadata.cached"] is False
    assert "metadata.skipped" not in attrs
    for whole in ("metrics", "request", "metadata"):
        assert whole not in attrs
    assert attrs["tenant"] == "acme"
    assert json.loads(attrs["tags"]) == ["audit", "q4"]
    assert attrs["status"] == "success"



class Env(str, enum.Enum):
    PROD = "prod"


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None


def _cyclic():
    d = {"a": 1}
    d["self"] = d
    return d


def _linked():
    n, m = Node("n"), Node("m")
    n.parent, m.parent = m, n
    return n


def _only_finished_span(memory):
    spans = memory.get_finished_spans()
    assert len(spans) == 1
    return spans[0]


@pytest.mark.parametrize(
    "log_kwargs, key, expected",
    [
        ({"input": _cyclic()}, "input", {"a": 1, "self": "[Circular]"}),
        ({"output": {(1, 2): "v"}}, "output", {"(1, 2)": "v"}),
        ({"metadata": {"env": Env.PROD}}, "metadata.env", "prod"),
        ({"metadata": _cyclic()}, "metadata.self", "[Circular]"),
        ({"metadata": {"node": _linked()}}, "metadata.node.parent.parent", "[Circular]"),
    ],
)
@pytest.mark.parametrize("raises", [False, True])
def test_unencodable_values_keep_status_and_attributes(exporter, log_kwargs, key, expected, raises):
    @traced(type="tool", attributes={"tenant": "acme"}, capture_output=False)
    def work(user_id):
        current_span().log(**log_kwargs)
        if raises:
            raise RuntimeError("boom")
        return "ok"

    if raises:
        with pytest.raises(RuntimeError):
            work("u-002")
    else:
        work("u-002")
    span = _only_finished_span(exporter)
    attrs = dict(span.attributes)

    if raises:
        assert span.status.status_code == StatusCode.ERROR
        assert [event.name for event in span.events] == ["exception"]
    else:
        assert span.status.status_code == StatusCode.OK
    assert attrs["tenant"] == "acme"
    assert attrs["type"] == "tool"
    value = attrs[key]
    assert (json.loads(value) if key in ("input", "output") else value) == expected


def test_to_json_safe_never_raises():
    class BadStr:
        __slots__ = ()

        def __str__(self):
            raise RuntimeError("no")

    deep = current = {}
    for _ in range(100):
        current["c"] = {}
        current = current["c"]

    assert to_json_safe(BadStr()) == "<unrepresentable BadStr>"
    assert json.dumps(to_json_safe(deep)).count("[MaxDepth]") == 1
    assert to_json_safe({Env.PROD: {1, 2}, (1, 2): "t", 3: "i"}) == {"prod": [1, 2], "(1, 2)": "t", "3": "i"}


@pytest.mark.parametrize(
    "span_type, operation",
    [("agent", "invoke_agent"), ("llm", "chat"), ("tool", "execute_tool"),
     ("retrieval", "retrieval"), ("embedding", "embeddings"), ("function", None)],
)
def test_span_type_maps_to_genai_operation_name(exporter, span_type, operation):
    @traced(name="step", type=span_type)
    def step():
        return "ok"

    step()
    attrs = _only_span(exporter)

    assert attrs["type"] == span_type
    assert attrs.get("gen_ai.operation.name") == operation


def test_agent_and_tool_spans_carry_semconv_names(exporter):
    @traced(name="lookup", type="tool")
    def lookup(user_id):
        return {"user_id": user_id}

    @traced(name="planner", type="agent")
    def planner():
        return lookup("u-002")

    planner()
    by_name = {s.name: dict(s.attributes) for s in exporter.get_finished_spans()}

    assert by_name["planner"]["gen_ai.agent.name"] == "planner"
    assert "gen_ai.tool.name" not in by_name["planner"]
    assert by_name["lookup"]["gen_ai.tool.name"] == "lookup"
    assert by_name["lookup"]["gen_ai.tool.type"] == "function"
    assert json.loads(by_name["lookup"]["gen_ai.tool.call.arguments"]) == {"user_id": "u-002"}


def test_span_log_usage_and_request_get_semconv_names(exporter):
    @traced(type="llm")
    def generate():
        current_span().log(
            metrics={
                "prompt_tokens": 76,
                "completion_tokens": 425,
                "tokens": 501,
                "prompt_tokens_details": {"cached_tokens": 12},
                "completion_tokens_details": {"reasoning_tokens": 412},
            },
            request={"provider": "anthropic", "model": "claude-haiku-5-5", "max_tokens": 2000,
                     "temperature": 0.2, "seed": "not-an-int"},
        )
        return "ok"

    generate()
    attrs = _only_span(exporter)

    assert attrs["gen_ai.usage.input_tokens"] == 76
    assert attrs["gen_ai.usage.output_tokens"] == 425
    assert attrs["gen_ai.usage.cache_read.input_tokens"] == 12
    assert attrs["gen_ai.usage.reasoning.output_tokens"] == 412
    assert attrs["gen_ai.provider.name"] == "anthropic"
    assert attrs["gen_ai.request.model"] == "claude-haiku-5-5"
    assert attrs["gen_ai.request.max_tokens"] == 2000
    assert attrs["gen_ai.request.temperature"] == 0.2
    # Orq bills cached/reasoning tokens from the *_tokens_details keys.
    assert attrs["gen_ai.usage.prompt_tokens_details.cached_tokens"] == 12
    assert attrs["gen_ai.usage.completion_tokens_details.reasoning_tokens"] == 412
    # Renamed keys are not also written under their span.log() name.
    for old in ("metrics.prompt_tokens", "metrics.completion_tokens", "request.model",
                "metrics.prompt_tokens_details.cached_tokens"):
        assert old not in attrs
    # Semconv types seed as int, so a string seed keeps its own key.
    assert attrs["request.seed"] == "not-an-int"
    assert "gen_ai.request.seed" not in attrs


def test_explicit_semconv_attributes_are_kept(exporter):
    @traced(type="llm", attributes={
        "gen_ai.usage.input_tokens": 10,
        "gen_ai.usage.cache_read.input_tokens": 4,
        "gen_ai.request.model": "gpt-5",
        "request.model": "gpt-5-mini",
        "gen_ai.operation.name": "text_completion",
    })
    def generate():
        return "ok"

    generate()
    attrs = _only_span(exporter)

    assert attrs["gen_ai.usage.input_tokens"] == 10
    assert "metrics.prompt_tokens" not in attrs
    assert attrs["gen_ai.usage.prompt_tokens_details.cached_tokens"] == 4
    # Both names already set: neither is overwritten.
    assert attrs["request.model"] == "gpt-5-mini"
    assert attrs["gen_ai.request.model"] == "gpt-5"
    assert attrs["gen_ai.operation.name"] == "text_completion"


class QuotaExceeded(Exception):
    pass


@pytest.mark.parametrize("error, expected", [
    (RuntimeError("boom"), "RuntimeError"),
    (QuotaExceeded("over"), f"{__name__}.QuotaExceeded"),
])
def test_error_span_sets_error_type(exporter, error, expected):
    @traced(type="tool")
    def failing():
        raise error

    with pytest.raises(type(error)):
        failing()
    attrs = _only_span(exporter)

    assert attrs["error.type"] == expected
    assert attrs["error.message"] == str(error)


def test_cyclic_argument_and_return_value_are_captured(exporter):
    @traced(type="function")
    def echo(payload):
        return payload

    echo(_cyclic())
    attrs = _only_span(exporter)

    assert json.loads(attrs["input"]) == {"payload": {"a": 1, "self": "[Circular]"}}
    assert json.loads(attrs["output"]) == {"a": 1, "self": "[Circular]"}


def test_non_otel_span_dict_never_raises():
    set_config(Config(api_key="test-key", enabled=True))
    try:
        span = Span(trace_id="0" * 31 + "1", span_id="0" * 15 + "1", name="no-otel")
        span.set_attribute("loop", _cyclic())
        span.set_input(_cyclic())
        payload = span.to_dict()
    finally:
        set_config(Config(enabled=False))

    assert payload["attributes"]["loop.a"] == 1
    assert payload["attributes"]["loop.self"] == "[Circular]"
    json.dumps(payload["input"], allow_nan=False)


def test_non_finite_floats_and_big_ints_stay_valid(exporter):
    @traced(type="function")
    def stats():
        current_span().log(metrics={"score": float("nan"), "count": 2 ** 70})
        return {"ratio": float("inf")}

    stats()
    attrs = _only_span(exporter)

    assert json.loads(attrs["output"]) == {"ratio": "inf"}
    assert attrs["metrics.score"] == "nan"
    assert attrs["metrics.count"] == str(2 ** 70)


def test_wrongly_typed_usage_keeps_its_span_log_key(exporter):
    @traced(type="llm")
    def generate():
        current_span().log(metrics={"prompt_tokens": "76", "completion_tokens": 425})
        return "ok"

    generate()
    attrs = _only_span(exporter)

    assert attrs["metrics.prompt_tokens"] == "76"
    assert "gen_ai.usage.input_tokens" not in attrs
    assert attrs["gen_ai.usage.output_tokens"] == 425


def _workload():
    """An agent calling an llm, a tool and a failing function."""

    @traced(type="llm", name="generate")
    def generate():
        current_span().log(
            metrics={"prompt_tokens": 76, "completion_tokens": 425, "prompt_tokens_details": {"cached_tokens": 64}},
            request={"provider": "openai", "model": "gpt-4o", "temperature": 0.2},
            metadata={"tags": ["a", "b"]},
        )
        return "ok"

    @traced(type="tool", name="lookup")
    def lookup(city):
        return {"city": city}

    @traced(name="fails")
    def fails():
        raise ValueError("boom")

    @traced(type="agent", name="planner")
    def planner():
        generate()
        lookup("Amsterdam")
        try:
            fails()
        except ValueError:
            pass

    planner()


def test_http_path_sends_the_same_attributes_as_otel(exporter, monkeypatch):
    _workload()
    otel = {
        span.name: {k: v for k, v in span.attributes.items() if k not in ("input", "output")}
        for span in exporter.get_finished_spans()
    }

    monkeypatch.setattr(trace, "_TRACER_PROVIDER", None)
    monkeypatch.setattr(trace, "_TRACER_PROVIDER_SET_ONCE", Once())
    submitted = []
    client = MagicMock()
    client.submit_span.side_effect = submitted.append
    monkeypatch.setattr("orq_ai_sdk.traced.decorators.get_client", lambda: client)
    _workload()
    http = {span.name: span.to_dict()["attributes"] for span in submitted}

    assert http == otel
    assert http["generate"]["gen_ai.usage.input_tokens"] == 76
    assert http["generate"]["gen_ai.usage.prompt_tokens_details.cached_tokens"] == 64
    assert "metrics.prompt_tokens" not in http["generate"]
    assert http["fails"]["error.type"] == "ValueError"
