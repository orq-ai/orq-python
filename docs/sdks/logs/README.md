# Logs

## Overview

### Available Operations

* [list_trace_logs](#list_trace_logs) - List logs for a trace
* [aggregate](#aggregate) - Aggregate logs
* [list_facets](#list_facets) - List log facets
* [list_facet_values](#list_facet_values) - List facet values
* [list_fields](#list_fields) - List log fields
* [find_patterns](#find_patterns) - Find log patterns
* [query](#query) - Query logs with OQL
* [search](#search) - Search logs
* [get](#get) - Get a single log
* [context](#context) - Get surrounding log context

## list_trace_logs

Return all log records correlated with a given trace_id. Results are scoped to the authenticated workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListTraceLogs" method="get" path="/v2/traces/{trace_id}/logs" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.list_trace_logs(trace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trace_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_token`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTraceLogsResponse](../../models/listtracelogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## aggregate

Return severity counts grouped by time buckets at a configurable grain (auto, minute, hour, day).

### Example Usage

<!-- UsageSnippet language="python" operationID="AggregateLogs" method="post" path="/v3/logs/aggregate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.aggregate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                             | N/A                                                                                                                                                                                                            |
| `to`                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                             | N/A                                                                                                                                                                                                            |
| `grain`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | Time bucket grain: "auto" \| "minute" \| "hour" \| "day", matching the shared<br/> libs/go/reporting Grain vocabulary used by the traces reporting API. Empty<br/> defaults to "auto" (grain picked from the time range). |
| `filters`                                                                                                                                                                                                      | List[[models.TraceFilter](../../models/tracefilter.md)]                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                             | N/A                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                            |

### Response

**[models.AggregateLogsResponse](../../models/aggregatelogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_facets

Return the facet hierarchy: attribute families (native, attribute, resource, scope) with their keys, counts, and top values for the requested time range.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListLogFacets" method="get" path="/v3/logs/facets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.list_facets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `key_limit`                                                          | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `value_limit`                                                        | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ListLogFacetsResponse](../../models/listlogfacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_facet_values

Return distinct values with occurrence counts for a given facet field.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListLogFacetValues" method="get" path="/v3/logs/facets/{field}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.list_facet_values(field="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `field`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `search`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional case-insensitive substring search over facet values.        |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ListLogFacetValuesResponse](../../models/listlogfacetvaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_fields

Return all queryable fields: static columns and dynamic attribute families (attribute.*, resource.*).

### Example Usage

<!-- UsageSnippet language="python" operationID="ListLogFields" method="get" path="/v3/logs/fields" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.list_fields()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListLogFieldsResponse](../../models/listlogfieldsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## find_patterns

Find stable templates in a bounded sample of matching log bodies. The response reports sampling and truncation metadata and never returns an unbounded list of raw bodies.

### Example Usage

<!-- UsageSnippet language="python" operationID="FindLogPatterns" method="post" path="/v3/logs/patterns" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.find_patterns(from_=parse_datetime("2025-09-21T07:55:29.692Z"), to=parse_datetime("2024-10-05T00:49:57.596Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `query`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filters`                                                            | List[[models.TraceFilter](../../models/tracefilter.md)]              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Maximum patterns to return. Defaults to 50.                          |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.FindLogPatternsResponse](../../models/findlogpatternsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## query

Run an OQL log query using the pipeline grammar `fetch logs | filter <expr> | sort timestamp desc | limit N`. The query is compiled onto the same engine as SearchLogs; timestamp desc is the only supported sort.

### Example Usage

<!-- UsageSnippet language="python" operationID="QueryLogs" method="post" path="/v3/logs/query" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.query(oql="<value>", from_=parse_datetime("2026-04-01T20:23:07.108Z"), to=parse_datetime("2025-08-17T16:51:30.424Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `oql`                                                                                              | *str*                                                                                              | :heavy_check_mark:                                                                                 | OQL query string, e.g.<br/> `fetch logs \| filter severity_number > 10 \| filter body contains "error"`. |
| `from_`                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                               | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `to`                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                               | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `limit`                                                                                            | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Maximum rows to return; a `\| limit N` pipeline command takes precedence.                          |
| `page_token`                                                                                       | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Opaque cursor for pagination.                                                                      |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.QueryLogsResponse](../../models/querylogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## search

Query log records with filters, free-text search, and keyset pagination. Results are ordered timestamp desc (the only supported sort, mirroring traces).

### Example Usage

<!-- UsageSnippet language="python" operationID="SearchLogs" method="post" path="/v3/logs/search" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.search()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `from_`                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `to`                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                             | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `query`                                                                                          | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Free-text query matched against the body field (case-insensitive).                               |
| `filter_operator`                                                                                | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | How to combine multiple filters: "and" (default) or "or", mirroring<br/> the traces filter_operator. |
| `filters`                                                                                        | List[[models.TraceFilter](../../models/tracefilter.md)]                                          | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `sort`                                                                                           | List[[models.TraceSort](../../models/tracesort.md)]                                              | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `limit`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | Maximum rows to return. Defaults to 100 and is capped at 1000.                                   |
| `page_token`                                                                                     | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Opaque cursor for pagination; empty or absent means the first page.                              |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.SearchLogsResponse](../../models/searchlogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a log record by its ULID. Returns 404 if the record does not exist or belongs to another workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetLog" method="get" path="/v3/logs/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetLogResponse](../../models/getlogresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## context

Retrieve the matching log records immediately before and after an anchor log. Neighbors use the same free-text and structured filter dialect as SearchLogs and are returned in chronological order.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetLogContext" method="post" path="/v3/logs/{id}/context" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.logs.context(id="<id>", from_=parse_datetime("2025-10-13T07:44:36.992Z"), to=parse_datetime("2025-04-02T17:30:56.013Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `query`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filters`                                                            | List[[models.TraceFilter](../../models/tracefilter.md)]              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `before`                                                             | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Number of matching records earlier than the anchor. Defaults to 10.  |
| `after`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Number of matching records later than the anchor. Defaults to 10.    |
| `oql`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional OQL pipeline. It cannot be combined with query or filters.  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.GetLogContextResponse](../../models/getlogcontextresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |