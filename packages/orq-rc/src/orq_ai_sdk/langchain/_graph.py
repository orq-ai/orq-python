"""Graph tracker for building a graph view from LangChain callbacks.

Tracks LangGraph node executions and builds a graph data structure
(nodes + edges) that gets attached to the root trace span. The frontend
can then render a visual state machine graph.

Graph nodes are detected as chain callbacks whose parent is the root chain
(the LangGraph graph itself). Each node stores the span IDs of all its
invocations. Edges are built from the execution order of these nodes.
"""

import json
from typing import Any, Dict, List, Optional


class GraphTracker:
    """Builds a graph from LangGraph chain callback execution order.

    Usage:
        tracker = GraphTracker()
        tracker.on_node_start("__start__", span_id, root_run_id)
        tracker.on_node_end("__start__", root_run_id)
        tracker.on_node_start("agent", span_id, root_run_id)
        ...
        graph_json = tracker.build()  # returns JSON string
    """

    def __init__(self) -> None:
        # node_id -> {"type": str, "span_ids": [str]}
        self._nodes: Dict[str, Dict[str, Any]] = {}
        # [(source, target)] — deduplicated edges
        self._edges: List[tuple] = []
        # root run_id -> last completed node_id (for edge tracking)
        self._last_completed: Dict[str, Optional[str]] = {}
        # root run_id -> currently active node_id
        self._active_node: Dict[str, Optional[str]] = {}

    def on_node_start(self, node_id: str, span_id: str, root_run_id: str) -> None:
        """Register a graph node starting execution."""
        # Determine node type
        if node_id == "__start__":
            node_type = "start"
        elif node_id == "__end__":
            node_type = "end"
        else:
            node_type = "chain"

        # Create node if first time, or append span_id
        if node_id not in self._nodes:
            self._nodes[node_id] = {"type": node_type, "span_ids": []}
        self._nodes[node_id]["span_ids"].append(span_id)

        # Build edge from last completed node to this one
        last = self._last_completed.get(root_run_id)
        if last is not None:
            edge = (last, node_id)
            if edge not in self._edges:
                self._edges.append(edge)

        self._active_node[root_run_id] = node_id

    def on_node_end(self, node_id: str, root_run_id: str) -> None:
        """Mark a graph node as completed (for edge tracking)."""
        self._last_completed[root_run_id] = node_id
        if self._active_node.get(root_run_id) == node_id:
            self._active_node[root_run_id] = None

    def has_nodes(self) -> bool:
        """Return True if any graph nodes have been registered."""
        return len(self._nodes) > 0

    def build(self, root_run_id: str, root_span_id: str) -> str:
        """Build the graph JSON string to attach as a span attribute.

        If LangGraph did not emit explicit ``__start__`` / ``__end__`` chain
        events (the common case in Python), synthesize them and anchor their
        span_ids to the root span so the UI always has clean entry/exit markers.
        """
        node_items: List[tuple] = []  # (id, type, span_ids)
        edges: List[tuple] = list(self._edges)

        if self._nodes and "__start__" not in self._nodes:
            first = next(iter(self._nodes))
            node_items.append(("__start__", "start", [root_span_id]))
            edges.insert(0, ("__start__", first))

        for node_id, info in self._nodes.items():
            node_items.append((node_id, info["type"], info["span_ids"]))

        if self._nodes and "__end__" not in self._nodes:
            last = self._last_completed.get(root_run_id)
            if last:
                node_items.append(("__end__", "end", [root_span_id]))
                edges.append((last, "__end__"))

        nodes_out = [
            {"id": nid, "type": ntype, "span_ids": sids}
            for nid, ntype, sids in node_items
        ]
        edges_out = [{"source": s, "target": t} for s, t in edges]
        return json.dumps({"nodes": nodes_out, "edges": edges_out}, default=str)
