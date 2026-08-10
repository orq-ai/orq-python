# ListSmartRoutersResponse


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `object`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | Object type for this collection. Always `list`.                                 |
| `data`                                                                          | List[[models.SmartRouter](../models/smartrouter.md)]                            | :heavy_check_mark:                                                              | Smart Routers in the current page.                                              |
| `has_more`                                                                      | *bool*                                                                          | :heavy_check_mark:                                                              | Whether more Smart Routers are available in the requested pagination direction. |