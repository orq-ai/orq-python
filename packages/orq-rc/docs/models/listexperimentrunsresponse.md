# ListExperimentRunsResponse


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `data`                                                                | List[[models.Run](../models/run.md)]                                  | :heavy_minus_sign:                                                    | Page of runs, newest first.                                           |
| `has_more`                                                            | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Whether more runs are available in the selected pagination direction. |