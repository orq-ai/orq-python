# MetricBaseline

Comparison with the baseline run.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `avg`                                                                               | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | Average of the baseline run.                                                        |
| `delta`                                                                             | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | This run's average minus the baseline average.                                      |
| `pct_change`                                                                        | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | `delta` as a percentage of the baseline average; 0 when the baseline<br/> average is 0. |
| `direction`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | `up`, `down` or `same`, by the sign of `delta`.                                     |