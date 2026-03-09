# ResponseBodyMcp


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `server_url`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | The MCP server URL (cached for execution)                                    |
| `headers`                                                                    | Dict[str, [models.ResponseBodyHeaders](../models/responsebodyheaders.md)]    | :heavy_minus_sign:                                                           | HTTP headers for MCP server requests with encryption support                 |
| `tools`                                                                      | List[[models.ResponseBodyTools](../models/responsebodytools.md)]             | :heavy_check_mark:                                                           | Array of tools available from the MCP server                                 |
| `connection_type`                                                            | [models.ResponseBodyConnectionType](../models/responsebodyconnectiontype.md) | :heavy_check_mark:                                                           | The connection type used by the MCP server                                   |