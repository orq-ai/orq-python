# ToolsFunction

A function tool the model can call.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `description`                                                                      | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | A description of what the function does.                                           |
| `name`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | The name of the function.                                                          |
| `parameters`                                                                       | [Optional[models.ToolsParameters]](../models/toolsparameters.md)                   | :heavy_minus_sign:                                                                 | The parameters the function accepts, as a JSON Schema object.                      |
| `strict`                                                                           | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether to enforce strict parameter validation.                                    |
| `type`                                                                             | [models.CreateRouterResponseToolsType](../models/createrouterresponsetoolstype.md) | :heavy_check_mark:                                                                 | N/A                                                                                |