# Provider

Provider to run this search. Exa uses auto, Linkup uses standard depth, Tavily uses basic depth, and OpenAI runs one web_search tool call on gpt-5.6-luna. Workspace credentials are selected automatically for this provider.

## Example Usage

```python
from orq_ai_sdk.models import Provider
value: Provider = "exa"
```


## Values

- `"exa"`
- `"ceramic"`
- `"linkup"`
- `"tavily"`
- `"serper"`
- `"openai"`
- `"perplexity"`
