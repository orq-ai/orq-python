# TelemetryRow


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `timestamp`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)             | :heavy_minus_sign:                                                               | Unset when the resolved grain is "none" — one row per group, not a<br/> time series. |
| `group`                                                                          | Dict[str, *str*]                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |
| `metrics`                                                                        | Dict[str, *float*]                                                               | :heavy_minus_sign:                                                               | N/A                                                                              |