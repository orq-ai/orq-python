# ToolsParameters

The parameters the function accepts


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.CreateResponseToolsType](../models/createresponsetoolstype.md) | :heavy_check_mark:                                                     | The type of the parameters object                                      |
| `properties`                                                           | Dict[str, [models.Properties](../models/properties.md)]                | :heavy_check_mark:                                                     | The parameters the function accepts, described as a JSON Schema object |
| `required`                                                             | List[*str*]                                                            | :heavy_minus_sign:                                                     | List of required parameter names                                       |
| `additional_properties`                                                | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Whether to allow properties not defined in the schema                  |