# ThreadFilters


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `interval`                                              | [models.SessionInterval](../models/sessioninterval.md)  | :heavy_check_mark:                                      | N/A                                                     |
| `project_id`                                            | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `tags`                                                  | List[*str*]                                             | :heavy_minus_sign:                                      | N/A                                                     |
| `start_date`                                            | *Optional[str]*                                         | :heavy_minus_sign:                                      | Start of a custom activity window in unix milliseconds. |
| `end_date`                                              | *Optional[str]*                                         | :heavy_minus_sign:                                      | End of a custom activity window in unix milliseconds.   |
| `client`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `repo`                                                  | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `kind`                                                  | [Optional[models.ThreadKind]](../models/threadkind.md)  | :heavy_minus_sign:                                      | N/A                                                     |