# ResponseBodyJury


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `judges_configured`                          | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `judges_succeeded`                           | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `judges_failed`                              | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `replacements_used`                          | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `tie`                                        | *bool*                                       | :heavy_check_mark:                           | N/A                                          |
| `votes`                                      | List[[models.Votes](../models/votes.md)]     | :heavy_check_mark:                           | N/A                                          |
| `stats`                                      | [Optional[models.Stats]](../models/stats.md) | :heavy_minus_sign:                           | N/A                                          |