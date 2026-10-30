# GetRunMetricsResponse


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `metrics`                                                     | Dict[str, [models.MetricSummary](../models/metricsummary.md)] | :heavy_minus_sign:                                            | Keyed "{task_column_id}_{metric_id}" like Run.metrics.        |