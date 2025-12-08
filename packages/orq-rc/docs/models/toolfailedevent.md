# ToolFailedEvent

Emitted when a tool execution fails. Contains error details.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | [models.ToolFailedEventType](../models/toolfailedeventtype.md) | :heavy_check_mark:                                             | N/A                                                            |
| `timestamp`                                                    | *str*                                                          | :heavy_check_mark:                                             | ISO timestamp of when the event occurred                       |
| `data`                                                         | [models.ToolFailedEventData](../models/toolfailedeventdata.md) | :heavy_check_mark:                                             | N/A                                                            |