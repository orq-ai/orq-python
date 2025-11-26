# AgentInactiveStreamingEvent

Emitted when the agent completes processing or pauses for input. Contains the final message, finish reason (stop, tool_calls, max_iterations, etc.), and any pending tool calls awaiting user response.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type`                                                                                 | [models.AgentInactiveStreamingEventType](../models/agentinactivestreamingeventtype.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `timestamp`                                                                            | *str*                                                                                  | :heavy_check_mark:                                                                     | ISO timestamp of the event                                                             |
| `data`                                                                                 | [models.AgentInactiveStreamingEventData](../models/agentinactivestreamingeventdata.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |