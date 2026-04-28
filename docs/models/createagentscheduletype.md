# CreateAgentScheduleType

Schedule type. cron uses 6-field cron expressions; interval uses @every <duration>; once uses @at <RFC3339-UTC>.

## Example Usage

```python
from orq_ai_sdk.models import CreateAgentScheduleType
value: CreateAgentScheduleType = "cron"
```


## Values

- `"cron"`
- `"once"`
- `"interval"`
