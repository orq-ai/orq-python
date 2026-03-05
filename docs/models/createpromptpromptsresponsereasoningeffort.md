# CreatePromptPromptsResponseReasoningEffort

Constrains effort on reasoning for reasoning models. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.

## Example Usage

```python
from orq_ai_sdk.models import CreatePromptPromptsResponseReasoningEffort
value: CreatePromptPromptsResponseReasoningEffort = "none"
```


## Values

| Name      | Value     |
| --------- | --------- |
| `NONE`    | none      |
| `DISABLE` | disable   |
| `MINIMAL` | minimal   |
| `LOW`     | low       |
| `MEDIUM`  | medium    |
| `HIGH`    | high      |