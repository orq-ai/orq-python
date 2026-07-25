# QueryReportRequestGrain

Requested bucket grain. Use `auto` or omit the field to let the server choose based on the requested range.

## Example Usage

```python
from orq_ai_sdk.models import QueryReportRequestGrain
value: QueryReportRequestGrain = "auto"
```


## Values

- `"auto"`
- `"minute"`
- `"hour"`
- `"day"`
