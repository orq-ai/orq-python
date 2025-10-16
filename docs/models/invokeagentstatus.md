# InvokeAgentStatus

Task status information


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `state`                                                                | [models.InvokeAgentState](../models/invokeagentstate.md)               | :heavy_check_mark:                                                     | Current task state                                                     |
| `timestamp`                                                            | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | ISO timestamp of status update                                         |
| `message`                                                              | [Optional[models.InvokeAgentMessage]](../models/invokeagentmessage.md) | :heavy_minus_sign:                                                     | Optional status message                                                |