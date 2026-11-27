# ListAgentsToolApprovalRequired

An Agent runs its tools without waiting for a human decision on `POST /v3/router/responses`. See https://docs.orq.ai/ai-studio/ai-engineering/build-agents#tool-approval.

## Example Usage

```python
from orq_ai_sdk.models import ListAgentsToolApprovalRequired
value: ListAgentsToolApprovalRequired = "all"
```


## Values

- `"all"`
- `"respect_tool"`
- `"none"`
