# AlertRun


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Time of the evaluation tick.                                         |
| `value`                                                              | *float*                                                              | :heavy_check_mark:                                                   | Observed metric value. Zero when `has_data` is false.                |
| `breached`                                                           | *bool*                                                               | :heavy_check_mark:                                                   | Whether the value breached the alert condition.                      |
| `has_data`                                                           | *bool*                                                               | :heavy_check_mark:                                                   | Whether the evaluation window contained any data.                    |
| `severity`                                                           | [Optional[models.Severity]](../models/severity.md)                   | :heavy_minus_sign:                                                   | Tier the value landed in when breached. Empty when not breached.     |