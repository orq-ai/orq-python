# ExperimentTaskUpdateRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `experiment_id`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | ID of the experiment.                                                  |
| `run_id`                                                               | *str*                                                                  | :heavy_check_mark:                                                     | ID of the run.                                                         |
| `task_id`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | ID of the task column.                                                 |
| `update_task_column_request`                                           | [models.UpdateTaskColumnRequest](../models/updatetaskcolumnrequest.md) | :heavy_check_mark:                                                     | N/A                                                                    |