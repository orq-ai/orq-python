# RetrieveAnnotationQueueItemOutputAnnotationQueuesResponse200ApplicationJSONStatus

Similar to `FunctionCallStatus`. All three options are allowed here for compatibility, but because in practice these items will be provided by developers, only `completed` should be used.

## Example Usage

```python
from orq_ai_sdk.models import RetrieveAnnotationQueueItemOutputAnnotationQueuesResponse200ApplicationJSONStatus
value: RetrieveAnnotationQueueItemOutputAnnotationQueuesResponse200ApplicationJSONStatus = "in_progress"
```


## Values

- `"in_progress"`
- `"completed"`
- `"incomplete"`
