# McpSessions

## Overview

### Available Operations

* [list](#list) - List MCP sessions
* [revoke](#revoke) - Revoke an MCP session

## list

Returns a paginated list of per-user OAuth sessions for MCP gateways.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpSessionList" method="get" path="/v2/mcp-sessions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_sessions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `starting_after`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `ending_before`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `mcp_gateway_id`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `mcp_server_id`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `account_id`                                                          | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `status`                                                              | [Optional[models.McpSessionStatus]](../../models/mcpsessionstatus.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListMcpSessionsResponse](../../models/listmcpsessionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## revoke

Revokes a per-user OAuth session, invalidating the stored upstream token.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpSessionRevoke" method="delete" path="/v2/mcp-sessions/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_sessions.revoke(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RevokeMcpSessionResponse](../../models/revokemcpsessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |