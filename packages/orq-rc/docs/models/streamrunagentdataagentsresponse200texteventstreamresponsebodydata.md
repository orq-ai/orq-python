# StreamRunAgentDataAgentsResponse200TextEventStreamResponseBodyData


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `agent_id`                           | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `action_id`                          | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `agent_tool_call_id`                 | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `review`                             | [models.Review](../models/review.md) | :heavy_check_mark:                   | N/A                                  |
| `mock_output`                        | Dict[str, *Any*]                     | :heavy_minus_sign:                   | N/A                                  |
| `review_source`                      | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `reviewed_by_id`                     | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `workflow_run_id`                    | *str*                                | :heavy_check_mark:                   | N/A                                  |