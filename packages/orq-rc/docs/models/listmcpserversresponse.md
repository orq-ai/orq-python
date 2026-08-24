# ListMcpServersResponse


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `object`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Always "list".                                   |
| `data`                                           | List[[models.McpServer](../models/mcpserver.md)] | :heavy_minus_sign:                               | MCP servers on the current page.                 |
| `has_more`                                       | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether further items exist beyond this page.    |