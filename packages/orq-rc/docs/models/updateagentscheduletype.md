# UpdateAgentScheduleType

Change the schedule type. Changing type or expression resets the NATS schedule and bumps generation.

## Example Usage

```python
from orq_ai_sdk.models import UpdateAgentScheduleType
value: UpdateAgentScheduleType = "cron"
```


## Values

- `"cron"`
- `"once"`
- `"interval"`
