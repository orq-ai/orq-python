# RunStats

Execution totals of a run. Not reset when the run is executed again.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `total_cost`                                                          | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Total cost in USD of the successful prompt and agent cell executions. |
| `total_errors`                                                        | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Number of failed prompt and agent cell executions.                    |
| `total_done`                                                          | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Number of successful prompt and agent cell executions.                |