# BooleanMetricSummary

Statistics of a pass or fail metric.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `passed_rate`                                                        | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | Percentage of rows that passed, 0 to 100, rounded to a whole number. |
| `count`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Number of rows with a value.                                         |