# ToolExecutionStartedStreamingEventData


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `tool_id`                                                        | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `tool_key`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `tool_display_name`                                              | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `action_type`                                                    | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `tool_arguments`                                                 | Dict[str, *Any*]                                                 | :heavy_check_mark:                                               | N/A                                                              |
| `tool_execution_context`                                         | [models.ToolExecutionContext](../models/toolexecutioncontext.md) | :heavy_check_mark:                                               | N/A                                                              |
| `response_id`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `workflow_run_id`                                                | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |