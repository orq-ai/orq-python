# PublicPluginID

Plugin discriminator. pii_redaction redacts PII, response_healing repairs malformed JSON, and trace_scrubbing removes selected sensitive fields from exported traces.

## Example Usage

```python
from orq_ai_sdk.models import PublicPluginID
value: PublicPluginID = "pii_redaction"
```


## Values

- `"pii_redaction"`
- `"response_healing"`
- `"trace_scrubbing"`
