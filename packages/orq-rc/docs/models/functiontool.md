# FunctionTool

Custom function tool with configurable parameters


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `type`                                                   | [models.FunctionToolType](../models/functiontooltype.md) | :heavy_check_mark:                                       | N/A                                                      |
| `id`                                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `key`                                                    | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `display_name`                                           | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `description`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `requires_approval`                                      | *Optional[bool]*                                         | :heavy_minus_sign:                                       | N/A                                                      |
| `function`                                               | [models.Function](../models/function.md)                 | :heavy_check_mark:                                       | N/A                                                      |