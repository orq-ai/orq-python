# AgentResponseMessage

Response message from an agent execution.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `message_id`                             | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `role`                                   | [models.Role](../models/role.md)         | :heavy_check_mark:                       | N/A                                      |
| `parts`                                  | List[[models.Parts](../models/parts.md)] | :heavy_check_mark:                       | N/A                                      |
| `metadata`                               | Dict[str, *Any*]                         | :heavy_minus_sign:                       | N/A                                      |