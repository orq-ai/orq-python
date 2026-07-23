# RetrieveKnowledgeBasesTool

Lists available knowledge bases


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `type`                                                                                              | [models.AgentToolInputCRUD9Type](../models/agenttoolinputcrud9type.md)                              | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `requires_approval`                                                                                 | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether this tool requires approval before execution                                                |
| `configuration`                                                                                     | Dict[str, *Any*]                                                                                    | :heavy_minus_sign:                                                                                  | Static tool configuration set at design time. Merged over LLM-provided arguments at execution time. |