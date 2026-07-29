# McpGatewayCalls

## Overview

### Available Operations

* [list](#list) - List MCP gateway calls

## list

Returns a paginated audit log of tool calls made through MCP gateways.

### Example Usage

<!-- UsageSnippet language="python" operationID="McpGatewayCallList" method="get" path="/v2/mcp-gateway-calls" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.mcp_gateway_calls.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `starting_after`                                                              | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `ending_before`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `mcp_gateway_id`                                                              | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `mcp_server_id`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `status`                                                                      | [Optional[models.McpGatewayCallStatus]](../../models/mcpgatewaycallstatus.md) | :heavy_minus_sign:                                                            | N/A                                                                           |
| `start_time`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `end_time`                                                                    | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ListMcpGatewayCallsResponse](../../models/listmcpgatewaycallsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |