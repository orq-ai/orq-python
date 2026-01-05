# ToolDoneEvent

Emitted when a tool completes execution successfully. Contains the tool result.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `type`                                                     | [models.ToolDoneEventType](../models/tooldoneeventtype.md) | :heavy_check_mark:                                         | N/A                                                        |
| `timestamp`                                                | *str*                                                      | :heavy_check_mark:                                         | ISO timestamp of when the event occurred                   |
| `data`                                                     | [models.ToolDoneEventData](../models/tooldoneeventdata.md) | :heavy_check_mark:                                         | N/A                                                        |