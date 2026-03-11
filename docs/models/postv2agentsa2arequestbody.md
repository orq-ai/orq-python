# PostV2AgentsA2aRequestBody


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the agent                                     |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Display name for the agent                                          |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Description of the agent                                            |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Project path for organizing the agent                               |
| `agent_url`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The A2A agent endpoint URL                                          |
| `card_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional explicit agent card URL (must be different from agent_url) |
| `headers`                                                           | Dict[str, [models.Headers](../models/headers.md)]                   | :heavy_minus_sign:                                                  | Authentication headers for the A2A agent                            |