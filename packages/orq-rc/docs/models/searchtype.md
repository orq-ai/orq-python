# SearchType

The type of search to perform. If not provided, will default to the knowledge base configured `retrieval_type`

## Example Usage

```python
from orq_ai_sdk.models import SearchType
value: SearchType = "vector_search"
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `VECTOR_SEARCH`  | vector_search    |
| `KEYWORD_SEARCH` | keyword_search   |
| `HYBRID_SEARCH`  | hybrid_search    |