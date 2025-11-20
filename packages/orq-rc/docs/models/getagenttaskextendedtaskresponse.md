# GetAgentTaskExtendedTaskResponse

Agent task execution response format with full conversation history and artifacts. Used for API responses when retrieving task details.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique task execution identifier                                     |
| `context_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Correlation ID for tracking                                          |
| `kind`                                                               | [models.GetAgentTaskKind](../models/getagenttaskkind.md)             | :heavy_check_mark:                                                   | A2A entity type                                                      |
| `status`                                                             | [models.GetAgentTaskTaskStatus](../models/getagenttasktaskstatus.md) | :heavy_check_mark:                                                   | Current task execution status                                        |
| `history`                                                            | List[[models.ExtendedA2AMessage](../models/extendeda2amessage.md)]   | :heavy_check_mark:                                                   | Conversation history with all messages exchanged                     |
| `artifacts`                                                          | List[[models.TaskArtifact](../models/taskartifact.md)]               | :heavy_minus_sign:                                                   | Optional files or data produced during execution                     |
| `metadata`                                                           | Dict[str, *Any*]                                                     | :heavy_minus_sign:                                                   | Additional task metadata                                             |