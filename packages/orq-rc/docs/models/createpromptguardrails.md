# CreatePromptGuardrails


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | [models.CreatePromptID](../models/createpromptid.md)                                          | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `execute_on`                                                                                  | [models.CreatePromptExecuteOn](../models/createpromptexecuteon.md)                            | :heavy_check_mark:                                                                            | Determines whether the guardrail runs on the input (user message) or output (model response). |