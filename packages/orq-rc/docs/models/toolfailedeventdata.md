# ToolFailedEventData


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `tool_id`                                            | *str*                                                | :heavy_check_mark:                                   | Unique identifier for the tool in the tool registry  |
| `tool_call_id`                                       | *str*                                                | :heavy_check_mark:                                   | Unique identifier matching the tool call that failed |
| `error`                                              | *str*                                                | :heavy_check_mark:                                   | Error message describing why the tool failed         |