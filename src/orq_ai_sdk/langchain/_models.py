"""Internal event models for in-flight state tracking between start/end callbacks."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class EventType(str, Enum):
    AGENT = "agent"
    CHAIN = "chain"
    LLM = "llm"
    RETRIEVAL = "retrieval"
    TOOL = "tool"


@dataclass
class InFlightEvent:
    """Tracks state between on_*_start and on_*_end callbacks.

    Not sent to the API directly -- converted to OTLP spans by _span_builder.
    """

    run_id: str
    event_type: EventType
    name: str = ""
    parent_run_id: Optional[str] = None
    trace_id: Optional[str] = None

    # Timing
    start_time_iso: str = ""
    end_time_iso: Optional[str] = None

    # Serialized info from LangChain
    serialized: Dict[str, Any] = field(default_factory=dict)
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

    # LLM-specific
    messages: Optional[List[Dict[str, Any]]] = None  # normalized messages
    prompts: Optional[List[str]] = None
    model_name: Optional[str] = None
    model_parameters: Optional[Dict[str, Any]] = None
    token_usage: Optional[Dict[str, Any]] = None
    response_choices: Optional[List[Dict[str, Any]]] = None
    streaming_tokens: Optional[List[str]] = None  # accumulated from on_llm_new_token

    # Chain-specific
    inputs: Optional[Dict[str, Any]] = None
    outputs: Optional[Dict[str, Any]] = None

    # Tool-specific
    tool_input: Optional[str] = None
    tool_output: Optional[str] = None

    # Retrieval-specific
    query: Optional[str] = None
    documents: Optional[List[Dict[str, Any]]] = None

    # Agent-specific
    agent_actions: Optional[List[Dict[str, Any]]] = None
    agent_finish: Optional[Dict[str, Any]] = None

    # Error
    error: Optional[Dict[str, str]] = None
