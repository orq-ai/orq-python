# TracesListFacetValuesRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `field`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `all_accessible_projects`                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Spans every project the caller belongs to instead of the active one. |