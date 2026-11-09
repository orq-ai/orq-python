"""Outbound correlation through real local HTTP and the ADK runner."""

import asyncio
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from queue import Queue
from threading import Thread
from unittest.mock import patch

import aiohttp
import httpx
import httpx2
import pytest
import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from orq_ai_sdk.integrations.google_adk import instrument_google_adk
from orq_ai_sdk.traced.context import SpanContext, SpanContextManager


@pytest.fixture(scope="module")
def telemetry():
    provider = TracerProvider()
    exporter = InMemorySpanExporter()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    instrument_google_adk(tracer_provider=provider)
    yield provider.get_tracer(__name__), exporter, provider
    from openinference.instrumentation.google_adk import GoogleADKInstrumentor

    GoogleADKInstrumentor().uninstrument()
    provider.shutdown()


@pytest.fixture
def endpoint():
    captured = Queue()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            captured.put(dict(self.headers))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            captured.put(dict(self.headers))
            payload = json.dumps(
                {
                    "candidates": [
                        {
                            "content": {"role": "model", "parts": [{"text": "ok"}]},
                            "finishReason": "STOP",
                        }
                    ],
                    "usageMetadata": {
                        "promptTokenCount": 5,
                        "candidatesTokenCount": 1,
                        "totalTokenCount": 6,
                        "cachedContentTokenCount": 3,
                    },
                    "modelVersion": "gemini-2.5-flash",
                    "responseId": "local-response",
                }
            ).encode()
            self.send_response(200)
            streaming = "alt=sse" in self.path
            self.send_header(
                "Content-Type", "text/event-stream" if streaming else "application/json"
            )
            self.end_headers()
            self.wfile.write(b"data: " + payload + b"\n\n" if streaming else payload)

        def log_message(self, *_args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}", captured
    server.shutdown()
    server.server_close()
    thread.join()


def incoming(captured):
    return {key.lower(): value for key, value in captured.get(timeout=2).items()}


def expected_parent(span):
    context = span.get_span_context()
    return f"00-{context.trace_id:032x}-{context.span_id:016x}-{int(context.trace_flags):02x}"


@pytest.mark.parametrize("library", [httpx, httpx2, requests])
def test_sync_transports_propagate_active_otel_span(telemetry, endpoint, library):
    tracer, _, _ = telemetry
    url, captured = endpoint
    with tracer.start_as_current_span("call_llm") as span:
        with library.Session() if library is requests else library.Client() as client:
            client.get(url)
        headers = incoming(captured)
        assert headers["traceparent"] == expected_parent(span)
        assert "orq=1" not in headers.get("tracestate", "")


@pytest.mark.asyncio
@pytest.mark.parametrize("library", [httpx, httpx2, aiohttp])
async def test_async_transports_propagate_active_otel_span(
    telemetry, endpoint, library
):
    tracer, _, _ = telemetry
    url, captured = endpoint
    with tracer.start_as_current_span("call_llm") as span:
        if library is aiohttp:
            async with library.ClientSession() as client, client.get(url) as response:
                await response.read()
        else:
            async with library.AsyncClient() as client:
                await client.get(url)
        headers = incoming(captured)
        assert headers["traceparent"] == expected_parent(span)
        assert "orq=1" not in headers.get("tracestate", "")


def test_existing_headers_and_no_span_are_preserved(telemetry, endpoint):
    tracer, _, _ = telemetry
    url, captured = endpoint
    existing = "00-11111111111111111111111111111111-2222222222222222-00"
    with tracer.start_as_current_span("call_llm"):
        httpx.get(url, headers={"Traceparent": existing, "Tracestate": "vendor=value"})
    headers = incoming(captured)
    assert headers["traceparent"] == existing
    assert headers["tracestate"] == "vendor=value"
    httpx.get(url)
    assert "traceparent" not in incoming(captured)


@pytest.mark.asyncio
async def test_concurrent_calls_keep_separate_contexts(telemetry, endpoint):
    tracer, _, _ = telemetry
    url, captured = endpoint

    async def call(index):
        with tracer.start_as_current_span(f"call_llm_{index}") as span:
            expected = expected_parent(span)
            await asyncio.sleep(0.01)
            async with aiohttp.ClientSession() as client, client.get(url) as response:
                await response.read()
            return expected

    expected = set(await asyncio.gather(*(call(i) for i in range(8))))
    actual = {incoming(captured)["traceparent"] for _ in range(8)}
    assert actual == expected


def test_legacy_traced_span_still_marks_orq_ownership(endpoint):
    url, captured = endpoint
    context = SpanContext(trace_id="1" * 32, span_id="2" * 16)
    with SpanContextManager(context):
        httpx.get(url)
    headers = incoming(captured)
    assert headers["traceparent"] == f"00-{'1' * 32}-{'2' * 16}-01"
    assert headers["tracestate"] == "orq=1"


def test_helper_reuses_the_instrumentor(telemetry):
    _, _, provider = telemetry
    from openinference.instrumentation.google_adk import GoogleADKInstrumentor

    other_provider = TracerProvider()
    try:
        with patch.object(GoogleADKInstrumentor, "instrument") as instrument:
            instrument_google_adk(tracer_provider=other_provider)
            instrument_google_adk(tracer_provider=provider)
            instrument.assert_not_called()
    finally:
        other_provider.shutdown()


@pytest.mark.asyncio
@pytest.mark.parametrize("stream", [False, True])
@pytest.mark.parametrize("transport", ["httpx", "aiohttp"])
async def test_real_adk_runner_correlates_model_request(
    telemetry, endpoint, stream, transport
):
    from google import genai
    from google.adk.agents import Agent
    from google.adk.agents.run_config import RunConfig, StreamingMode
    from google.adk.models import Gemini
    from google.adk.runners import InMemoryRunner
    from google.genai import types

    _, exporter, _ = telemetry
    exporter.clear()
    url, captured = endpoint
    options = types.HttpOptions(base_url=url, api_version="v1beta")
    if transport == "httpx":
        options.async_client_args = {"transport": httpx.AsyncHTTPTransport()}
    client = genai.Client(
        api_key="local-test-key", vertexai=False, http_options=options
    )
    model = Gemini(model="gemini-2.5-flash", client=client)
    runner = InMemoryRunner(
        agent=Agent(name="local_agent", model=model, instruction="Answer briefly.")
    )
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="local-user"
    )
    try:
        events = [
            event
            async for event in runner.run_async(
                user_id="local-user",
                session_id=session.id,
                new_message=types.Content(
                    role="user", parts=[types.Part(text="hello")]
                ),
                run_config=RunConfig(
                    streaming_mode=StreamingMode.SSE if stream else StreamingMode.NONE
                ),
            )
        ]
        assert any(event.is_final_response() for event in events)
        headers = incoming(captured)
        spans = exporter.get_finished_spans()
        matching = [
            span for span in spans if headers["traceparent"] == expected_parent(span)
        ]
        assert len(matching) == 1
        assert matching[0].attributes["openinference.span.kind"] == "LLM"
        assert matching[0].attributes["gen_ai.usage.cache_read.input_tokens"] == 3
        assert "orq=1" not in headers.get("tracestate", "")
    finally:
        await client.aio.aclose()
        client.close()


def test_unsampled_native_context_preserves_flags_and_tracestate(telemetry, endpoint):
    url, captured = endpoint
    context = trace.SpanContext(
        trace_id=int("3" * 32, 16),
        span_id=int("4" * 16, 16),
        is_remote=False,
        trace_flags=trace.TraceFlags(0),
        trace_state=trace.TraceState([("vendor", "value")]),
    )
    with trace.use_span(trace.NonRecordingSpan(context)):
        httpx.get(url)
    headers = incoming(captured)
    assert headers["traceparent"] == f"00-{'3' * 32}-{'4' * 16}-00"
    assert headers["tracestate"] == "vendor=value"


@pytest.mark.asyncio
async def test_aiohttp_preserves_client_default_trace_headers(telemetry, endpoint):
    tracer, _, _ = telemetry
    url, captured = endpoint
    existing = f"00-{'5' * 32}-{'6' * 16}-01"
    with tracer.start_as_current_span("call_llm"):
        async with (
            aiohttp.ClientSession(
                headers={"Traceparent": existing, "Tracestate": "vendor=prior"}
            ) as client,
            client.get(url) as response,
        ):
            await response.read()
    headers = incoming(captured)
    assert headers["traceparent"] == existing
    assert headers["tracestate"] == "vendor=prior"


def test_helper_rejects_unsupported_python(monkeypatch):
    from orq_ai_sdk.integrations import google_adk

    monkeypatch.setattr(google_adk.sys, "version_info", (3, 10, 0))
    with pytest.raises(RuntimeError, match="Python 3.11"):
        instrument_google_adk()
