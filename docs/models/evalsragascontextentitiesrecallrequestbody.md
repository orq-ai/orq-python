# EvalsRagasContextEntitiesRecallRequestBody


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `reference`                                               | *str*                                                     | :heavy_check_mark:                                        | The ground truth answer to evaluate entity recall against |
| `retrievals`                                              | List[*str*]                                               | :heavy_minus_sign:                                        | Knowledge base retrievals containing entities to evaluate |
| `model`                                                   | *str*                                                     | :heavy_check_mark:                                        | N/A                                                       |