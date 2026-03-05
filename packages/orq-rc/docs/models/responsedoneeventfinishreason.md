# ResponseDoneEventFinishReason

The reason why the agent stopped generating

## Example Usage

```python
from orq_ai_sdk.models import ResponseDoneEventFinishReason
value: ResponseDoneEventFinishReason = "stop"
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `STOP`           | stop             |
| `LENGTH`         | length           |
| `TOOL_CALLS`     | tool_calls       |
| `CONTENT_FILTER` | content_filter   |
| `FUNCTION_CALL`  | function_call    |
| `MAX_ITERATIONS` | max_iterations   |
| `MAX_TIME`       | max_time         |