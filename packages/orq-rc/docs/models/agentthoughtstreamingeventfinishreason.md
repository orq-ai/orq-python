# AgentThoughtStreamingEventFinishReason

The reason the model stopped generating tokens.

## Example Usage

```python
from orq_ai_sdk.models import AgentThoughtStreamingEventFinishReason
value: AgentThoughtStreamingEventFinishReason = "stop"
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `STOP`           | stop             |
| `LENGTH`         | length           |
| `TOOL_CALLS`     | tool_calls       |
| `CONTENT_FILTER` | content_filter   |
| `FUNCTION_CALL`  | function_call    |