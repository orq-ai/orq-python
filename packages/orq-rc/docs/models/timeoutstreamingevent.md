# TimeoutStreamingEvent

Emitted when the agent stream exceeds the configured timeout duration. Contains a message describing the timeout condition.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `type`                                                                     | [models.TimeoutStreamingEventType](../models/timeoutstreamingeventtype.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `timestamp`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | ISO timestamp of the event                                                 |
| `data`                                                                     | [models.TimeoutStreamingEventData](../models/timeoutstreamingeventdata.md) | :heavy_check_mark:                                                         | N/A                                                                        |