"""Attributes @traced writes on its OpenTelemetry span when a global SDK provider is set."""

import json

import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.util._once import Once

from orq_ai_sdk.traced.config import Config, set_config
from orq_ai_sdk.traced.context import current_span
from orq_ai_sdk.traced.constants import MAX_ATTRIBUTE_VALUE_CHARS, TRUNCATION_MARKER
from orq_ai_sdk.traced.decorators import traced


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


def test_custom_attributes_are_json(exporter):
    @traced(attributes={"tenant": "acme", "tags": ["audit", "q4"]})
    def generate():
        current_span().log(
            metrics={"prompt_tokens": 76, "completion_tokens": 425},
            request={"provider": "anthropic", "model": "claude-haiku-5-5"},
            metadata={"thing": Opaque()},
        )
        return "ok"

    generate()
    attrs = _only_span(exporter)

    assert attrs["tenant"] == "acme"
    assert json.loads(attrs["tags"]) == ["audit", "q4"]
    assert json.loads(attrs["metrics"]) == {"prompt_tokens": 76, "completion_tokens": 425}
    assert json.loads(attrs["request"]) == {"provider": "anthropic", "model": "claude-haiku-5-5"}
    assert json.loads(attrs["metadata"]) == {"thing": "<Opaque>"}
    assert attrs["status"] == "success"


def test_oversized_custom_attribute_is_truncated(exporter):
    @traced(attributes={"blob": "y" * (MAX_ATTRIBUTE_VALUE_CHARS + 10)})
    def noop():
        return None

    noop()
    attrs = _only_span(exporter)

    assert len(attrs["blob"]) == MAX_ATTRIBUTE_VALUE_CHARS
    assert attrs["blob"].endswith(TRUNCATION_MARKER)
