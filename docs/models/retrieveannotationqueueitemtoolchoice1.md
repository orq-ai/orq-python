# RetrieveAnnotationQueueItemToolChoice1

Controls which (if any) tool is called by the model. `none` means the model will not call any tool. `auto` means the model can pick between generating a message or calling a tool. `required` means the model must call a tool.

## Example Usage

```python
from orq_ai_sdk.models import RetrieveAnnotationQueueItemToolChoice1
value: RetrieveAnnotationQueueItemToolChoice1 = "none"
```


## Values

- `"none"`
- `"auto"`
- `"required"`
