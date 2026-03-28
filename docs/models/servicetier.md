# ServiceTier

Specifies the latency tier to use for processing the request. Defaults to "auto".

## Example Usage

```python
from orq_ai_sdk.models import ServiceTier
value: ServiceTier = "auto"
```


## Values

- `"auto"`
- `"default"`
- `"flex"`
- `"scale"`
- `"priority"`
