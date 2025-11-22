# InvokeAgentA2ATaskResponse

Response format following the Agent-to-Agent (A2A) protocol. Returned when starting or continuing an agent task execution.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | The unique ID of the created agent execution task                            |
| `context_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | The correlation ID for this execution (used for tracking)                    |
| `kind`                                                                       | [models.InvokeAgentKind](../models/invokeagentkind.md)                       | :heavy_check_mark:                                                           | A2A entity type identifier                                                   |
| `status`                                                                     | [models.TaskStatus](../models/taskstatus.md)                                 | :heavy_check_mark:                                                           | Current task status information                                              |
| `metadata`                                                                   | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | Task metadata containing workspace_id and trace_id for feedback and tracking |