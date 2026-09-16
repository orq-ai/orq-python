# ListEvalVersionsRequest


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `id`                                                  | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `limit`                                               | *Optional[int]*                                       | :heavy_minus_sign:                                    | Page size, 1-200. Unset uses the server default (10). |
| `starting_after`                                      | *Optional[str]*                                       | :heavy_minus_sign:                                    | N/A                                                   |
| `ending_before`                                       | *Optional[str]*                                       | :heavy_minus_sign:                                    | N/A                                                   |