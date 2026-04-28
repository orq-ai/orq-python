# TemplateEngine

Template engine for variable substitution in instructions. Defaults to the agent manifest's engine when invoking an agent, otherwise text.

## Example Usage

```python
from orq_ai_sdk.models import TemplateEngine
value: TemplateEngine = "text"
```


## Values

- `"text"`
- `"jinja"`
- `"mustache"`
