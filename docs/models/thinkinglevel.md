# ThinkingLevel

The level of reasoning the model should use. This setting is supported only by `gemini-3` models. If budget_tokens is specified and `thinking_level` is available, `budget_tokens` will be ignored.

## Example Usage

```python
from orq_ai_sdk.models import ThinkingLevel
value: ThinkingLevel = "low"
```


## Values

- `"low"`
- `"high"`
