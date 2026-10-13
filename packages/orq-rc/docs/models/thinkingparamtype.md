# ThinkingParamType

The thinking mode to use for the model. Sonnet 5.5 supports between_tools for progress updates without extended thinking.

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
