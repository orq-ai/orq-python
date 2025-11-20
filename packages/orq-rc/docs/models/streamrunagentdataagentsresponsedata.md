# StreamRunAgentDataAgentsResponseData


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `last_message`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `finish_reason`                                                             | [models.FinishReason](../models/finishreason.md)                            | :heavy_check_mark:                                                          | The reason why the agent execution became inactive                          |
| `pending_tool_calls`                                                        | List[[models.PendingToolCalls](../models/pendingtoolcalls.md)]              | :heavy_minus_sign:                                                          | Tool calls that are pending user response (for function_call finish reason) |