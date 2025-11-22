# StreamAgentDataAgentsResponse200TextEventStreamResponseBodyData


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `agent_id`                               | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `action_id`                              | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `requires_approval`                      | *bool*                                   | :heavy_check_mark:                       | N/A                                      |
| `tool`                                   | [models.DataTool](../models/datatool.md) | :heavy_check_mark:                       | N/A                                      |
| `input`                                  | Dict[str, *Any*]                         | :heavy_check_mark:                       | N/A                                      |
| `agent_tool_call_id`                     | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `response_id`                            | *Optional[str]*                          | :heavy_minus_sign:                       | N/A                                      |