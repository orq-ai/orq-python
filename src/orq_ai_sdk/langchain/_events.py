"""In-flight event storage with cleanup."""

from typing import Dict, Optional

from ._models import InFlightEvent


class Events:
    """Tracks state between on_*_start and on_*_end callbacks.

    All dicts are instance-level (not class-level) to avoid sharing across instances.
    """

    def __init__(self) -> None:
        self._events: Dict[str, InFlightEvent] = {}
        self._parent_map: Dict[str, Optional[str]] = {}

    def store(self, run_id: str, event: InFlightEvent) -> None:
        self._events[run_id] = event

    def get(self, run_id: str) -> Optional[InFlightEvent]:
        return self._events.get(run_id)

    def remove(self, run_id: str) -> None:
        """Remove event after it's been sent to prevent memory leaks."""
        self._events.pop(run_id, None)

    def map_parent(self, run_id: str, parent_run_id: Optional[str]) -> None:
        self._parent_map[run_id] = parent_run_id

    def get_trace_id(self, run_id: str) -> str:
        """Walk up the parent chain to find the root run_id (= trace_id)."""
        parent = self._parent_map.get(run_id)
        if parent is None:
            return run_id
        return self.get_trace_id(parent)

    def cleanup_parent(self, run_id: str) -> None:
        """Remove parent mapping after event is done."""
        self._parent_map.pop(run_id, None)
