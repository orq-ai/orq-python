# PublicPluginID

Plugin discriminator. pii_redaction replaces PII with placeholders before the provider sees it and restores the original values in the response. response_healing repairs malformed JSON in non-streaming model output.

## Example Usage

```python
from orq_ai_sdk.models import PublicPluginID
value: PublicPluginID = "pii_redaction"
```


## Values

- `"pii_redaction"`
- `"response_healing"`
