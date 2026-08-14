"""Tests for the @traced decorator with both sync and async functions."""

import asyncio
import inspect
from unittest.mock import patch, MagicMock

import pytest
import pytest_asyncio

from orq_ai_sdk.traced.decorators import traced
from orq_ai_sdk.traced.config import Config, set_config
from orq_ai_sdk.traced.context import current_span


@pytest.fixture(autouse=True)
def _configure_tracing():
    """Set up tracing config with a fake API key and mock the client."""
    config = Config(api_key="test-key", enabled=True)
    set_config(config)

    mock_client = MagicMock()
    with patch("orq_ai_sdk.traced.decorators.get_client", return_value=mock_client):
        yield mock_client

    # Reset config
    set_config(Config(enabled=False))


# ---------------------------------------------------------------------------
# Sync tests
# ---------------------------------------------------------------------------


class TestSyncTraced:
    def test_basic_return_value(self):
        @traced
        def add(a, b):
            return a + b

        assert add(1, 2) == 3

    def test_preserves_function_metadata(self):
        @traced
        def my_func():
            """My docstring."""
            pass

        assert my_func.__name__ == "my_func"
        assert my_func.__doc__ == "My docstring."

    def test_custom_name(self):
        @traced(name="custom")
        def my_func():
            return 42

        assert my_func() == 42

    def test_exception_propagates(self):
        @traced
        def failing():
            raise ValueError("boom")

        with pytest.raises(ValueError, match="boom"):
            failing()

    def test_span_records_error(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        def failing():
            raise RuntimeError("oops")

        with pytest.raises(RuntimeError):
            failing()

        assert len(spans) == 1
        assert spans[0].attributes["status"] == "error"
        assert spans[0].attributes["error.message"] == "oops"

    def test_span_captures_input_and_output(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        def greet(name):
            return f"hello {name}"

        result = greet("world")
        assert result == "hello world"
        assert len(spans) == 1
        assert spans[0].input == {"name": "world"}
        assert spans[0].output == "hello world"

    def test_capture_input_false(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced(capture_input=False)
        def greet(name):
            return f"hello {name}"

        greet("world")
        assert len(spans) == 1
        assert spans[0].input is None

    def test_capture_output_false(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced(capture_output=False)
        def greet(name):
            return f"hello {name}"

        greet("world")
        assert len(spans) == 1
        assert spans[0].output is None

    def test_current_span_accessible(self):
        captured_span = None

        @traced
        def my_func():
            nonlocal captured_span
            captured_span = current_span()
            return "done"

        my_func()
        assert captured_span is not None
        assert captured_span.name == "my_func"

    def test_nested_spans_parent_child(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        def inner():
            return "inner"

        @traced
        def outer():
            return inner()

        outer()
        assert len(spans) == 2
        inner_span = spans[0]
        outer_span = spans[1]
        assert inner_span.parent_id == outer_span.span_id
        assert inner_span.trace_id == outer_span.trace_id

    def test_is_not_coroutine_function(self):
        @traced
        def my_func():
            pass

        assert not inspect.iscoroutinefunction(my_func)

    def test_disabled_tracing_skips_spans(self, _configure_tracing):
        mock_client = _configure_tracing
        set_config(Config(api_key="test-key", enabled=False))

        @traced
        def my_func():
            return 42

        assert my_func() == 42
        mock_client.submit_span.assert_not_called()


# ---------------------------------------------------------------------------
# Async tests
# ---------------------------------------------------------------------------


class TestAsyncTraced:
    @pytest.mark.asyncio
    async def test_basic_return_value(self):
        @traced
        async def add(a, b):
            return a + b

        assert await add(1, 2) == 3

    @pytest.mark.asyncio
    async def test_preserves_function_metadata(self):
        @traced
        async def my_func():
            """My async docstring."""
            pass

        assert my_func.__name__ == "my_func"
        assert my_func.__doc__ == "My async docstring."

    @pytest.mark.asyncio
    async def test_is_coroutine_function(self):
        @traced
        async def my_func():
            pass

        assert inspect.iscoroutinefunction(my_func)

    @pytest.mark.asyncio
    async def test_custom_name(self):
        @traced(name="custom_async")
        async def my_func():
            return 42

        assert await my_func() == 42

    @pytest.mark.asyncio
    async def test_exception_propagates(self):
        @traced
        async def failing():
            raise ValueError("async boom")

        with pytest.raises(ValueError, match="async boom"):
            await failing()

    @pytest.mark.asyncio
    async def test_span_records_error(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        async def failing():
            raise RuntimeError("async oops")

        with pytest.raises(RuntimeError):
            await failing()

        assert len(spans) == 1
        assert spans[0].attributes["status"] == "error"
        assert spans[0].attributes["error.message"] == "async oops"

    @pytest.mark.asyncio
    async def test_span_captures_input_and_output(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        async def greet(name):
            return f"hello {name}"

        result = await greet("world")
        assert result == "hello world"
        assert len(spans) == 1
        assert spans[0].input == {"name": "world"}
        assert spans[0].output == "hello world"

    @pytest.mark.asyncio
    async def test_output_is_not_coroutine_object(self, _configure_tracing):
        """The core bug: before the fix, output would be '<coroutine object ...>'."""
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        async def compute():
            return {"result": 42}

        result = await compute()
        assert result == {"result": 42}
        assert len(spans) == 1
        assert spans[0].output == {"result": 42}
        assert "coroutine" not in str(spans[0].output)

    @pytest.mark.asyncio
    async def test_capture_input_false(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced(capture_input=False)
        async def greet(name):
            return f"hello {name}"

        await greet("world")
        assert len(spans) == 1
        assert spans[0].input is None

    @pytest.mark.asyncio
    async def test_capture_output_false(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced(capture_output=False)
        async def greet(name):
            return f"hello {name}"

        await greet("world")
        assert len(spans) == 1
        assert spans[0].output is None

    @pytest.mark.asyncio
    async def test_current_span_accessible(self):
        captured_span = None

        @traced
        async def my_func():
            nonlocal captured_span
            captured_span = current_span()
            return "done"

        await my_func()
        assert captured_span is not None
        assert captured_span.name == "my_func"

    @pytest.mark.asyncio
    async def test_nested_async_spans_parent_child(self, _configure_tracing):
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        async def inner():
            return "inner"

        @traced
        async def outer():
            return await inner()

        await outer()
        assert len(spans) == 2
        inner_span = spans[0]
        outer_span = spans[1]
        assert inner_span.parent_id == outer_span.span_id
        assert inner_span.trace_id == outer_span.trace_id

    @pytest.mark.asyncio
    async def test_mixed_sync_async_nesting(self, _configure_tracing):
        """Async parent calling sync child should maintain parent-child relationship."""
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        def sync_inner():
            return "sync"

        @traced
        async def async_outer():
            return sync_inner()

        await async_outer()
        assert len(spans) == 2
        sync_span = spans[0]
        async_span = spans[1]
        assert sync_span.parent_id == async_span.span_id

    @pytest.mark.asyncio
    async def test_disabled_tracing_skips_spans(self, _configure_tracing):
        mock_client = _configure_tracing
        set_config(Config(api_key="test-key", enabled=False))

        @traced
        async def my_func():
            return 42

        assert await my_func() == 42
        mock_client.submit_span.assert_not_called()

    @pytest.mark.asyncio
    async def test_concurrent_async_tasks(self, _configure_tracing):
        """Multiple concurrent async traced functions should each get their own span."""
        mock_client = _configure_tracing
        spans = []
        mock_client.submit_span.side_effect = lambda s: spans.append(s)

        @traced
        async def task(n):
            await asyncio.sleep(0.01)
            return n * 2

        results = await asyncio.gather(task(1), task(2), task(3))
        assert sorted(results) == [2, 4, 6]
        assert len(spans) == 3
