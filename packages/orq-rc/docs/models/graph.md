# Graph

Agent state-machine graph ({ nodes, edges }) attached to the root trace span. Present for LangGraph traces.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `nodes`                                  | List[[models.Nodes](../models/nodes.md)] | :heavy_check_mark:                       | N/A                                      |
| `edges`                                  | List[[models.Edges](../models/edges.md)] | :heavy_check_mark:                       | N/A                                      |