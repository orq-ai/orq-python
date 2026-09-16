# QueryReportRequestMode

Value shaping. `timeseries` (default) buckets by time; `scalar` returns one aggregated row per group over the whole window, ordered by value (top list), or a single row when `group_by` is empty.

## Example Usage

```python
from orq_ai_sdk.models import QueryReportRequestMode
value: QueryReportRequestMode = "timeseries"
```


## Values

- `"timeseries"`
- `"scalar"`
