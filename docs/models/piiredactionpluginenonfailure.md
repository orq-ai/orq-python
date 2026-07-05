# PIIRedactionPluginEnOnFailure

Behavior when redaction is unavailable. `block` (default) fails the request; `passthrough` sends the original text.

## Example Usage

```python
from orq_ai_sdk.models import PIIRedactionPluginEnOnFailure
value: PIIRedactionPluginEnOnFailure = "block"
```


## Values

- `"block"`
- `"passthrough"`
