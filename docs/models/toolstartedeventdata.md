# ToolStartedEventData


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `tool_id`                                     | *str*                                         | :heavy_check_mark:                            | Unique identifier for the tool                |
| `tool_name`                                   | *Optional[str]*                               | :heavy_minus_sign:                            | Display name of the tool                      |
| `tool_call_id`                                | *str*                                         | :heavy_check_mark:                            | Unique identifier for this specific tool call |
| `arguments`                                   | Dict[str, *Any*]                              | :heavy_check_mark:                            | Arguments passed to the tool                  |