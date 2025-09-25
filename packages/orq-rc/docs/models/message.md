# Message

The A2A format message containing the task for the agent to perform.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `message_id`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Optional A2A message ID in ULID format                           |
| `role`                                                           | [models.RunAgentRole](../models/runagentrole.md)                 | :heavy_check_mark:                                               | Message role (user or tool for continuing executions)            |
| `parts`                                                          | List[[models.PublicMessagePart](../models/publicmessagepart.md)] | :heavy_check_mark:                                               | A2A message parts (text, file, or tool_result only)              |