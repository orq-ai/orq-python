# SyncMcpToolResponseBodySchema

The schema for the response format, described as a JSON Schema object. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `type`                                   | *str*                                    | :heavy_check_mark:                       | The JSON Schema type                     |
| `properties`                             | Dict[str, *Any*]                         | :heavy_check_mark:                       | The properties of the JSON Schema object |
| `required`                               | List[*str*]                              | :heavy_check_mark:                       | Array of required property names         |
| `__pydantic_extra__`                     | Dict[str, *Any*]                         | :heavy_minus_sign:                       | N/A                                      |