# CreateAgentScheduleSchedulesType

Schedule type. Only cron can be created or updated; once and interval only appear on schedules stored before that restriction.

## Example Usage

```python
from orq_ai_sdk.models import CreateAgentScheduleSchedulesType
value: CreateAgentScheduleSchedulesType = "cron"
```


## Values

- `"cron"`
- `"once"`
- `"interval"`
