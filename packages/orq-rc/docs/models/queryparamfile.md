# QueryParamFile

Which result file to download: output holds successful responses, errors holds the per-line failures. Defaults to output, and answers the errors file when the batch produced no output file. Requesting errors on a batch with no error file returns 409 output_unavailable.

## Example Usage

```python
from orq_ai_sdk.models import QueryParamFile
value: QueryParamFile = "output"
```


## Values

- `"output"`
- `"errors"`
