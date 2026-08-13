# SearchType

The type of search to perform. Send `null` or omit to use the knowledge base configured `retrieval_type`

## Example Usage

```python
from orq_ai_sdk.models import SearchType
value: SearchType = "vector_search"
```


## Values

- `"vector_search"`
- `"keyword_search"`
- `"hybrid_search"`
