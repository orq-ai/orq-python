# SearchRetrievalConfigRerankConfig

Override reranking for this retrieval configuration. Omit to inherit stored settings or set to null to disable reranking.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `enabled`                                                        | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | N/A                                                              |
| `provider`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `top_k`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `model`                                                          | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `model_db_id`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `model_type`                                                     | [Optional[models.ModelType]](../models/modeltype.md)             | :heavy_minus_sign:                                               | N/A                                                              |
| `model_parameters`                                               | [Optional[models.ModelParameters]](../models/modelparameters.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `integration_id`                                                 | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | N/A                                                              |