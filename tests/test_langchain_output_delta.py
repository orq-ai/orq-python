"""Regression test for root-chain output message delta.

LangGraph hands its root on_chain_end the full merged state, so the
input turns leak into outputs['messages']. The handler trims them via
root_output_delta before storing event.outputs.
"""

import pytest

pytest.importorskip("langchain_core")

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  # noqa: E402

from orq_ai_sdk.langchain._utils import root_output_delta  # noqa: E402


class TestRootOutputDelta:
    def test_strips_input_messages_by_id(self):
        human = HumanMessage(content="hello", id="msg-1")
        new_ai = AIMessage(content="hi", id="msg-2")

        result = root_output_delta(
            inputs={"messages": [human]},
            outputs={"messages": [human, new_ai]},
        )

        assert result["messages"] == [new_ai]

    def test_multi_turn_input_with_single_new_reply(self):
        inputs = [
            SystemMessage(content="sys", id="m1"),
            HumanMessage(content="hi", id="m2"),
            AIMessage(content="hello", id="m3"),
            HumanMessage(content="continue", id="m4"),
        ]
        reply = AIMessage(content="ok", id="m5")

        result = root_output_delta(
            inputs={"messages": inputs},
            outputs={"messages": inputs + [reply]},
        )

        assert result["messages"] == [reply]

    def test_falls_back_to_positional_trim_when_ids_missing(self):
        # Older LangChain Message objects may not auto-assign ids.
        human = HumanMessage(content="hi")
        human.id = None
        reply = AIMessage(content="ok")
        reply.id = None

        result = root_output_delta(
            inputs={"messages": [human]},
            outputs={"messages": [human, reply]},
        )

        assert result["messages"] == [reply]

    def test_tuple_inputs_trimmed_positionally(self):
        # create_react_agent: input is [("user", "...")], output is BaseMessage list.
        ai = AIMessage(content="hello", id="m2")
        result = root_output_delta(
            inputs={"messages": [("user", "hi")]},
            outputs={"messages": [HumanMessage(content="hi", id="m1"), ai]},
        )

        assert result["messages"] == [ai]

    def test_tuple_inputs_multiple_new(self):
        replies = [
            AIMessage(content="tool call", id="m2"),
            HumanMessage(content="next turn", id="m3"),  # synthetic, illustrative
        ]
        result = root_output_delta(
            inputs={"messages": [("user", "hi")]},
            outputs={"messages": [HumanMessage(content="hi", id="m1")] + replies},
        )

        assert result["messages"] == replies

    def test_preserves_extra_output_keys(self):
        human = HumanMessage(content="hi", id="m1")
        reply = AIMessage(content="ok", id="m2")

        result = root_output_delta(
            inputs={"messages": [human]},
            outputs={
                "messages": [human, reply],
                "step": 3,
                "metadata": {"foo": "bar"},
            },
        )

        assert result["messages"] == [reply]
        assert result["step"] == 3
        assert result["metadata"] == {"foo": "bar"}

    def test_empty_output_messages_passes_through(self):
        result = root_output_delta(
            inputs={"messages": [HumanMessage(content="hi", id="m1")]},
            outputs={"messages": []},
        )

        assert result == {"messages": []}

    def test_non_messages_output_unchanged(self):
        outputs = {"summary": "done", "count": 3}

        result = root_output_delta(
            inputs={"messages": [HumanMessage(content="hi", id="m1")]},
            outputs=outputs,
        )

        assert result == outputs

    def test_missing_inputs_passes_through(self):
        outputs = {"messages": [AIMessage(content="ok", id="m1")]}

        result = root_output_delta(inputs=None, outputs=outputs)

        assert result == outputs

    def test_works_with_already_normalized_dict_messages(self):
        in_dict = {"role": "user", "content": "hi", "id": "m1"}
        new_dict = {"role": "assistant", "content": "ok", "id": "m2"}

        result = root_output_delta(
            inputs={"messages": [in_dict]},
            outputs={"messages": [in_dict, new_dict]},
        )

        assert result["messages"] == [new_dict]

    def test_message_removed_via_id_filtering(self):
        # If a node deletes a message (e.g. RemoveMessage), it simply isn't in
        # outputs.messages anymore; the delta should reflect only what remains
        # that wasn't in inputs.
        msg_keep = HumanMessage(content="keep me", id="m1")
        msg_drop = HumanMessage(content="will be removed", id="m2")
        reply = AIMessage(content="reply", id="m3")

        result = root_output_delta(
            inputs={"messages": [msg_keep, msg_drop]},
            outputs={"messages": [msg_keep, reply]},  # m2 removed by a node
        )

        assert result["messages"] == [reply]
