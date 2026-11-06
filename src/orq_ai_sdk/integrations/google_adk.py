"""Google ADK tracing with outbound request correlation."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from opentelemetry.trace import TracerProvider


def instrument_google_adk(*, tracer_provider: TracerProvider | None = None) -> None:
    """Instrument ADK and propagate its active trace context to model requests.

    Call after configuring the OpenTelemetry provider/exporter and before creating
    ADK runners or model clients. The integration does not create a provider or
    exporter and can be called more than once.
    """
    if sys.version_info < (3, 11):
        raise RuntimeError("Google ADK integration requires Python 3.11 or later.")

    try:
        from openinference.instrumentation.google_adk import GoogleADKInstrumentor
    except ImportError as exc:
        raise ImportError(
            "Google ADK tracing requires the optional integration: "
            "pip install 'orq-ai-sdk[google-adk]'"
        ) from exc

    from orq_ai_sdk.traced.http_propagation import install_http_propagation

    instrumentor = GoogleADKInstrumentor()
    if not instrumentor.is_instrumented_by_opentelemetry:
        instrumentor.instrument(
            tracer_provider=tracer_provider, raise_exception_on_conflict=True
        )
    install_http_propagation(otel_context=True)
