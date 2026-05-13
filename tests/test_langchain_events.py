"""Tests for the Events store, especially root-run tracking across invocations."""

import pytest

pytest.importorskip("langchain_core")

from orq_ai_sdk.langchain._events import Events  # noqa: E402


class TestRootTracking:
    def test_first_parentless_chain_becomes_root(self):
        events = Events()
        events.set_root_if_needed("run-1")

        assert events.is_root("run-1")
        assert events.root_run_id == "run-1"

    def test_second_set_root_does_not_override(self):
        events = Events()
        events.set_root_if_needed("run-1")
        events.set_root_if_needed("run-2")

        assert events.is_root("run-1")
        assert not events.is_root("run-2")

    def test_clear_root_releases_first_run(self):
        events = Events()
        events.set_root_if_needed("run-1")
        events.clear_root("run-1")

        assert events.root_run_id is None
        assert not events.is_root("run-1")

    def test_clear_root_ignores_non_root_ids(self):
        events = Events()
        events.set_root_if_needed("run-1")
        events.clear_root("run-2")

        assert events.is_root("run-1")

    def test_new_invocation_becomes_root_after_clear(self):
        # Reproduces the multi-invocation bug: prior to the fix,
        # the second top-level invocation could never become root.
        events = Events()
        events.set_root_if_needed("run-1")
        events.clear_root("run-1")
        events.set_root_if_needed("run-2")

        assert events.is_root("run-2")
        assert not events.is_root("run-1")

    def test_clear_root_resets_graph_tracker(self):
        events = Events()
        events.set_root_if_needed("run-1")
        first_graph = events.graph

        events.clear_root("run-1")

        # New graph tracker for the next invocation, so node state doesn't leak.
        assert events.graph is not first_graph
