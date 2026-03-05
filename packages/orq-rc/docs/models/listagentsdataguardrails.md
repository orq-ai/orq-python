# ListAgentsDataGuardrails


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | [models.DataID](../models/dataid.md)                                                          | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `execute_on`                                                                                  | [models.ListAgentsDataAgentsExecuteOn](../models/listagentsdataagentsexecuteon.md)            | :heavy_check_mark:                                                                            | Determines whether the guardrail runs on the input (user message) or output (model response). |