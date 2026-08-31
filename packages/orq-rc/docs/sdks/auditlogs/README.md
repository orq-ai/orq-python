# AuditLogs

## Overview

### Available Operations

* [query](#query) - Query audit logs

## query

Queries audit logs from your workspace with filters, sorting, and cursor pagination.

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogQuery" method="post" path="/v2/audit-logs/query" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.audit_logs.query(filters={
        "operator": "and",
        "filters": [
            {
                "type": "string",
                "path": "entity_type",
                "operator": "is",
                "value": "skill",
            },
        ],
    }, pagination={
        "limit": 20,
    }, sorting=[
        {
            "key": "created_at",
            "direction": "desc",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filters`                                                           | [models.AuditLogFilterQuery](../../models/auditlogfilterquery.md)   | :heavy_check_mark:                                                  | Search and advanced filters for querying audit logs.                |
| `pagination`                                                        | [models.AuditLogPagination](../../models/auditlogpagination.md)     | :heavy_check_mark:                                                  | Cursor pagination settings for audit log queries.                   |
| `sorting`                                                           | List[[models.AuditLogSort](../../models/auditlogsort.md)]           | :heavy_minus_sign:                                                  | Sort expressions. Defaults to audit_log_id descending when omitted. |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.QueryAuditLogsResponse](../../models/queryauditlogsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |