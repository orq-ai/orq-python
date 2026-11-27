# ExperimentRunRowDuplicateRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `experiment_id`                                                | *str*                                                          | :heavy_check_mark:                                             | ID of the experiment.                                          |
| `run_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | ID of the run.                                                 |
| `row_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | ID of the row to copy.                                         |
| `duplicate_row_request`                                        | [models.DuplicateRowRequest](../models/duplicaterowrequest.md) | :heavy_check_mark:                                             | N/A                                                            |