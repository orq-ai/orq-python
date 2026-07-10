"""Live integration tests for function tools over the orq.ai Responses API.

These hit the real router, so they are skipped unless ORQ_API_KEY is set. They
guard the strict-schema fix: a tool with a defaulted parameter must be accepted
by OpenAI-routed models (which enforce OpenAI's strict function-calling spec and
returned a 400 before the fix) as well as Gemini (which tolerated the old schema).
"""

from __future__ import annotations

import os

import pytest

from orq_ai_sdk import Orq
from orq_ai_sdk.function_tools import tool

pytestmark = pytest.mark.skipif(
    not os.environ.get("ORQ_API_KEY"),
    reason="ORQ_API_KEY not set; skipping live Responses API tests.",
)

# provider/model format expected by the router.
MODELS = ["openai/gpt-4o", "google-ai/gemini-2.5-flash"]


@tool
def get_weather(city: str, units: str = "celsius") -> str:
    """Return the current weather for a city.

    `units` has a default, so under strict mode it is emitted as required +
    nullable — the exact shape that used to 400 on OpenAI-routed models.
    """
    return f"20 degrees {units} in {city}"


def test_defaulted_param_tool_is_accepted_across_providers():
    # Sanity-check the schema we're about to send is the strict shape under test.
    assert get_weather.schema["strict"] is True
    assert "units" in get_weather.schema["parameters"]["required"]
    assert get_weather.schema["parameters"]["properties"]["units"] == {
        "anyOf": [{"type": "string"}, {"type": "null"}]
    }


@pytest.mark.parametrize("model", MODELS)
def test_responses_api_accepts_defaulted_param_tool(model: str):
    client = Orq(api_key=os.environ["ORQ_API_KEY"])

    # Reaching a non-error response is the assertion: before the fix, openai/*
    # rejected this tool schema with a 400 at request time.
    response = client.responses.create(
        model=model,
        input="What is the weather in Paris? Use the get_weather tool.",
        tools=[get_weather],
    )

    assert response is not None


def test_pre_fix_schema_still_400s_on_openai():
    """Regression guard: proves the live suite actually catches the original bug.

    This is the schema shape the code produced before the fix — a defaulted param
    omitted from `required` under strict=True. OpenAI-routed models reject it with a
    400; if `_make_nullable`/required handling ever regresses to this shape, the
    positive test above would start failing for the same reason.
    """
    client = Orq(api_key=os.environ["ORQ_API_KEY"])
    pre_fix_tool = {
        "type": "function",
        "name": "get_weather",
        "description": "Return the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}, "units": {"type": "string"}},
            "required": ["city"],  # units omitted -> invalid under strict
            "additionalProperties": False,
        },
        "strict": True,
    }

    with pytest.raises(Exception, match="400"):
        client.responses.create(
            model="openai/gpt-4o",
            input="What is the weather in Paris?",
            tools=[pre_fix_tool],
        )
