# CreateSmartRouterRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `key`                                                                    | *str*                                                                    | :heavy_check_mark:                                                       | Required. Stable lowercase key containing letters, numbers, and hyphens. |
| `models`                                                                 | List[*str*]                                                              | :heavy_check_mark:                                                       | Required. Ordered pool of distinct models in provider/model format.      |
| `profile`                                                                | [models.SmartRouterProfile](../models/smartrouterprofile.md)             | :heavy_check_mark:                                                       | N/A                                                                      |