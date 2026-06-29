# PublicPIIRedactionPluginOnFailure

Behavior when redaction is unavailable. block (default) fails the request; passthrough sends the original text.

## Example Usage

```python
from orq_ai_sdk.models import PublicPIIRedactionPluginOnFailure
value: PublicPIIRedactionPluginOnFailure = "block"
```


## Values

- `"block"`
- `"passthrough"`
