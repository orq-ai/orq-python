# QueryRunResponse


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `rows`                                                                    | List[[models.QueryRow](../models/queryrow.md)]                            | :heavy_minus_sign:                                                        | N/A                                                                       |
| `has_more`                                                                | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `server_timestamp`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)      | :heavy_minus_sign:                                                        | Cursor for the next incremental query (server clock minus a skew buffer). |