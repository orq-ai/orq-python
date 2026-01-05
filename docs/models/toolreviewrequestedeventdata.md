# ToolReviewRequestedEventData


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `tool_id`                                           | *str*                                               | :heavy_check_mark:                                  | Unique identifier for the tool in the tool registry |
| `tool_call_id`                                      | *str*                                               | :heavy_check_mark:                                  | The tool call ID requiring review                   |
| `tool_name`                                         | *Optional[str]*                                     | :heavy_minus_sign:                                  | Name of the tool requiring approval                 |
| `arguments`                                         | Dict[str, *Any*]                                    | :heavy_check_mark:                                  | Arguments that will be passed to the tool           |
| `requires_approval`                                 | *bool*                                              | :heavy_check_mark:                                  | Whether approval is mandatory before execution      |