# McpServers

## Overview

### Available Operations

* [list](#list) - List MCP servers
* [create](#create) - Create an MCP server
* [get](#get) - Retrieve an MCP server
* [delete](#delete) - Delete an MCP server
* [update](#update) - Update an MCP server
* [test_tool](#test_tool) - Test an MCP server tool
* [sync](#sync) - Sync an MCP server
* [test](#test) - Test an MCP server connection

## list

Returns a paginated list of MCP servers in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerList" method="get" path="/v2/mcp-servers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `status`                                                            | [Optional[models.McpServerStatus]](../../models/mcpserverstatus.md) | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMcpServersResponse](../../models/listmcpserversresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new upstream MCP server connection in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerCreate" method="post" path="/v2/mcp-servers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `key`                                                                 | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `display_name`                                                        | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `description`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `project_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `connection`                                                          | [Optional[models.McpConnection]](../../models/mcpconnection.md)       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `auth`                                                                | [Optional[models.McpAuthConfig]](../../models/mcpauthconfig.md)       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `default_tool_exposure`                                               | [Optional[models.McpToolExposure]](../../models/mcptoolexposure.md)   | :heavy_minus_sign:                                                    | N/A                                                                   |
| `sharing`                                                             | [Optional[models.McpServerSharing]](../../models/mcpserversharing.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateMcpServerResponse](../../models/createmcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the details of an existing MCP server by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerGet" method="get" path="/v2/mcp-servers/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMcpServerResponse](../../models/getmcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an MCP server from the workspace. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerDelete" method="delete" path="/v2/mcp-servers/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteMcpServerResponse](../../models/deletemcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates mutable fields of an existing MCP server. Omitted optional fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerUpdate" method="patch" path="/v2/mcp-servers/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `key`                                                                 | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `display_name`                                                        | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `description`                                                         | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `connection`                                                          | [Optional[models.McpConnection]](../../models/mcpconnection.md)       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `auth`                                                                | [Optional[models.McpAuthConfig]](../../models/mcpauthconfig.md)       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `default_tool_exposure`                                               | [Optional[models.McpToolExposure]](../../models/mcptoolexposure.md)   | :heavy_minus_sign:                                                    | N/A                                                                   |
| `status`                                                              | [Optional[models.McpServerStatus]](../../models/mcpserverstatus.md)   | :heavy_minus_sign:                                                    | N/A                                                                   |
| `sharing`                                                             | [Optional[models.McpServerSharing]](../../models/mcpserversharing.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UpdateMcpServerResponse](../../models/updatemcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## test_tool

Executes a single tool on an upstream MCP server for testing. Connects to the server, invokes the tool with the provided arguments, and returns the result.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerTestTool" method="post" path="/v2/mcp-servers/{id}/tools:test" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.test_tool(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `tool_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `arguments`                                                         | [Optional[models.Arguments]](../../models/arguments.md)             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestMcpServerToolResponse](../../models/testmcpservertoolresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## sync

Connects to an upstream MCP server, discovers tools, and persists the tool list and sync state on the server record.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerSync" method="post" path="/v2/mcp-servers/{id}:sync" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.sync(id="<id>", sync_mcp_server_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sync_mcp_server_request`                                           | [models.SyncMcpServerRequest](../../models/syncmcpserverrequest.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SyncMcpServerResponse](../../models/syncmcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## test

Probes an upstream MCP server connection without persisting it. Returns discovered tools and connectivity status.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerTest" method="post" path="/v2/mcp-servers:test" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.test()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connection`                                                        | [Optional[models.McpConnection]](../../models/mcpconnection.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `auth`                                                              | [Optional[models.McpAuthConfig]](../../models/mcpauthconfig.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestMcpServerResponse](../../models/testmcpserverresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |