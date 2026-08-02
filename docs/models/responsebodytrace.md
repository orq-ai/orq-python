# ResponseBodyTrace

Trace-specific metadata


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `framework`                                                                                                 | [Optional[models.ResponseBodyFramework]](../models/responsebodyframework.md)                                | :heavy_minus_sign:                                                                                          | Framework or platform that generated the trace                                                              |
| `graph`                                                                                                     | [Optional[models.ResponseBodyGraph]](../models/responsebodygraph.md)                                        | :heavy_minus_sign:                                                                                          | Agent state-machine graph ({ nodes, edges }) attached to the root trace span. Present for LangGraph traces. |