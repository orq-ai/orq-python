# ReplayAuditLogDeliveriesRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `from_`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_check_mark:                                                            | Required. Start of the window (inclusive).                                    |
| `to`                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_check_mark:                                                            | Required. End of the window (exclusive). The window may span at most 31 days. |