# GetAllPromptTemplatesItemsPromptTemplatesResponse200ApplicationJSONResponseFormat

An object specifying the format that the model must output. 

 Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema 

 Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if finish_reason="length", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.


## Supported Types

### `models.GetAllPromptTemplatesResponseFormatPromptTemplatesResponse200ApplicationJSONResponseBody1`

```python
value: models.GetAllPromptTemplatesResponseFormatPromptTemplatesResponse200ApplicationJSONResponseBody1 = /* values here */
```

### `models.GetAllPromptTemplatesResponseFormatPromptTemplatesResponse200ApplicationJSONResponseBody2`

```python
value: models.GetAllPromptTemplatesResponseFormatPromptTemplatesResponse200ApplicationJSONResponseBody2 = /* values here */
```

