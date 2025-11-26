# AgentErroredStreamingEvent

Emitted when an error occurs during agent execution. Contains the error message and HTTP status code indicating the failure type.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [models.AgentErroredStreamingEventType](../models/agenterroredstreamingeventtype.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `timestamp`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | ISO timestamp of the event                                                           |
| `data`                                                                               | [models.AgentErroredStreamingEventData](../models/agenterroredstreamingeventdata.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |