# ThinkingParamType

The thinking mode to use for the model. between_tools returns progress updates between tool calls without extended thinking on models that support it.

## Example Usage

```python
from orq_ai_sdk.models import ThinkingParamType
value: ThinkingParamType = "enabled"
```


## Values

- `"enabled"`
- `"disabled"`
- `"adaptive"`
- `"between_tools"`
