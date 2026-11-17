# QueryParamFormat

File format: `json` (an array of records), `jsonl` (one record per line) or `csv`. Each record is one row and task column.

## Example Usage

```python
from orq_ai_sdk.models import QueryParamFormat
value: QueryParamFormat = "csv"
```


## Values

- `"csv"`
- `"json"`
- `"jsonl"`
