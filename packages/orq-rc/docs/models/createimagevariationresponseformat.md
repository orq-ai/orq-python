# CreateImageVariationResponseFormat

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

## Example Usage

```python
from orq_ai_sdk.models import CreateImageVariationResponseFormat
value: CreateImageVariationResponseFormat = "url"
```


## Values

- `"url"`
- `"b64_json"`
