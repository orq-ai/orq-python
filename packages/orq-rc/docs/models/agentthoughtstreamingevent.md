# AgentThoughtStreamingEvent

Emitted during agent reasoning. Contains the incremental message changes, model choices, iteration count, and token usage for this processing step.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [models.AgentThoughtStreamingEventType](../models/agentthoughtstreamingeventtype.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `timestamp`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | ISO timestamp of the event                                                           |
| `data`                                                                               | [models.AgentThoughtStreamingEventData](../models/agentthoughtstreamingeventdata.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |