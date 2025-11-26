# AgentHandedOffStreamingEvent

Emitted when control is transferred to a sub-agent. Contains the target agent ID and the input message for the handoff.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `type`                                                                                   | [models.AgentHandedOffStreamingEventType](../models/agenthandedoffstreamingeventtype.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `timestamp`                                                                              | *str*                                                                                    | :heavy_check_mark:                                                                       | ISO timestamp of the event                                                               |
| `data`                                                                                   | [models.AgentHandedOffStreamingEventData](../models/agenthandedoffstreamingeventdata.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |