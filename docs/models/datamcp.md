# DataMcp


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `server_url`                                                 | *str*                                                        | :heavy_check_mark:                                           | The MCP server URL (cached for execution)                    |
| `headers`                                                    | Dict[str, [models.DataHeaders](../models/dataheaders.md)]    | :heavy_minus_sign:                                           | HTTP headers for MCP server requests with encryption support |
| `tools`                                                      | List[[models.DataTools](../models/datatools.md)]             | :heavy_check_mark:                                           | Array of tools available from the MCP server                 |
| `connection_type`                                            | [models.DataConnectionType](../models/dataconnectiontype.md) | :heavy_check_mark:                                           | The connection type used by the MCP server                   |