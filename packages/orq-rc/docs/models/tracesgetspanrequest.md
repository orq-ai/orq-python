# TracesGetSpanRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `trace_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Optional: queue items predating trace_id capture only have the span. |
| `span_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `all_accessible_projects`                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Spans every project the caller belongs to instead of the active one. |