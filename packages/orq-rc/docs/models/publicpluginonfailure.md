# PublicPluginOnFailure

pii_redaction only. Behavior when redaction is unavailable. block (default) fails the request; passthrough sends the original text.

## Example Usage

```python
from orq_ai_sdk.models import PublicPluginOnFailure
value: PublicPluginOnFailure = "block"
```


## Values

- `"block"`
- `"passthrough"`
