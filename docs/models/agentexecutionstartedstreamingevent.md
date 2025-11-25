# AgentExecutionStartedStreamingEvent

Initial event emitted when an agent stream begins. Contains the task ID for tracking, workspace context, and trace ID for observability.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `type`                           | [models.Type](../models/type.md) | :heavy_check_mark:               | N/A                              |
| `timestamp`                      | *str*                            | :heavy_check_mark:               | ISO timestamp of the event       |
| `data`                           | [models.Data](../models/data.md) | :heavy_check_mark:               | N/A                              |