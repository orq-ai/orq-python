# Input2

An input item. The "type" field determines the item kind.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `content`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | The content of the item.                             |
| `id`                                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | The ID of the item.                                  |
| `role`                                               | [Optional[models.InputRole]](../models/inputrole.md) | :heavy_minus_sign:                                   | The role of the message sender (for message items).  |
| `type`                                               | [Optional[models.InputType]](../models/inputtype.md) | :heavy_minus_sign:                                   | The type of item.                                    |