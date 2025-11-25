# AgentStartedStreamingEvent

Emitted when the agent begins processing. Contains configuration details including the model, instructions, system prompt, and input message.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [models.AgentStartedStreamingEventType](../models/agentstartedstreamingeventtype.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `timestamp`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | ISO timestamp of the event                                                           |
| `data`                                                                               | [models.AgentStartedStreamingEventData](../models/agentstartedstreamingeventdata.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |