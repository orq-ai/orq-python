# Reporting

## Overview

### Available Operations

* [query](#query) - Query reporting metrics

## query

Returns time-series analytics for AI usage, cost, latency, evaluator results, and guardrail outcomes. Select a metric and time range, break results down by supported dimensions, apply filters, and optionally include totals for the full range.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReportingQuery" method="post" path="/v2/reporting" -->
```python
from orq_ai_sdk import Orq
from orq_ai_sdk.utils import parse_datetime
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.reporting.query(metric="genai.evaluator.score.avg", from_=parse_datetime("2026-12-14T22:21:09.964Z"), to=parse_datetime("2026-03-06T12:20:53.904Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `metric`                                                                                                                       | [models.Metric](../../models/metric.md)                                                                                        | :heavy_check_mark:                                                                                                             | Catalogue metric to query.                                                                                                     |
| `from_`                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                           | :heavy_check_mark:                                                                                                             | Inclusive lower bound for the report window (RFC 3339, UTC).                                                                   |
| `to`                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                           | :heavy_check_mark:                                                                                                             | Exclusive upper bound for the report window (RFC 3339, UTC).                                                                   |
| `grain`                                                                                                                        | [Optional[models.Grain]](../../models/grain.md)                                                                                | :heavy_minus_sign:                                                                                                             | Requested bucket grain. Use `auto` or omit the field to let the server choose based on the requested range.                    |
| `group_by`                                                                                                                     | List[[models.GroupBy](../../models/groupby.md)]                                                                                | :heavy_minus_sign:                                                                                                             | Reporting dimensions to break down by. Valid dimensions depend on the selected metric.                                         |
| `filters`                                                                                                                      | List[[models.Filter](../../models/filter_.md)]                                                                                 | :heavy_minus_sign:                                                                                                             | Up to 20 allowlisted predicates combined with AND.                                                                             |
| `limit`                                                                                                                        | *Optional[int]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Maximum bucket rows returned. Defaults to 1000 and is capped at<br/> 5000.                                                     |
| `time_zone`                                                                                                                    | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | IANA time zone applied to bucket boundaries, for example<br/> `America/New_York`. Response timestamps remain UTC. Empty means UTC. |
| `include_totals`                                                                                                               | *Optional[bool]*                                                                                                               | :heavy_minus_sign:                                                                                                             | When true, include a `totals` block aggregated across the full<br/> report window.                                             |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[models.QueryReportResponse](../../models/queryreportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |