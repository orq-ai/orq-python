# ListMcpGatewaysResponse


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `object`                                           | *Optional[str]*                                    | :heavy_minus_sign:                                 | Always "list".                                     |
| `data`                                             | List[[models.McpGateway](../models/mcpgateway.md)] | :heavy_minus_sign:                                 | MCP gateways on the current page.                  |
| `has_more`                                         | *Optional[bool]*                                   | :heavy_minus_sign:                                 | Whether further items exist beyond this page.      |