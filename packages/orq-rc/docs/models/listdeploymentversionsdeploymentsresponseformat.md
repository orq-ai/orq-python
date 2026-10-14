# ListDeploymentVersionsDeploymentsResponseFormat

An object specifying the format that the model must output. 

 Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema 

 Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if finish_reason="length", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.


## Supported Types

### `models.ListDeploymentVersionsResponseFormatDeployments1`

```python
value: models.ListDeploymentVersionsResponseFormatDeployments1 = /* values here */
```

### `models.ListDeploymentVersionsResponseFormatDeployments2`

```python
value: models.ListDeploymentVersionsResponseFormatDeployments2 = /* values here */
```

### `models.ListDeploymentVersionsResponseFormatDeployments3`

```python
value: models.ListDeploymentVersionsResponseFormatDeployments3 = /* values here */
```

### `models.ListDeploymentVersionsResponseFormatDeployments4`

```python
value: models.ListDeploymentVersionsResponseFormatDeployments4 = /* values here */
```

### `models.ListDeploymentVersionsResponseFormat5`

```python
value: models.ListDeploymentVersionsResponseFormat5 = /* values here */
```

### `models.ListDeploymentVersionsResponseFormat6`

```python
value: models.ListDeploymentVersionsResponseFormat6 = /* values here */
```

