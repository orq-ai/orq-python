# AgentToolInputCRUD

Tool configuration for agent create/update operations. Built-in tools only require a type, while custom tools (HTTP, Code, Function, JSON Schema, MCP) must reference pre-created tools by key or id. Provider-prefixed tools (e.g., openai:web_search) are passed through to the provider.


## Supported Types

### `models.GoogleSearchToolInput`

```python
value: models.GoogleSearchToolInput = /* values here */
```

### `models.WebScraperToolInput`

```python
value: models.WebScraperToolInput = /* values here */
```

### `models.CallSubAgentToolInput`

```python
value: models.CallSubAgentToolInput = /* values here */
```

### `models.RetrieveAgentsToolInput`

```python
value: models.RetrieveAgentsToolInput = /* values here */
```

### `models.QueryMemoryStoreToolInput`

```python
value: models.QueryMemoryStoreToolInput = /* values here */
```

### `models.WriteMemoryStoreToolInput`

```python
value: models.WriteMemoryStoreToolInput = /* values here */
```

### `models.RetrieveMemoryStoresToolInput`

```python
value: models.RetrieveMemoryStoresToolInput = /* values here */
```

### `models.DeleteMemoryDocumentToolInput`

```python
value: models.DeleteMemoryDocumentToolInput = /* values here */
```

### `models.RetrieveKnowledgeBasesToolInput`

```python
value: models.RetrieveKnowledgeBasesToolInput = /* values here */
```

### `models.QueryKnowledgeBaseToolInput`

```python
value: models.QueryKnowledgeBaseToolInput = /* values here */
```

### `models.CurrentDateToolInput`

```python
value: models.CurrentDateToolInput = /* values here */
```

### `models.AdvisorToolInput`

```python
value: models.AdvisorToolInput = /* values here */
```

### `models.SidekickToolInput`

```python
value: models.SidekickToolInput = /* values here */
```

### `models.CodeInterpreterToolInput`

```python
value: models.CodeInterpreterToolInput = /* values here */
```

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

