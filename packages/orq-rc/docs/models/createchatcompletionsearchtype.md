# CreateChatCompletionSearchType

The type of search to perform. If not provided, will default to the knowledge base configured `retrieval_type`

## Example Usage

```python
from orq_ai_sdk.models import CreateChatCompletionSearchType
value: CreateChatCompletionSearchType = "vector_search"
```


## Values

- `"vector_search"`
- `"keyword_search"`
- `"hybrid_search"`
