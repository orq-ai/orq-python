# McpGateways

## Overview

### Available Operations

* [list](#list) - List MCP gateways
* [create](#create) - Create an MCP gateway
* [list_tools](#list_tools) - List exposed tools for a gateway
* [retrieve](#retrieve) - Retrieve an MCP gateway
* [delete](#delete) - Delete an MCP gateway
* [update](#update) - Update an MCP gateway

## list

Returns a paginated list of MCP gateways in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayList" method="get" path="/v2/mcp-gateways" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | Page size between 1 and 200. Defaults to 25.                                            |
| `starting_after`                                                                        | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Cursor for the page after the given item id. Mutually exclusive with `ending_before`.   |
| `ending_before`                                                                         | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Cursor for the page before the given item id. Mutually exclusive with `starting_after`. |
| `search`                                                                                | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Case-insensitive match against the gateway key and display name.                        |
| `status`                                                                                | [Optional[models.McpGatewayStatus]](../../models/mcpgatewaystatus.md)                   | :heavy_minus_sign:                                                                      | Returns only gateways in this status.                                                   |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ListMcpGatewaysResponse](../../models/listmcpgatewaysresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a client-facing MCP gateway that links one or more synced upstream servers and exposes a unified MCP endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayCreate" method="post" path="/v2/mcp-gateways" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.create(key="<key>", display_name="Litzy_Ruecker98")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                    | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | Lowercase slug of letters, digits, hyphens and underscores, max 64 characters, unique per workspace; backs the gateway's public MCP URL. |
| `display_name`                                                                                                                           | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | Human readable name shown in the workspace.                                                                                              |
| `description`                                                                                                                            | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Free-form note about what this gateway is for.                                                                                           |
| `server_links`                                                                                                                           | List[[models.McpGatewayServerLink](../../models/mcpgatewayserverlink.md)]                                                                | :heavy_minus_sign:                                                                                                                       | Upstream servers this gateway aggregates.                                                                                                |
| `tool_naming`                                                                                                                            | [Optional[models.McpToolNaming]](../../models/mcptoolnaming.md)                                                                          | :heavy_minus_sign:                                                                                                                       | N/A                                                                                                                                      |
| `mode`                                                                                                                                   | [Optional[models.McpGatewayMode]](../../models/mcpgatewaymode.md)                                                                        | :heavy_minus_sign:                                                                                                                       | N/A                                                                                                                                      |
| `sharing`                                                                                                                                | [Optional[models.Sharing]](../../models/sharing.md)                                                                                      | :heavy_minus_sign:                                                                                                                       | Which projects in the workspace may use this gateway. Defaults to every project.                                                         |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[models.CreateMcpGatewayResponse](../../models/createmcpgatewayresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_tools

Returns the namespaced tool view for a gateway.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayListTools" method="get" path="/v2/mcp-gateways/{gateway_id}/tools" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.list_tools(gateway_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `gateway_id`                                                                                   | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier of the MCP gateway.                                                          |
| `limit`                                                                                        | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | Page size between 1 and 200. Defaults to 25.                                                   |
| `starting_after`                                                                               | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for the page after the given `exposed_name`. Mutually exclusive with `ending_before`.   |
| `ending_before`                                                                                | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for the page before the given `exposed_name`. Mutually exclusive with `starting_after`. |
| `mcp_server_id`                                                                                | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Returns only tools contributed by this upstream server.                                        |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.ListMcpGatewayToolsResponse](../../models/listmcpgatewaytoolsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves the details of an existing MCP gateway by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayGet" method="get" path="/v2/mcp-gateways/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the MCP gateway.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMcpGatewayResponse](../../models/getmcpgatewayresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes an MCP gateway from the workspace. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayDelete" method="delete" path="/v2/mcp-gateways/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the MCP gateway.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteMcpGatewayResponse](../../models/deletemcpgatewayresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates mutable fields of an existing MCP gateway. Omitted optional fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayUpdate" method="patch" path="/v2/mcp-gateways/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                 | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | Unique identifier of the MCP gateway.                                                                                                                                                |
| `key`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Rejected with INVALID_ARGUMENT: the key backs the gateway's public MCP URL<br/> and is immutable after creation. Retained so callers get an error rather<br/> than a silently ignored field. |
| `display_name`                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Human readable name shown in the workspace.                                                                                                                                          |
| `description`                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Free-form note about what this gateway is for.                                                                                                                                       |
| `server_links`                                                                                                                                                                       | List[[models.McpGatewayServerLink](../../models/mcpgatewayserverlink.md)]                                                                                                            | :heavy_minus_sign:                                                                                                                                                                   | Replaces the current links. An empty array is treated as no change; use `clear_server_links` to remove them all.                                                                     |
| `tool_naming`                                                                                                                                                                        | [Optional[models.McpToolNaming]](../../models/mcptoolnaming.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | N/A                                                                                                                                                                                  |
| `status`                                                                                                                                                                             | [Optional[models.McpGatewayStatus]](../../models/mcpgatewaystatus.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                   | N/A                                                                                                                                                                                  |
| `mode`                                                                                                                                                                               | [Optional[models.McpGatewayMode]](../../models/mcpgatewaymode.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                   | N/A                                                                                                                                                                                  |
| `sharing`                                                                                                                                                                            | [Optional[models.Sharing]](../../models/sharing.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                   | Which projects in the workspace may use this gateway. Defaults to every project.                                                                                                     |
| `clear_server_links`                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Set true to remove every link; cannot be combined with `server_links`.                                                                                                               |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[models.UpdateMcpGatewayResponse](../../models/updatemcpgatewayresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |