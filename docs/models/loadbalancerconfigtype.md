# LoadBalancerConfigType

Strategy used to pick a model: weight_based splits traffic by weight, round_robin rotates through the list, latency_based favors the fastest model. An unrecognized value falls back to weight_based.

## Example Usage

```python
from orq_ai_sdk.models import LoadBalancerConfigType
value: LoadBalancerConfigType = "weight_based"
```


## Values

- `"weight_based"`
- `"round_robin"`
- `"latency_based"`
