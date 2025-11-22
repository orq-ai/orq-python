# ToolExecutionContext


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `action_id`                                            | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `agent_tool_call_id`                                   | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `workspace_id`                                         | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `agent_manifest_id`                                    | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `agent_execution_id`                                   | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `product`                                              | [models.Product](../models/product.md)                 | :heavy_check_mark:                                     | Orquesta product                                       |
| `memory`                                               | [Optional[models.DataMemory]](../models/datamemory.md) | :heavy_minus_sign:                                     | N/A                                                    |
| `parent_id`                                            | *Optional[str]*                                        | :heavy_minus_sign:                                     | N/A                                                    |