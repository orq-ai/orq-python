# ExecuteRunRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `scope`                                                                | [models.ExecuteScope](../models/executescope.md)                       | :heavy_check_mark:                                                     | N/A                                                                    |
| `targets`                                                              | List[[models.ExecuteTarget](../models/executetarget.md)]               | :heavy_minus_sign:                                                     | Rows and columns to execute. Required for row, column and cell scope.  |
| `constraints`                                                          | [Optional[models.ExecuteConstraints]](../models/executeconstraints.md) | :heavy_minus_sign:                                                     | Limits for this execution, saved into the run's settings.              |