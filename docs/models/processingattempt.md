# ProcessingAttempt


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `started_at`                                                 | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `queued_at`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `completed_at`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `errors`                                                     | List[[models.ProcessingError](../models/processingerror.md)] | :heavy_minus_sign:                                           | N/A                                                          |
| `retryable`                                                  | *Optional[bool]*                                             | :heavy_minus_sign:                                           | N/A                                                          |