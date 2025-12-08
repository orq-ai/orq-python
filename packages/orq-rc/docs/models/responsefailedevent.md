# ResponseFailedEvent

Emitted when an error occurs during agent execution. Contains error details.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.ResponseFailedEventType](../models/responsefailedeventtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `timestamp`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ISO timestamp of when the event occurred                               |
| `data`                                                                 | [models.ResponseFailedEventData](../models/responsefailedeventdata.md) | :heavy_check_mark:                                                     | N/A                                                                    |