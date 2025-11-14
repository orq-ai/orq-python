# RequestBodyMcp


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `server_url`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | The MCP server URL (cached for execution)                                  |
| `headers`                                                                  | Dict[str, [models.RequestBodyHeaders](../models/requestbodyheaders.md)]    | :heavy_minus_sign:                                                         | HTTP headers for MCP server requests with encryption support               |
| `connection_type`                                                          | [models.RequestBodyConnectionType](../models/requestbodyconnectiontype.md) | :heavy_check_mark:                                                         | The connection type used by the MCP server                                 |