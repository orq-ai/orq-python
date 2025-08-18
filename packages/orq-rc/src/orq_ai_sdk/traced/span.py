"""Span implementation for Orq tracing."""

import time
from typing import Any, Dict, List, Optional, Union, TypedDict
from dataclasses import dataclass, field

from .utils import serialize_value, validate_span_type, get_current_time_iso


class CompletionTokensDetails(TypedDict, total=False):
    """Type definition for completion tokens details."""
    accepted_prediction_tokens: int
    reasoning_tokens: int
    rejected_prediction_tokens: int


class PromptTokensDetails(TypedDict, total=False):
    """Type definition for prompt tokens details."""
    cached_tokens: int


class Metrics(TypedDict, total=False):
    """Type definition for metrics in span logging."""
    prompt_tokens: int
    completion_tokens: int
    tokens: int
    completion_tokens_details: CompletionTokensDetails
    prompt_tokens_details: PromptTokensDetails


class Request(TypedDict, total=False):
    """Type definition for AI request parameters."""
    provider: str
    model: str
    temperature: float
    top_p: float
    max_tokens: int
    frequency_penalty: float
    presence_penalty: float
    seed: Union[str, int]


@dataclass
class Event:
    """Represents an event within a span."""
    name: str
    timestamp: str
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Span:
    """Represents a single span in a trace."""
    
    # Context
    trace_id: str
    span_id: str
    parent_id: Optional[str] = None
    session_id: Optional[str] = None
    user_id: Optional[str] = None
    
    # Core attributes
    name: str = ""
    type: str = "function"
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    
    # Data
    input: Any = None
    output: Any = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    events: List[Event] = field(default_factory=list)
    
    # Runtime
    _id: Optional[str] = None
    
    def __post_init__(self):
        """Initialize span with current time if not provided and validate type."""
        if not self.start_time:
            self.start_time = get_current_time_iso()
        
        # Validate span type
        self.type = validate_span_type(self.type)
    
    def set_input(self, input_data: Any) -> None:
        """Set the input data for the span."""
        self.input = input_data
    
    def set_output(self, output_data: Any) -> None:
        """Set the output data for the span."""
        self.output = output_data
    
    def set_attribute(self, key: str, value: Any) -> None:
        """Set a single attribute."""
        self.attributes[key] = value
    
    def set_attributes(self, attributes: Dict[str, Any]) -> None:
        """Set multiple attributes."""
        self.attributes.update(attributes)
    
    def add_event(self, name: str, attributes: Optional[Dict[str, Any]] = None) -> None:
        """Add an event to the span."""
        event = Event(
            name=name,
            timestamp=get_current_time_iso(),
            attributes=attributes or {}
        )
        self.events.append(event)
    
    def end(self, end_time: Optional[str] = None) -> None:
        """End the span with the given or current time."""
        if not end_time:
            end_time = get_current_time_iso()
        self.end_time = end_time
    
    def log(self, input: Any = None, output: Any = None, metrics: Optional[Metrics] = None, metadata: Optional[Dict[str, Any]] = None, request: Optional[Request] = None) -> None:  # pylint: disable=redefined-builtin
        """Log input, output, metrics, metadata, provider, and model to the span."""
        if input is not None:
            self.set_input(input)
        
        if output is not None:
            self.set_output(output)
        
        if metrics is not None:
            self.set_attribute("metrics", metrics)

        if request is not None:
            self.set_attribute("request", request)
        
        if metadata is not None:
            self.set_attribute("metadata", metadata)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert span to dictionary for API submission."""
        span_dict = {
            "context": {
                "trace_id": self.trace_id,
                "span_id": self.span_id,
            },
            "name": self.name,
            "type": self.type,
            "start_time": self.start_time,
            "end_time": self.end_time or str(int(time.time() * 1000)),
            "attributes": serialize_value(self.attributes),
            "events": [
                {
                    "name": event.name,
                    "timestamp": event.timestamp,
                    "attributes": serialize_value(event.attributes)
                }
                for event in self.events
            ]
        }
        
        # Add optional fields
        if self._id:
            span_dict["_id"] = self._id
        
        if self.parent_id:
            span_dict["parent_id"] = self.parent_id
        
        if self.session_id:
            span_dict["context"]["session_id"] = self.session_id
        
        if self.user_id:
            span_dict["context"]["user_id"] = self.user_id
        
        if self.input is not None:
            span_dict["input"] = serialize_value(self.input)
        
        if self.output is not None:
            span_dict["output"] = serialize_value(self.output)
        
        return span_dict
