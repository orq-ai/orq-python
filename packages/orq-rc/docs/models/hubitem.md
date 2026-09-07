# HubItem


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | Unique hub item ID.                                      |
| `entity_id`                                              | *str*                                                    | :heavy_check_mark:                                       | ID of the workspace entity represented by this hub item. |
| `display_name`                                           | *str*                                                    | :heavy_check_mark:                                       | Human-readable hub item name.                            |
| `description`                                            | *str*                                                    | :heavy_check_mark:                                       | Hub item description.                                    |
| `type`                                                   | *str*                                                    | :heavy_check_mark:                                       | Hub item type.                                           |
| `is_active`                                              | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Whether a vendor hub item is active.                     |
| `is_private`                                             | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Whether a vendor hub item is private.                    |
| `is_provided_by_orq`                                     | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Whether the hub item is provided by orq.                 |
| `engine`                                                 | *Optional[str]*                                          | :heavy_minus_sign:                                       | Execution engine for vendor hub item templates.          |
| `key`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Stable vendor template key.                              |
| `evaluator`                                              | [Optional[models.Evaluator]](../models/evaluator.md)     | :heavy_minus_sign:                                       | Evaluator template payload.                              |
| `prompt`                                                 | [Optional[models.Prompt]](../models/prompt.md)           | :heavy_minus_sign:                                       | Prompt template payload.                                 |