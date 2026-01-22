# Tools1

A function tool definition


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | [models.ToolsType](../models/toolstype.md)                               | :heavy_check_mark:                                                       | The type of tool                                                         |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | The name of the function to be called                                    |
| `description`                                                            | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | A description of what the function does                                  |
| `parameters`                                                             | [models.ToolsParameters](../models/toolsparameters.md)                   | :heavy_check_mark:                                                       | The parameters the function accepts                                      |
| `strict`                                                                 | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether to enable strict schema adherence when generating function calls |