# UpdateAgentScheduleType

Change the schedule type. Only cron is accepted. Changing the type or expression reschedules future executions and increments generation.

## Example Usage

```python
from orq_ai_sdk.models import UpdateAgentScheduleType
value: UpdateAgentScheduleType = "cron"
```


## Values

- `"cron"`
