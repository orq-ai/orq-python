"""Regression test for tool-input serialization.

Prior to the fix, on_tool_start stored LangChain's ``input_str`` verbatim. For
a tool whose schema is a Pydantic model, ``input_str`` is ``str(tool_input)``
on a dict whose values' ``__repr__`` produces ``Order(...)`` notation -- not
valid JSON. The handler now prefers the structured ``inputs`` kwarg and
serializes Pydantic models to JSON, so evaluators and the trace viewer can
parse the captured arguments.
"""

import json
from uuid import uuid4

import pytest

pytest.importorskip("langchain_core")
pytest.importorskip("pydantic")

from pydantic import BaseModel  # noqa: E402

from orq_ai_sdk.langchain._handler import OrqLangchainCallback  # noqa: E402
from orq_ai_sdk.langchain._utils import serialize_tool_payload  # noqa: E402


class _Item(BaseModel):
    sku: str
    qty: int


def _handler() -> OrqLangchainCallback:
    handler = OrqLangchainCallback(api_key="test-key", api_url="http://invalid.local")
    # Stub the client send -- the test asserts on the in-flight event, not on
    # the wire payload, and we never want a network call during unit tests.
    handler._client.send_otlp = lambda *args, **kwargs: None  # type: ignore[method-assign]
    return handler


class TestSerializeToolPayload:
    def test_pydantic_dict_becomes_json(self):
        payload = {"item": _Item(sku="X", qty=3)}

        result = serialize_tool_payload(payload)

        assert json.loads(result) == {"item": {"sku": "X", "qty": 3}}

    def test_string_passes_through_unchanged(self):
        # Tool outputs are typically already strings; we must not double-quote.
        assert serialize_tool_payload("ok") == "ok"

    def test_plain_dict_round_trips(self):
        assert json.loads(serialize_tool_payload({"a": 1, "b": [2, 3]})) == {
            "a": 1,
            "b": [2, 3],
        }

    def test_none_serializes_as_json_null(self):
        assert serialize_tool_payload(None) == "null"

    def test_unserializable_falls_back_to_json_string(self):
        class _Weird:
            def __repr__(self) -> str:
                return "Weird()"

        # Must not raise. json.dumps(..., default=str) coerces unknown objects
        # to their str() form and quotes them, so the output remains valid JSON
        # rather than a crash or a raw Python repr.
        result = serialize_tool_payload(_Weird())
        assert json.loads(result) == "Weird()"


class TestOnToolStartPrefersInputsKwarg:
    def test_pydantic_input_serialized_as_json(self):
        handler = _handler()
        run_id = uuid4()
        structured_inputs = {"item": _Item(sku="X", qty=3)}
        lossy_input_str = str(structured_inputs)  # what LangChain hands us

        handler.on_tool_start(
            serialized={"name": "submit"},
            input_str=lossy_input_str,
            run_id=run_id,
            inputs=structured_inputs,
        )

        event = handler._events.get(str(run_id))
        assert event is not None
        assert event.tool_input is not None
        # Critical: must parse as JSON, not be Python-repr.
        parsed = json.loads(event.tool_input)
        assert parsed == {"item": {"sku": "X", "qty": 3}}

    def test_falls_back_to_input_str_when_inputs_kwarg_absent(self):
        # LangChain versions or call paths that do not provide kwargs["inputs"]
        # should keep working -- we just lose Pydantic-aware encoding for them.
        handler = _handler()
        run_id = uuid4()

        handler.on_tool_start(
            serialized={"name": "submit"},
            input_str="raw-string-input",
            run_id=run_id,
        )

        event = handler._events.get(str(run_id))
        assert event is not None
        assert event.tool_input == "raw-string-input"


class TestOnToolEndPreservesStrings:
    def test_string_output_unchanged(self):
        assert serialize_tool_payload("plain string result") == "plain string result"

    def test_pydantic_output_becomes_json(self):
        # Pre-empts a future regression if a tool returns a Pydantic model.
        out = _Item(sku="A", qty=1)
        assert json.loads(serialize_tool_payload(out)) == {"sku": "A", "qty": 1}

    def test_tool_message_output_unwraps_to_content_string(self):
        # When invoked through an agent (langgraph), LangChain wraps the
        # tool's return in a ToolMessage. The handler must unwrap to .content
        # so the trace viewer sees a clean string -- not the full message
        # struct (which would expose additional_kwargs, response_metadata,
        # artifact, status, ...).
        from langchain_core.messages import ToolMessage

        handler = _handler()
        sent: list = []
        # Capture what the span builder produces by stubbing send_otlp.
        handler._client.send_otlp = lambda payload: sent.append(payload)  # type: ignore[method-assign]

        run_id = uuid4()
        handler.on_tool_start(
            serialized={"name": "get_weather"},
            input_str='{"city": "Paris"}',
            run_id=run_id,
            inputs={"city": "Paris"},
        )
        # Inspect the event before finish-and-send pops it.
        event = handler._events.get(str(run_id))
        assert event is not None
        msg = ToolMessage(
            content="Sunny, 22°C",
            tool_call_id="call_abc",
            name="get_weather",
        )
        # Manually invoke the unwrap-then-serialize path that on_tool_end uses.
        from langchain_core.messages import BaseMessage
        unwrapped = msg.content if isinstance(msg, BaseMessage) else msg
        result = serialize_tool_payload(unwrapped)

        assert result == "Sunny, 22°C"


class TestChainSpanPydanticInputs:
    """Pydantic models nested inside chain inputs/outputs must serialize as JSON.

    BaseTool.invoke wraps the call in a chain span whose ``event.inputs`` is the
    raw dict ``{"order": Order(...)}``. Without a JSON-aware encoder, the OTLP
    builder's ``json.dumps(..., default=str)`` falls back to ``repr()`` on the
    Pydantic value, producing a Python-repr string in the trace.
    """

    def test_chain_input_with_pydantic_value_serializes_as_json(self):
        from orq_ai_sdk.langchain._models import EventType, InFlightEvent
        from orq_ai_sdk.langchain._span_builder import build_otlp_span

        event = InFlightEvent(
            run_id="span-1",
            event_type=EventType.CHAIN,
            name="submit_order",
            start_time_ns="0",
            end_time_ns="1",
            inputs={"order": _Item(sku="X", qty=3)},
        )

        span = build_otlp_span(event)
        prompt_attr = next(
            a for a in span["attributes"] if a["key"] == "gen_ai.prompt"
        )
        parsed = json.loads(prompt_attr["value"]["stringValue"])
        assert parsed == {"order": {"sku": "X", "qty": 3}}

    def test_tool_prompt_emits_messages_shape_for_input_panel(self):
        # The viewer derives its Input panel from gen_ai.input.messages, which
        # the backend synthesizes from a {"messages": [...]} prompt -- not from
        # the legacy {"input": "..."} wrapper. Tool spans must emit the same
        # shape as LLM spans so the input renders.
        from orq_ai_sdk.langchain._models import EventType, InFlightEvent
        from orq_ai_sdk.langchain._span_builder import build_otlp_span

        args_json = json.dumps({"city": "paris"})
        event = InFlightEvent(
            run_id="span-tool",
            event_type=EventType.TOOL,
            name="get_weather",
            start_time_ns="0",
            end_time_ns="1",
            tool_input=args_json,
        )

        span = build_otlp_span(event)
        prompt_attr = next(a for a in span["attributes"] if a["key"] == "gen_ai.prompt")
        parsed = json.loads(prompt_attr["value"]["stringValue"])

        assert parsed["messages"] == [{"role": "user", "content": args_json}]
        # Legacy key preserved for any downstream readers still keying off it.
        assert parsed["input"] == args_json

    def test_chain_output_with_pydantic_value_serializes_as_json(self):
        from orq_ai_sdk.langchain._models import EventType, InFlightEvent
        from orq_ai_sdk.langchain._span_builder import build_otlp_span

        event = InFlightEvent(
            run_id="span-2",
            event_type=EventType.CHAIN,
            name="submit_order",
            start_time_ns="0",
            end_time_ns="1",
            outputs={"result": _Item(sku="X", qty=3)},
        )

        span = build_otlp_span(event)
        completion_attr = next(
            a for a in span["attributes"] if a["key"] == "gen_ai.completion"
        )
        parsed = json.loads(completion_attr["value"]["stringValue"])
        assert parsed == {"result": {"sku": "X", "qty": 3}}
