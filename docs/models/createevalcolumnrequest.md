# CreateEvalColumnRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `evaluator_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | ID of the evaluator to add. Each row gets one evaluator cell per task<br/> column. |
| `position`                                                                     | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | 0-based position among the run's columns. Defaults to the end.                 |