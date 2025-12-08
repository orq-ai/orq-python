# ToolDoneEventData


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `tool_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | Unique identifier for the tool in the tool registry        |
| `tool_call_id`                                             | *str*                                                      | :heavy_check_mark:                                         | Unique identifier matching the tool call that was executed |
| `result`                                                   | *Optional[Any]*                                            | :heavy_minus_sign:                                         | The result returned by the tool                            |