# DeploymentsTools


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `display_name`                                                 | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `type`                                                         | [models.DeploymentsType](../models/deploymentstype.md)         | :heavy_check_mark:                                             | The type of the tool. Currently, only `function` is supported. |
| `function`                                                     | [models.DeploymentsFunction](../models/deploymentsfunction.md) | :heavy_check_mark:                                             | N/A                                                            |
| `id`                                                           | *Optional[float]*                                              | :heavy_minus_sign:                                             | N/A                                                            |