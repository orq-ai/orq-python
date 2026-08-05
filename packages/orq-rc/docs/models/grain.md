# Grain

Requested bucket grain. Use `auto` or omit the field to let the server choose based on the requested range.

## Example Usage

```python
from orq_ai_sdk.models import Grain
value: Grain = "auto"
```


## Values

- `"auto"`
- `"minute"`
- `"hour"`
- `"day"`
