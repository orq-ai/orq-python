# Traces

## Overview

### Available Operations

* [aggregate](#aggregate) - Aggregate traces
* [list_facets](#list_facets) - List trace facets
* [list_facet_values](#list_facet_values) - List trace facet values
* [list_fields](#list_fields) - List trace fields
* [query](#query) - Query traces with OQL
* [search](#search) - Search traces
* [get](#get) - Get trace
* [list_spans](#list_spans) - List trace spans
* [get_span](#get_span) - Get trace span

## aggregate

Aggregate trace metrics using the structured trace filter contract.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesAggregate" method="post" path="/v2/traces/aggregate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.aggregate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filters`                                                            | List[[models.TraceFilter](../../models/tracefilter.md)]              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `group_by`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `compute`                                                            | List[[models.TraceCompute](../../models/tracecompute.md)]            | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.AggregateTracesResponse](../../models/aggregatetracesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_facets

List trace fields that support facet value discovery.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesListFacets" method="get" path="/v2/traces/facets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.list_facets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTraceFacetsResponse](../../models/listtracefacetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_facet_values

List values and counts for one trace facet field.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesListFacetValues" method="get" path="/v2/traces/facets/{field}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.list_facet_values(field="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `field`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ListTraceFacetValuesResponse](../../models/listtracefacetvaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_fields

List currently supported static trace fields.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesListFields" method="get" path="/v2/traces/fields" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.list_fields()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListTraceFieldsResponse](../../models/listtracefieldsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## query

Run an OQL trace query. OQL is validated against the trace field registry and compiled through the trace planner.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesQueryOql" method="post" path="/v2/traces/query" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.query(from_=parse_datetime("2025-02-10T08:55:05.233Z"), to=parse_datetime("2024-12-12T15:00:42.128Z"), oql="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `oql`                                                                | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `page_token`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.QueryTracesResponse](../../models/querytracesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## search

Search trace summaries using the structured trace filter contract.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesSearch" method="post" path="/v2/traces/search" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.search(from_=parse_datetime("2025-05-02T22:00:26.030Z"), to=parse_datetime("2025-09-17T16:33:38.335Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `from_`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `to`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `filters`                                                            | List[[models.TraceFilter](../../models/tracefilter.md)]              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filter_operator`                                                    | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `query`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `sort`                                                               | List[[models.TraceSort](../../models/tracesort.md)]                  | :heavy_minus_sign:                                                   | N/A                                                                  |
| `limit`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `page_token`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.SearchTracesResponse](../../models/searchtracesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve one trace summary by trace id.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesGet" method="get" path="/v2/traces/{trace_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.get(trace_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trace_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTraceResponse](../../models/gettraceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_spans

List canonical span summaries for a trace.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesListSpans" method="get" path="/v2/traces/{trace_id}/spans" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.list_spans(trace_id="<id>")

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

**[models.ListTraceSpansResponse](../../models/listtracespansresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_span

Retrieve one hydrated span.

### Example Usage

<!-- UsageSnippet language="python" operationID="TracesGetSpan" method="get" path="/v2/traces/{trace_id}/spans/{span_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.traces.get_span(trace_id="<id>", span_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trace_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `span_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTraceSpanResponse](../../models/gettracespanresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |