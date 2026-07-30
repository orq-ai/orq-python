# McpGateways

## Overview

### Available Operations

* [list](#list) - List MCP gateways
* [create](#create) - Create an MCP gateway
* [list_tools](#list_tools) - List exposed tools for a gateway
* [get](#get) - Retrieve an MCP gateway
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

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `starting_after`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `ending_before`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `search`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `status`                                                              | [Optional[models.McpGatewayStatus]](../../models/mcpgatewaystatus.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListMcpGatewaysResponse](../../models/listmcpgatewaysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

    res = orq.mcp_gateways.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `key`                                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `display_name`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `description`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `project_id`                                                              | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `server_links`                                                            | List[[models.McpGatewayServerLink](../../models/mcpgatewayserverlink.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `tool_naming`                                                             | [Optional[models.McpToolNaming]](../../models/mcptoolnaming.md)           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `runtime_limits`                                                          | [Optional[models.McpRuntimeLimits]](../../models/mcpruntimelimits.md)     | :heavy_minus_sign:                                                        | N/A                                                                       |
| `egress_policy`                                                           | [Optional[models.McpEgressPolicy]](../../models/mcpegresspolicy.md)       | :heavy_minus_sign:                                                        | N/A                                                                       |
| `mode`                                                                    | [Optional[models.McpGatewayMode]](../../models/mcpgatewaymode.md)         | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateMcpGatewayResponse](../../models/createmcpgatewayresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `gateway_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `mcp_server_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMcpGatewayToolsResponse](../../models/listmcpgatewaytoolsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the details of an existing MCP gateway by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayGet" method="get" path="/v2/mcp-gateways/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateways.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMcpGatewayResponse](../../models/getmcpgatewayresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteMcpGatewayResponse](../../models/deletemcpgatewayresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `key`                                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `display_name`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `description`                                                             | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `server_links`                                                            | List[[models.McpGatewayServerLink](../../models/mcpgatewayserverlink.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `tool_naming`                                                             | [Optional[models.McpToolNaming]](../../models/mcptoolnaming.md)           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `runtime_limits`                                                          | [Optional[models.McpRuntimeLimits]](../../models/mcpruntimelimits.md)     | :heavy_minus_sign:                                                        | N/A                                                                       |
| `egress_policy`                                                           | [Optional[models.McpEgressPolicy]](../../models/mcpegresspolicy.md)       | :heavy_minus_sign:                                                        | N/A                                                                       |
| `status`                                                                  | [Optional[models.McpGatewayStatus]](../../models/mcpgatewaystatus.md)     | :heavy_minus_sign:                                                        | N/A                                                                       |
| `mode`                                                                    | [Optional[models.McpGatewayMode]](../../models/mcpgatewaymode.md)         | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UpdateMcpGatewayResponse](../../models/updatemcpgatewayresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |