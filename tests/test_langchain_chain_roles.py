"""Regression test for chain/agent span message-role round-tripping.

Prior to the fix, _build_prompt/_build_completion returned event.inputs/outputs
verbatim for CHAIN/AGENT events. Raw LangChain Message objects then serialized
via __str__ and lost their structured role, so SystemMessage/HumanMessage/
AIMessage all surfaced as role: assistant in the backend.
"""

import pytest

pytest.importorskip("langchain_core")

from langchain_core.messages import (  # noqa: E402
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

from orq_ai_sdk.langchain._models import EventType, InFlightEvent  # noqa: E402
from orq_ai_sdk.langchain._span_builder import (  # noqa: E402
    _build_completion,
    _build_prompt,
)


def _make_chain_event(*, inputs=None, outputs=None) -> InFlightEvent:
    return InFlightEvent(
        run_id="run-1",
        event_type=EventType.CHAIN,
        inputs=inputs,
        outputs=outputs,
    )


class TestChainMessageRoles:
    def test_prompt_preserves_roles_for_all_message_types(self):
        messages = [
            SystemMessage(content="sys"),
            HumanMessage(content="hi"),
            AIMessage(
                content="ok",
                tool_calls=[{"name": "noop", "args": {}, "id": "call_1"}],
            ),
            ToolMessage(content="result", tool_call_id="call_1"),
            HumanMessage(content="continue"),
        ]
        event = _make_chain_event(inputs={"messages": messages})

        prompt = _build_prompt(event)

        assert [m["role"] for m in prompt["messages"]] == [
            "system",
            "user",
            "assistant",
            "tool",
            "user",
        ]

    def test_completion_preserves_assistant_role(self):
        event = _make_chain_event(outputs={"messages": [AIMessage(content="done")]})

        completion = _build_completion(event)

        assert completion["messages"][0]["role"] == "assistant"
        assert completion["messages"][0]["content"] == "done"

    def test_ai_message_tool_calls_survive_normalization(self):
        tool_call = {"name": "lookup", "args": {"q": "x"}, "id": "call_abc"}
        event = _make_chain_event(
            outputs={"messages": [AIMessage(content="", tool_calls=[tool_call])]}
        )

        completion = _build_completion(event)

        entry = completion["messages"][0]
        assert entry["role"] == "assistant"
        assert len(entry["tool_calls"]) == 1
        assert entry["tool_calls"][0]["name"] == "lookup"
        assert entry["tool_calls"][0]["id"] == "call_abc"
        assert entry["tool_calls"][0]["args"] == {"q": "x"}

    def test_extra_state_keys_are_preserved(self):
        event = _make_chain_event(
            inputs={
                "messages": [HumanMessage(content="hi")],
                "session_id": "abc",
                "step": 2,
            }
        )

        prompt = _build_prompt(event)

        assert prompt["session_id"] == "abc"
        assert prompt["step"] == 2
        assert prompt["messages"][0]["role"] == "user"

    def test_non_message_inputs_pass_through_unchanged(self):
        event = _make_chain_event(inputs={"query": "search term", "k": 5})

        prompt = _build_prompt(event)

        assert prompt == {"query": "search term", "k": 5}

    def test_already_normalized_messages_pass_through(self):
        already_dicts = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "hi"},
        ]
        event = _make_chain_event(inputs={"messages": already_dicts})

        prompt = _build_prompt(event)

        assert prompt["messages"] == already_dicts

    def test_empty_messages_list_passes_through(self):
        event = _make_chain_event(inputs={"messages": []})

        prompt = _build_prompt(event)

        assert prompt == {"messages": []}

    def test_none_inputs_returns_none(self):
        event = _make_chain_event(inputs=None)

        assert _build_prompt(event) is None

    def test_tuple_inputs_get_normalized(self):
        # create_react_agent style: {"messages": [("user", "...")]}
        event = _make_chain_event(
            inputs={"messages": [("user", "hi"), ("system", "be nice")]}
        )

        prompt = _build_prompt(event)

        assert prompt["messages"] == [
            {"role": "user", "content": "hi"},
            {"role": "system", "content": "be nice"},
        ]

    def test_tuple_role_aliases(self):
        event = _make_chain_event(
            inputs={"messages": [("human", "hi"), ("ai", "ok")]}
        )

        prompt = _build_prompt(event)

        assert [m["role"] for m in prompt["messages"]] == ["user", "assistant"]

    def test_chain_output_as_single_ai_message_gets_normalized(self):
        # RunnableSequence wrapping a chat model hands on_chain_end a bare
        # AIMessage (not wrapped in a dict). The SDK now coerces this into
        # {messages: [...]} before normalization, so the trace gets readable
        # role/content/tool_calls instead of a Python __str__ repr.
        from orq_ai_sdk.langchain._utils import coerce_chain_payload  # noqa: WPS433

        ai = AIMessage(
            content="",
            tool_calls=[{"name": "lookup", "args": {"q": "x"}, "id": "call_1"}],
        )
        event = _make_chain_event(outputs=coerce_chain_payload(ai))

        completion = _build_completion(event)

        assert completion["messages"][0]["role"] == "assistant"
        assert completion["messages"][0]["content"] == ""
        assert len(completion["messages"][0]["tool_calls"]) == 1

    def test_chain_output_as_basemessage_list_gets_normalized(self):
        from orq_ai_sdk.langchain._utils import coerce_chain_payload  # noqa: WPS433

        messages = [HumanMessage(content="hi"), AIMessage(content="hello")]
        event = _make_chain_event(outputs=coerce_chain_payload(messages))

        completion = _build_completion(event)

        assert [m["role"] for m in completion["messages"]] == ["user", "assistant"]

    def test_coerce_passes_dicts_through_unchanged(self):
        from orq_ai_sdk.langchain._utils import coerce_chain_payload  # noqa: WPS433

        payload = {"messages": [HumanMessage(content="hi")], "extra": "keep"}
        assert coerce_chain_payload(payload) is payload

    def test_coerce_falls_back_to_outputs_for_unknown_types(self):
        from orq_ai_sdk.langchain._utils import coerce_chain_payload  # noqa: WPS433

        assert coerce_chain_payload("a string") == {"outputs": "a string"}
        assert coerce_chain_payload(42) == {"outputs": 42}

    def test_mixed_basemessages_and_tuples(self):
        event = _make_chain_event(
            inputs={
                "messages": [
                    ("user", "hi"),
                    AIMessage(content="hello back"),
                ]
            }
        )

        prompt = _build_prompt(event)

        assert [m["role"] for m in prompt["messages"]] == ["user", "assistant"]
        assert prompt["messages"][0]["content"] == "hi"
        assert prompt["messages"][1]["content"] == "hello back"
