# ListAgentsToolApprovalRequired

If all, the agent will require approval for all tools. If respect_tool, the agent will require approval for tools that have the requires_approval flag set to true. If none, the agent will not require approval for any tools.

## Example Usage

```python
from orq_ai_sdk.models import ListAgentsToolApprovalRequired
value: ListAgentsToolApprovalRequired = "all"
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ALL`          | all            |
| `RESPECT_TOOL` | respect_tool   |
| `NONE`         | none           |