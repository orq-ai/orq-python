# ToolExecutionFailedStreamingEvent

Emitted when a tool execution fails. Contains the error details, action type, and execution context.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `type`                                                                                             | [models.ToolExecutionFailedStreamingEventType](../models/toolexecutionfailedstreamingeventtype.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `timestamp`                                                                                        | *str*                                                                                              | :heavy_check_mark:                                                                                 | ISO timestamp of the event                                                                         |
| `data`                                                                                             | [models.ToolExecutionFailedStreamingEventData](../models/toolexecutionfailedstreamingeventdata.md) | :heavy_check_mark:                                                                                 | N/A                                                                                                |