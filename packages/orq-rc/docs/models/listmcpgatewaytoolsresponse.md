# ListMcpGatewayToolsResponse


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `object`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | Always "list".                                             |
| `data`                                                     | List[[models.McpGatewayTool](../models/mcpgatewaytool.md)] | :heavy_minus_sign:                                         | Exposed tools on the current page.                         |
| `has_more`                                                 | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether further items exist beyond this page.              |