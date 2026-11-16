"""Attributes @traced writes on its OpenTelemetry span when a global SDK provider is set."""

import enum
import json

import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.trace import StatusCode
from opentelemetry.util._once import Once

from orq_ai_sdk.traced.config import Config, set_config
from orq_ai_sdk.traced.context import current_span
from orq_ai_sdk.traced.constants import MAX_ATTRIBUTE_VALUE_CHARS, TRUNCATION_MARKER
from orq_ai_sdk.traced.decorators import traced
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


def test_oversized_output_is_truncated(exporter):
    @traced
    def big():
        return "x" * (MAX_ATTRIBUTE_VALUE_CHARS * 2)

    big()
    attrs = _only_span(exporter)

    assert len(attrs["output"]) == MAX_ATTRIBUTE_VALUE_CHARS
    assert attrs["output"].endswith(TRUNCATION_MARKER)


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

    # Keys the Orq ingest reads for usage and model (orqtraced.go extractUsage).
    assert attrs["metrics.prompt_tokens"] == 76
    assert attrs["metrics.completion_tokens"] == 425
    assert attrs["metrics.tokens"] == 501
    assert attrs["metrics.completion_tokens_details.reasoning_tokens"] == 412
    assert attrs["request.provider"] == "anthropic"
    assert attrs["request.model"] == "claude-haiku-5-5"
    assert attrs["request.temperature"] == 0.2
    assert attrs["metadata.thing"] == "<Opaque>"
    assert attrs["metadata.cached"] is False
    assert "metadata.skipped" not in attrs
    for whole in ("metrics", "request", "metadata"):
        assert whole not in attrs
    assert attrs["tenant"] == "acme"
    assert json.loads(attrs["tags"]) == ["audit", "q4"]
    assert attrs["status"] == "success"


def test_oversized_custom_attribute_is_truncated(exporter):
    @traced(attributes={"blob": "y" * (MAX_ATTRIBUTE_VALUE_CHARS + 10)})
    def noop():
        return None

    noop()
    attrs = _only_span(exporter)

    assert len(attrs["blob"]) == MAX_ATTRIBUTE_VALUE_CHARS
    assert attrs["blob"].endswith(TRUNCATION_MARKER)


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
