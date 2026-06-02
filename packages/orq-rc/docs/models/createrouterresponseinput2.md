# CreateRouterResponseInput2

An input item. The "type" field determines the item kind: "message", "function_call_output", "item_reference", etc.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `call_id`                                                                       | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The ID of the function call being responded to (for function_call_output type). |
| `content`                                                                       | [Optional[models.InputContent]](../models/inputcontent.md)                      | :heavy_minus_sign:                                                              | The content of the item: a string or an array of content parts.                 |
| `id`                                                                            | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The ID of the item (for item_reference type).                                   |
| `output`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The output of the function call (for function_call_output type).                |
| `role`                                                                          | [Optional[models.InputRole]](../models/inputrole.md)                            | :heavy_minus_sign:                                                              | The role of the message sender (for message items).                             |
| `type`                                                                          | [Optional[models.InputType]](../models/inputtype.md)                            | :heavy_minus_sign:                                                              | The type of item.                                                               |