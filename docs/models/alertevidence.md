# AlertEvidence


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `trace_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Trace the exemplar span belongs to.                                  |
| `span_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Exemplar span ID.                                                    |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Start time of the exemplar span.                                     |
| `value`                                                              | *float*                                                              | :heavy_check_mark:                                                   | Metric contribution of the exemplar (e.g. cost or duration).         |