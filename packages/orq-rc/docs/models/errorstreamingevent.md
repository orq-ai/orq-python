# ErrorStreamingEvent

Emitted when a streaming error occurs outside of normal agent execution. Contains the error message and error code for debugging.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.ErrorStreamingEventType](../models/errorstreamingeventtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `timestamp`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ISO timestamp of the event                                             |
| `data`                                                                 | [models.ErrorStreamingEventData](../models/errorstreamingeventdata.md) | :heavy_check_mark:                                                     | N/A                                                                    |