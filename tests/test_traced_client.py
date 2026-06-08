"""Regression tests for the traced span client.

These lock the fix for concurrent subspan loss: ``get_client()`` used to rebuild the
global span client on every span (via ``init_from_orq`` → ``shutdown()`` + recreate when
a live ``Orq`` instance is discoverable). Each span then landed on its own throwaway
client that never flushed during the process, so under ``asyncio.gather`` the children
were silently dropped — a trace showed its root with most/all subspans missing.

All tests are offline: ``requests.post`` is stubbed with a counting fake. We drive real
async via ``asyncio.run`` (no pytest-asyncio dependency) and force-flush by shutting the
client down before asserting.
"""

import asyncio
import threading

import pytest

from orq_ai_sdk.traced import client as traced_client
from orq_ai_sdk.traced import config as traced_config
from orq_ai_sdk.traced import context as traced_context
from orq_ai_sdk.traced.config import Config
from orq_ai_sdk.traced.decorators import traced


class _SpanSink:
    """Thread-safe stub for ``requests.post`` that counts the spans it receives."""

    def __init__(self):
        self._lock = threading.Lock()
        self.calls = 0
        self.spans = 0

    def __call__(self, _url, *_args, **kwargs):
        payload = kwargs.get("json") or {}
        n = len(payload.get("spans", []))
        with self._lock:
            self.calls += 1
            self.spans += n

        class _Resp:
            status_code = 200
            text = '{"success":true}'

        return _Resp()


class _FakeSDKConfig:
    """Mimics exactly the ``sdk_configuration`` attributes that ``init_from_orq`` reads."""

    def __init__(self, api_key: str, server_url: str):
        self.security = type("Sec", (), {"api_key": api_key})()
        self._server_url = server_url
        self.debug_logger = None
        self.timeout_ms = None

    def get_server_details(self):
        return self._server_url, {}


class _FakeOrq:
    def __init__(self, api_key: str = "test", server_url: str = "http://localhost:0"):
        self.sdk_configuration = _FakeSDKConfig(api_key, server_url)


@pytest.fixture(autouse=True)
def _reset_traced_globals(monkeypatch):
    """Each test starts from a clean global client/config and a stubbed transport."""
    sink = _SpanSink()
    monkeypatch.setattr(traced_client.requests, "post", sink)
    # Start clean; the patched OrqClient queue/thread is per-instance.
    monkeypatch.setattr(traced_client, "_client", None, raising=False)
    monkeypatch.setattr(traced_config, "_config", None, raising=False)
    # Reset span-stack/trace contextvars so a leaked parent can't bleed across tests.
    traced_context._span_stack.set([])
    traced_context._trace_context.set(None)
    yield sink
    client = traced_client._client
    if client is not None:
        client.shutdown()


def _drain():
    """Force any queued spans out, then let the background thread settle."""
    client = traced_client._client
    if client is not None:
        client.flush()
        client.shutdown()


def test_concurrent_children_share_one_client(_reset_traced_globals, monkeypatch):
    """Root + 8 gather children must all run on ONE span client.

    The bug rebuilt the client per span (here: 9 builds, and under real-world timing the
    orphaned clients drop their queued children). The deterministic signature is the build
    count: 9 before the fix, 1 after. We also assert all 9 spans ship.
    """
    sink = _reset_traced_globals
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq())

    built = {"n": 0}
    real_cls = traced_client.OrqClient

    class _Counting(real_cls):
        def __init__(self, *a, **k):
            built["n"] += 1
            super().__init__(*a, **k)

    monkeypatch.setattr(traced_client, "OrqClient", _Counting)

    @traced(name="root")
    async def root():
        await asyncio.gather(*[child(i) for i in range(8)])
        return "ok"

    @traced(type="llm", name="child")
    async def child(i):
        await asyncio.sleep(0.01)
        return i

    asyncio.run(root())
    _drain()
    assert built["n"] == 1, f"span client rebuilt per span (churn): {built['n']} clients built, expected 1"
    assert sink.spans == 9, f"expected 9 spans (1 root + 8 children), got {sink.spans}"


def test_sequential_children_all_sent_with_live_orq(_reset_traced_globals, monkeypatch):
    sink = _reset_traced_globals
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq())

    @traced(name="root")
    async def root():
        for i in range(8):
            await child(i)
        return "ok"

    @traced(type="llm", name="child")
    async def child(i):
        return i

    asyncio.run(root())
    _drain()
    assert sink.spans == 9, f"expected 9 spans, got {sink.spans}"


def test_no_orq_instance_path(_reset_traced_globals, monkeypatch):
    """With no discoverable Orq instance, the cached default client must also keep all spans."""
    sink = _reset_traced_globals
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: None)
    traced_config.set_config(Config(api_key="test", api_url="http://localhost:0", enabled=True))

    @traced(name="root")
    async def root():
        await asyncio.gather(*[child(i) for i in range(8)])

    @traced(type="llm", name="child")
    async def child(i):
        await asyncio.sleep(0.01)

    asyncio.run(root())
    _drain()
    assert sink.spans == 9, f"expected 9 spans, got {sink.spans}"


def test_get_client_is_cached(_reset_traced_globals, monkeypatch):
    """Repeated get_client() must return the same instance and build exactly one client."""
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq())

    built = {"n": 0}
    real_cls = traced_client.OrqClient

    class _Counting(real_cls):
        def __init__(self, *a, **k):
            built["n"] += 1
            super().__init__(*a, **k)

    monkeypatch.setattr(traced_client, "OrqClient", _Counting)

    first = traced_client.get_client()
    for _ in range(5):
        assert traced_client.get_client() is first
    assert built["n"] == 1, f"expected exactly 1 client construction, got {built['n']}"


def test_config_change_rebuilds(_reset_traced_globals, monkeypatch):
    """A genuinely different resolved config must rebuild — cache must not pin the wrong target."""
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq(server_url="http://host-a:0"))
    client_a = traced_client.get_client()
    assert client_a.config.api_url == "http://host-a:0"

    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq(server_url="http://host-b:0"))
    client_b = traced_client.get_client()
    assert client_b is not client_a
    assert client_b.config.api_url == "http://host-b:0"


def test_idempotent_no_thread_leak(_reset_traced_globals, monkeypatch):
    """Re-initializing from the same Orq config must not spawn a new client/thread each call."""
    monkeypatch.setattr(traced_client, "_find_orq_instance", lambda: _FakeOrq())
    first = traced_client.get_client()
    baseline_threads = threading.active_count()
    for _ in range(10):
        assert traced_client.get_client() is first
    assert threading.active_count() <= baseline_threads, "client/flush threads leaked on repeated get_client()"
