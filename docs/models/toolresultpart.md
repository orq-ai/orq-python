# ToolResultPart

The result of a tool execution. Contains the tool call ID for correlation and the result data from the tool invocation.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `kind`                                                       | [models.ToolResultPartKind](../models/toolresultpartkind.md) | :heavy_check_mark:                                           | N/A                                                          |
| `tool_call_id`                                               | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `result`                                                     | *Optional[Any]*                                              | :heavy_minus_sign:                                           | N/A                                                          |
| `metadata`                                                   | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |