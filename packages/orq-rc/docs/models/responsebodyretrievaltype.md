# ResponseBodyRetrievalType

The retrieval type to use for the knowledge base. If not provided, Hybrid Search will be used as a default query strategy.

## Example Usage

```python
from orq_ai_sdk.models import ResponseBodyRetrievalType
value: ResponseBodyRetrievalType = "vector_search"
```


## Values

- `"vector_search"`
- `"keyword_search"`
- `"hybrid_search"`
