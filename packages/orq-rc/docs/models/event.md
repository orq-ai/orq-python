# Event

The SSE event name, equal to the payload's `type`.

## Example Usage

```python
from orq_ai_sdk.models import Event
value: Event = "response.created"
```


## Values

- `"response.created"`
- `"response.queued"`
- `"response.in_progress"`
- `"response.completed"`
- `"response.failed"`
- `"response.incomplete"`
