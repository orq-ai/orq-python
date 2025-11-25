# ExecutionNamedStreamingEvent

Emitted when the agent execution is assigned a human-readable name, typically generated based on the conversation content.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `type`                                                                                   | [models.ExecutionNamedStreamingEventType](../models/executionnamedstreamingeventtype.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `timestamp`                                                                              | *str*                                                                                    | :heavy_check_mark:                                                                       | ISO timestamp of the event                                                               |
| `data`                                                                                   | [models.ExecutionNamedStreamingEventData](../models/executionnamedstreamingeventdata.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |