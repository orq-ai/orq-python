# RunAgentStatus

Task status information


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `state`                                                          | [models.RunAgentState](../models/runagentstate.md)               | :heavy_check_mark:                                               | Current task state                                               |
| `timestamp`                                                      | *Optional[str]*                                                  | :heavy_minus_sign:                                               | ISO timestamp of status update                                   |
| `message`                                                        | [Optional[models.RunAgentMessage]](../models/runagentmessage.md) | :heavy_minus_sign:                                               | Optional status message                                          |