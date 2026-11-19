# EvalColumnConfig

Configuration of an evaluator column. Name and types are read from the
 evaluator.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `evaluator_id`                                         | *Optional[str]*                                        | :heavy_minus_sign:                                     | ID of the evaluator.                                   |
| `evaluator_name`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | Evaluator display name.                                |
| `evaluator_type`                                       | *Optional[str]*                                        | :heavy_minus_sign:                                     | Evaluator type, such as `llm_eval` or `python_eval`.   |
| `evaluator_output_type`                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | Type of value the evaluator returns, such as `number`. |