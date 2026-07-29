# AlertTriggerEvent


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `event_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Unique event identifier, for example `alertevent_01H...`.            |
| `trigger_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Trigger the event was recorded on.                                   |
| `alert_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Alert the event belongs to.                                          |
| `at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Time of the evaluation tick.                                         |
| `value`                                                              | *float*                                                              | :heavy_check_mark:                                                   | Observed metric value at the tick.                                   |
| `evidence`                                                           | List[[models.AlertEvidence](../models/alertevidence.md)]             | :heavy_minus_sign:                                                   | Exemplar traces that contributed to the breach, worst first.         |