# InvokeAgentResponseBody

A2A Task response format


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | The ID of the created agent execution task                      |
| `context_id`                                                    | *str*                                                           | :heavy_check_mark:                                              | The correlation ID for this execution                           |
| `kind`                                                          | [models.InvokeAgentKind](../models/invokeagentkind.md)          | :heavy_check_mark:                                              | A2A entity type                                                 |
| `status`                                                        | [models.InvokeAgentStatus](../models/invokeagentstatus.md)      | :heavy_check_mark:                                              | Task status information                                         |
| `metadata`                                                      | Dict[str, *Any*]                                                | :heavy_minus_sign:                                              | Task metadata containing workspace_id and trace_id for feedback |