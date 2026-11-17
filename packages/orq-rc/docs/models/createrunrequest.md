# CreateRunRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `key`                                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Run name. Defaults to `Run ` plus the last four characters of the run ID. |
| `settings`                                                                | [Optional[models.RunSettings]](../models/runsettings.md)                  | :heavy_minus_sign:                                                        | Execution settings. Concurrency defaults to 10.                           |