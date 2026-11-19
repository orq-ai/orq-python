# PublicBatchError


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `code`                                                         | *str*                                                          | :heavy_check_mark:                                             | Machine-readable error code.                                   |
| `line`                                                         | *Optional[int]*                                                | :heavy_minus_sign:                                             | Input file line the error refers to, when it is line-specific. |
| `message`                                                      | *str*                                                          | :heavy_check_mark:                                             | Human-readable error message.                                  |
| `param`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | Request field the error refers to, when it is field-specific.  |