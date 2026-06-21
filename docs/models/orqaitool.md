# OrqAiTool

An orq.ai platform tool reference. For MCP tools, prefer type 'mcp' with 'key' instead of 'orq:mcp' with 'tool_id'.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `tool_id`                                                                                            | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The tool ID (for orq:mcp, orq:http, orq:function).                                                   |
| `type`                                                                                               | [models.CreateRouterResponseToolsResponsesType](../models/createrouterresponsetoolsresponsestype.md) | :heavy_check_mark:                                                                                   | The orq.ai tool type.                                                                                |