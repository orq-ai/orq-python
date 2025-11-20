# StreamAgentDataAgentsResponse200Data


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `last_message`                                                              | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `finish_reason`                                                             | [models.DataFinishReason](../models/datafinishreason.md)                    | :heavy_check_mark:                                                          | The reason why the agent execution became inactive                          |
| `pending_tool_calls`                                                        | List[[models.DataPendingToolCalls](../models/datapendingtoolcalls.md)]      | :heavy_minus_sign:                                                          | Tool calls that are pending user response (for function_call finish reason) |