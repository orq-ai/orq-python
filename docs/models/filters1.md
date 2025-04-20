# Filters1


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `operator`                                               | [models.FiltersOperator](../models/filtersoperator.md)   | :heavy_check_mark:                                       | N/A                                                      |
| `value`                                                  | *Optional[Any]*                                          | :heavy_minus_sign:                                       | N/A                                                      |
| `type`                                                   | [models.FiltersType](../models/filterstype.md)           | :heavy_check_mark:                                       | N/A                                                      |
| `options`                                                | List[[models.Options](../models/options.md)]             | :heavy_check_mark:                                       | N/A                                                      |
| `options_map`                                            | Dict[str, [models.OptionsMap](../models/optionsmap.md)]  | :heavy_minus_sign:                                       | N/A                                                      |
| `image_url_map`                                          | Dict[str, *str*]                                         | :heavy_minus_sign:                                       | N/A                                                      |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `path`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `hide_operators`                                         | List[[models.HideOperators](../models/hideoperators.md)] | :heavy_minus_sign:                                       | N/A                                                      |