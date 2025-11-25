# StreamRunAgentDataData


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `workflow_run_id`                                          | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `integration_id`                                           | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `input_message`                                            | [models.InputMessage](../models/inputmessage.md)           | :heavy_check_mark:                                         | N/A                                                        |
| `model_id`                                                 | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `instructions`                                             | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `system_prompt`                                            | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `settings`                                                 | [Optional[models.DataSettings]](../models/datasettings.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `agent_manifest_id`                                        | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `agent_key`                                                | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `variables`                                                | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `tool_execution_id`                                        | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `is_continuation`                                          | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `stream`                                                   | *Optional[bool]*                                           | :heavy_minus_sign:                                         | N/A                                                        |
| `response_id`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |