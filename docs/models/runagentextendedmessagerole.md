# RunAgentExtendedMessageRole

Role of the message sender in the A2A protocol. Values: user (end user), agent (AI agent), tool (tool execution result), system (system instructions/prompts).

## Example Usage

```python
from orq_ai_sdk.models import RunAgentExtendedMessageRole
value: RunAgentExtendedMessageRole = "user"
```


## Values

| Name     | Value    |
| -------- | -------- |
| `USER`   | user     |
| `AGENT`  | agent    |
| `TOOL`   | tool     |
| `SYSTEM` | system   |