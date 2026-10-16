# GetLogContextResponse


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `anchor`                                                            | [models.Log](../models/log.md)                                      | :heavy_check_mark:                                                  | Log is a log record returned by the log endpoints.                  |
| `before`                                                            | List[[models.Log](../models/log.md)]                                | :heavy_check_mark:                                                  | Matching records earlier than the anchor, ordered oldest to newest. |
| `after`                                                             | List[[models.Log](../models/log.md)]                                | :heavy_check_mark:                                                  | Matching records later than the anchor, ordered oldest to newest.   |
| `has_more_before`                                                   | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `has_more_after`                                                    | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |