# FallbackModelConfigurationExecuteOn

Determines whether the guardrail runs on the input (user message) or output (model response).

## Example Usage

```python
from orq_ai_sdk.models import FallbackModelConfigurationExecuteOn
value: FallbackModelConfigurationExecuteOn = "input"
```


## Values

| Name     | Value    |
| -------- | -------- |
| `INPUT`  | input    |
| `OUTPUT` | output   |