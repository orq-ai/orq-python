# Output3

A file search tool call output


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier for this output item                                             |
| `type`                                                                                 | [models.CreateResponseOutputProxyType](../models/createresponseoutputproxytype.md)     | :heavy_check_mark:                                                                     | The type of output item                                                                |
| `status`                                                                               | [models.CreateResponseOutputProxyStatus](../models/createresponseoutputproxystatus.md) | :heavy_check_mark:                                                                     | The status of the file search                                                          |
| `queries`                                                                              | List[*str*]                                                                            | :heavy_minus_sign:                                                                     | The search queries used                                                                |
| `results`                                                                              | *Optional[Any]*                                                                        | :heavy_minus_sign:                                                                     | The file search results                                                                |