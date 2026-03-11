# TwoTTL

The time-to-live for the cache control breakpoint. This may be one of the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. Only supported by `Anthropic` Claude models.

## Example Usage

```python
from orq_ai_sdk.models import TwoTTL
value: TwoTTL = "5m"
```


## Values

- `"5m"`
- `"1h"`
