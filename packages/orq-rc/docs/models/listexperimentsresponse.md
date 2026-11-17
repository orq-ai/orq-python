# ListExperimentsResponse


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | List[[models.Experiment](../models/experiment.md)]                            | :heavy_minus_sign:                                                            | Page of experiments, newest first.                                            |
| `has_more`                                                                    | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Whether more experiments are available in the selected pagination<br/> direction. |