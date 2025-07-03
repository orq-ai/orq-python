"""Span implementation for Orq tracing."""

import time
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field

from decorator.utils import get_current_time_iso, serialize_value
from decorator.types import SpanType


# TODO: event


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
    type: Union[SpanType, str] = SpanType.Generic
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    
    # Data
    input: Any = None
    output: Any = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    events: List[Event] = field(default_factory=list)
    
    # Runtime
    _start_time_unix: Optional[float] = field(default=None, init=False)
    _id: Optional[str] = None
    
    def __post_init__(self):
        """Initialize span with current time if not provided."""
        if not self.start_time:
            self.start_time = get_current_time_iso()
            self._start_time_unix = time.time()
    
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
    
    # TODO add_event function
    
    def end(self, end_time: Optional[str] = None) -> None:
        """End the span with the given or current time."""
        if not end_time:
            end_time = get_current_time_iso()
        self.end_time = end_time
    
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
            "end_time": self.end_time or get_current_time_iso(),
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
            span_dict["context"]["parent_id"] = self.parent_id
        
        if self.session_id:
            span_dict["context"]["session_id"] = self.session_id
        
        if self.user_id:
            span_dict["context"]["user_id"] = self.user_id
        
        if self.input is not None:
            span_dict["input"] = serialize_value(self.input)
        
        if self.output is not None:
            span_dict["output"] = serialize_value(self.output)
        
        return span_dict