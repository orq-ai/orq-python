"""In-flight event storage with cleanup."""

from typing import Dict, Optional

from ._graph import GraphTracker
from ._models import InFlightEvent


class Events:
    """Tracks state between on_*_start and on_*_end callbacks.

    Uses LangChain UUIDs directly (hyphens stripped) as trace/span IDs.
    All dicts are instance-level to avoid sharing across instances.
    """

    def __init__(self) -> None:
        self._events: Dict[str, InFlightEvent] = {}
        self._parent_map: Dict[str, Optional[str]] = {}  # run_id -> parent_run_id
        self._root_run_id: Optional[str] = None  # first chain with no parent
        self.graph: GraphTracker = GraphTracker()

    def store(self, run_id: str, event: InFlightEvent) -> None:
        self._events[run_id] = event

    def get(self, run_id: str) -> Optional[InFlightEvent]:
        return self._events.get(run_id)

    def remove(self, run_id: str) -> None:
        self._events.pop(run_id, None)

    def map_parent(self, run_id: str, parent_run_id: Optional[str]) -> None:
        self._parent_map[run_id] = parent_run_id

    def get_trace_id(self, run_id: str) -> str:
        """Walk up the parent chain to find the root run_id (= trace_id)."""
        root = self._get_root(run_id)
        return root.replace("-", "")

    def get_span_id(self, run_id: str) -> str:
        """Return run_id with hyphens stripped."""
        return run_id.replace("-", "")

    def set_root_if_needed(self, run_id: str) -> None:
        """Set the root run_id if not already set (first parentless chain)."""
        if self._root_run_id is None:
            self._root_run_id = run_id

    def is_root(self, run_id: str) -> bool:
        """Check if this run_id is the root chain."""
        return run_id == self._root_run_id

    def is_graph_node(self, run_id: str) -> bool:
        """Check if this chain's parent is the root (= a LangGraph node)."""
        parent = self._parent_map.get(run_id)
        return parent is not None and parent == self._root_run_id

    @property
    def root_run_id(self) -> Optional[str]:
        return self._root_run_id

    def _get_root(self, run_id: str) -> str:
        parent = self._parent_map.get(run_id)
        if parent is None:
            return run_id
        return self._get_root(parent)
