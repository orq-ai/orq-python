# QueryTelemetryRequestMode

Value shaping. `timeseries` buckets by grain; `scalar` returns one row per group. When omitted, grain selects the compatible shape.

## Example Usage

```python
from orq_ai_sdk.models import QueryTelemetryRequestMode
value: QueryTelemetryRequestMode = "timeseries"
```


## Values

- `"timeseries"`
- `"scalar"`
