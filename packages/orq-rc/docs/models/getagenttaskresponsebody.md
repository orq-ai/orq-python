# GetAgentTaskResponseBody

Agent task retrieved


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `context_id`                                                 | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `kind`                                                       | [models.GetAgentTaskKind](../models/getagenttaskkind.md)     | :heavy_check_mark:                                           | N/A                                                          |
| `status`                                                     | [models.GetAgentTaskStatus](../models/getagenttaskstatus.md) | :heavy_check_mark:                                           | N/A                                                          |
| `history`                                                    | List[*Any*]                                                  | :heavy_check_mark:                                           | N/A                                                          |
| `artifacts`                                                  | List[*Any*]                                                  | :heavy_minus_sign:                                           | N/A                                                          |
| `metadata`                                                   | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |