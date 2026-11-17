# Input2

An input item. The "type" field determines the item kind.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `author`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The path of the agent that sent the message (for agent_message items).       |
| `content`                                                                    | [Optional[models.InputContent]](../models/inputcontent.md)                   | :heavy_minus_sign:                                                           | The content of the item: a string or an array of content parts.              |
| `id`                                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The ID of the item.                                                          |
| `recipient`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The path of the agent the message is addressed to (for agent_message items). |
| `role`                                                                       | [Optional[models.InputRole]](../models/inputrole.md)                         | :heavy_minus_sign:                                                           | The role of the message sender (for message items).                          |
| `type`                                                                       | [Optional[models.InputType]](../models/inputtype.md)                         | :heavy_minus_sign:                                                           | The type of item.                                                            |