# McpServers

## Overview

### Available Operations

* [list](#list) - List MCP servers
* [create](#create) - Create an MCP server
* [retrieve](#retrieve) - Retrieve an MCP server
* [delete](#delete) - Delete an MCP server
* [update](#update) - Update an MCP server
* [test_tool](#test_tool) - Test an MCP server tool
* [sync](#sync) - Sync an MCP server

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

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `limit`                                                                                 | *Optional[int]*                                                                         | :heavy_minus_sign:                                                                      | Page size between 1 and 200. Defaults to 25.                                            |
| `starting_after`                                                                        | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Cursor for the page after the given item id. Mutually exclusive with `ending_before`.   |
| `ending_before`                                                                         | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Cursor for the page before the given item id. Mutually exclusive with `starting_after`. |
| `search`                                                                                | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Case-insensitive match against the server key and display name.                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ListMcpServersResponse](../../models/listmcpserversresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

    res = orq.mcp_servers.create(key="<key>", display_name="Felton.Daugherty-Reynolds", connection={
        "type": "MCP_CONNECTION_TYPE_HTTP",
        "url": "https://thin-event.net/",
    }, auth={
        "type": "MCP_AUTH_TYPE_OAUTH_CLIENT_CREDENTIALS",
    }, default_tool_exposure={
        "mode": "MCP_TOOL_EXPOSURE_MODE_UNSPECIFIED",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                               | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | Lowercase slug of letters, digits, hyphens and underscores, max 64 characters, unique per workspace; prefixes this server's tool names in gateways. |
| `display_name`                                                                                                                                      | *str*                                                                                                                                               | :heavy_check_mark:                                                                                                                                  | Human readable name shown in the workspace.                                                                                                         |
| `connection`                                                                                                                                        | [models.McpConnection](../../models/mcpconnection.md)                                                                                               | :heavy_check_mark:                                                                                                                                  | How the gateway dials the upstream server.                                                                                                          |
| `auth`                                                                                                                                              | [models.McpAuthConfig](../../models/mcpauthconfig.md)                                                                                               | :heavy_check_mark:                                                                                                                                  | Credentials the gateway sends upstream; send `type: NONE` explicitly for public servers.                                                            |
| `default_tool_exposure`                                                                                                                             | [models.McpToolExposure](../../models/mcptoolexposure.md)                                                                                           | :heavy_check_mark:                                                                                                                                  | Fallback exposure used by any gateway link that does not set its own.                                                                               |
| `description`                                                                                                                                       | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Free-form note about what this server is for.                                                                                                       |
| `sharing`                                                                                                                                           | [Optional[models.Sharing]](../../models/sharing.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                  | Which projects in the workspace may use this server. Defaults to every project.                                                                     |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |

### Response

**[models.CreateMcpServerResponse](../../models/createmcpserverresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves the details of an existing MCP server by its unique ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpServerGet" method="get" path="/v2/mcp-servers/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_servers.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the MCP server.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMcpServerResponse](../../models/getmcpserverresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the MCP server.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteMcpServerResponse](../../models/deletemcpserverresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

| Parameter                                                                                                                                                                                                          | Type                                                                                                                                                                                                               | Required                                                                                                                                                                                                           | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                 | Unique identifier of the MCP server.                                                                                                                                                                               |
| `key`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | Rejected with INVALID_ARGUMENT: the key prefixes this server's tools in<br/> every gateway that exposes it, so it is immutable after creation. Retained<br/> so callers get an error rather than a silently ignored field. |
| `display_name`                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | Human readable name shown in the workspace.                                                                                                                                                                        |
| `description`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | Free-form note about what this server is for.                                                                                                                                                                      |
| `connection`                                                                                                                                                                                                       | [Optional[models.McpConnection]](../../models/mcpconnection.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | How the gateway dials the upstream server.                                                                                                                                                                         |
| `auth`                                                                                                                                                                                                             | [Optional[models.McpAuthConfig]](../../models/mcpauthconfig.md)                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                 | Credentials the gateway sends upstream; send `type: NONE` explicitly for public servers.                                                                                                                           |
| `default_tool_exposure`                                                                                                                                                                                            | [Optional[models.McpToolExposure]](../../models/mcptoolexposure.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                 | Fallback exposure used by any gateway link that does not set its own.                                                                                                                                              |
| `sharing`                                                                                                                                                                                                          | [Optional[models.Sharing]](../../models/sharing.md)                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                 | Which projects in the workspace may use this server. Defaults to every project.                                                                                                                                    |
| `retries`                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                |

### Response

**[models.UpdateMcpServerResponse](../../models/updatemcpserverresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

    res = orq.mcp_servers.test_tool(id="<id>", tool_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the MCP server.                                                  |
| `tool_name`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | Bare upstream tool name, not a gateway's namespaced `exposed_name`.                   |
| `arguments`                                                                           | [Optional[models.Arguments]](../../models/arguments.md)                               | :heavy_minus_sign:                                                                    | Arguments passed to the tool, matching its `input_schema`.                            |
| `discovery_variables`                                                                 | Dict[str, *str*]                                                                      | :heavy_minus_sign:                                                                    | Values for the server's `template_variables`; treated as sensitive and not persisted. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.TestMcpServerToolResponse](../../models/testmcpservertoolresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

    res = orq.mcp_servers.sync(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the MCP server.                                                  |
| `discovery_variables`                                                                 | Dict[str, *str*]                                                                      | :heavy_minus_sign:                                                                    | Values for the server's `template_variables`; treated as sensitive and not persisted. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SyncMcpServerResponse](../../models/syncmcpserverresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |