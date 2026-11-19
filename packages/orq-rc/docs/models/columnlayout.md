# ColumnLayout

Layout change for one column.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `column_id`                                                 | *str*                                                       | :heavy_check_mark:                                          | ID of the column to change.                                 |
| `position`                                                  | *Optional[int]*                                             | :heavy_minus_sign:                                          | New 0-based position. The other columns shift to make room. |
| `width`                                                     | *Optional[int]*                                             | :heavy_minus_sign:                                          | New width, at least 1.                                      |
| `active`                                                    | *Optional[bool]*                                            | :heavy_minus_sign:                                          | False hides the column; true shows it.                      |