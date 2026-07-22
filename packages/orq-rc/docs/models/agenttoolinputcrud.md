# AgentToolInputCRUD

Tool configuration for agent create/update operations. Built-in tools only require a type, while custom tools (HTTP, Code, Function, JSON Schema, MCP) must reference pre-created tools by key or id. Provider-prefixed tools (e.g., openai:web_search) are passed through to the provider.


## Supported Types

### `models.HTTPToolInput`

```python
value: models.HTTPToolInput = /* values here */
```

### `models.CodeToolInput`

```python
value: models.CodeToolInput = /* values here */
```

### `models.FunctionToolInput`

```python
value: models.FunctionToolInput = /* values here */
```

### `models.JSONSchemaToolInput`

```python
value: models.JSONSchemaToolInput = /* values here */
```

### `models.McpToolInput`

```python
value: models.McpToolInput = /* values here */
```

