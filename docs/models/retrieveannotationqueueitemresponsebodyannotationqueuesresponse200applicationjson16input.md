# RetrieveAnnotationQueueItemResponseBodyAnnotationQueuesResponse200ApplicationJSON16Input


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `evaluator_id`                                     | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `evaluator_type`                                   | [models.EvaluatorType](../models/evaluatortype.md) | :heavy_check_mark:                                 | N/A                                                |
| `eval_type`                                        | [Optional[models.EvalType]](../models/evaltype.md) | :heavy_minus_sign:                                 | N/A                                                |
| `output_type`                                      | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `expected_value`                                   | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `display_name`                                     | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `description`                                      | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `input`                                            | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |