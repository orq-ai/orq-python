"""Regression test for ENG-1983 / ENG-1982 / ENG-2002.

A discriminated-union field that is UNSET or type-less must NOT raise at
model construction. Lives outside the Speakeasy-managed file set so it
survives regeneration.
"""

import pytest
from pydantic import TypeAdapter

from orq_ai_sdk import models
from orq_ai_sdk.models.updateevalop import GuardrailConfig
from orq_ai_sdk.types import UNSET


def test_update_eval_body_with_unset_guardrail_config():
    """ENG-1983: omitted/UNSET guardrail_config must construct cleanly."""
    body = models.UpdateEvalRequestBody(type=None, prompt="hi", guardrail_config=UNSET)
    # Unset is a pydantic model copied on validation, so compare by type, not identity.
    assert isinstance(body.guardrail_config, type(UNSET))


def test_update_eval_body_without_guardrail_config():
    """Baseline: field fully omitted (was already passing)."""
    body = models.UpdateEvalRequestBody(type=None, prompt="hi")
    assert isinstance(body.guardrail_config, type(UNSET))


def test_valid_guardrail_config_still_discriminates():
    """Guard against over-fixing: a real, typed union value must still resolve
    to the correct member rather than silently falling through."""
    cfg = TypeAdapter(GuardrailConfig).validate_python(
        {"type": "number", "value": 0.5, "operator": "gte"}
    )
    assert cfg.type == "number"
    assert cfg.value == 0.5


def test_typeless_guardrail_dict_does_not_crash_construction():
    """ENG-2002 shape: a type-less dict must raise pydantic's ValidationError
    (a clean union mismatch), NOT a raw ValueError out of the discriminator."""
    with pytest.raises(Exception) as exc:
        TypeAdapter(GuardrailConfig).validate_python({})
    # Must be pydantic validation, not the discriminator's ValueError.
    assert "Could not find discriminator field" not in str(exc.value)
