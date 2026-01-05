# ToolStartedEvent

Emitted when a tool begins execution. Contains tool details and input arguments.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `type`                                                           | [models.ToolStartedEventType](../models/toolstartedeventtype.md) | :heavy_check_mark:                                               | N/A                                                              |
| `timestamp`                                                      | *str*                                                            | :heavy_check_mark:                                               | ISO timestamp of when the event occurred                         |
| `data`                                                           | [models.ToolStartedEventData](../models/toolstartedeventdata.md) | :heavy_check_mark:                                               | N/A                                                              |