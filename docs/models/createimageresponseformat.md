# CreateImageResponseFormat

The format in which generated images are returned. Must be one of `url` or `b64_json`. This parameter isn't supported for `gpt-image-1` which will always return base64-encoded images.

## Example Usage

```python
from orq_ai_sdk.models import CreateImageResponseFormat
value: CreateImageResponseFormat = "url"
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `URL`      | url        |
| `B64_JSON` | b64_json   |