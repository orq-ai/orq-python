# A2AMessage

The A2A message to send to the agent (user input or tool results)


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `message_id`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Optional A2A message ID in ULID format                           |
| `role`                                                           | [models.InvokeAgentRole](../models/invokeagentrole.md)           | :heavy_check_mark:                                               | Message role (user or tool for continuing executions)            |
| `parts`                                                          | List[[models.PublicMessagePart](../models/publicmessagepart.md)] | :heavy_check_mark:                                               | A2A message parts (text, file, or tool_result only)              |