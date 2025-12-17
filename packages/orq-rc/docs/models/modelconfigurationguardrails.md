# ModelConfigurationGuardrails


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | [models.ModelConfigurationID](../models/modelconfigurationid.md)                              | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `execute_on`                                                                                  | [models.ModelConfigurationExecuteOn](../models/modelconfigurationexecuteon.md)                | :heavy_check_mark:                                                                            | Determines whether the guardrail runs on the input (user message) or output (model response). |