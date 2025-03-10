# Message1


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `type`                                                         | [models.MessageType](../models/messagetype.md)                 | :heavy_check_mark:                                             | N/A                                                            |
| `role`                                                         | [models.MessageRole](../models/messagerole.md)                 | :heavy_check_mark:                                             | The role of the prompt message                                 |
| `tool_calls`                                                   | List[[models.MessageToolCalls](../models/messagetoolcalls.md)] | :heavy_check_mark:                                             | N/A                                                            |
| `content`                                                      | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |