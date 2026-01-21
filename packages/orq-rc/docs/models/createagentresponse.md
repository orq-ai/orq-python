# CreateAgentResponse

Response type from the create-response endpoint.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | The unique response ID                                                  |
| `task_id`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | The agent execution task ID                                             |
| `output`                                                                | List[[models.AgentResponseMessage](../models/agentresponsemessage.md)]  | :heavy_check_mark:                                                      | Array of messages from the agent execution                              |
| `created_at`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | ISO timestamp of response creation                                      |
| `model`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | Model used in provider/model format                                     |
| `usage`                                                                 | [OptionalNullable[models.Usage]](../models/usage.md)                    | :heavy_minus_sign:                                                      | Token usage from the agent execution                                    |
| `finish_reason`                                                         | [Optional[models.FinishReason]](../models/finishreason.md)              | :heavy_minus_sign:                                                      | The reason why the agent stopped generating                             |
| `pending_tool_calls`                                                    | List[[models.PendingToolCalls](../models/pendingtoolcalls.md)]          | :heavy_minus_sign:                                                      | Tool calls awaiting user response (when finish_reason is function_call) |