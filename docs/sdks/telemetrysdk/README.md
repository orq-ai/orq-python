# Telemetry

## Overview

### Available Operations

* [query](#query) - Query telemetry

## query

Unified query envelope for traces, metrics, and logs. Selects a source, a compute list, and a time range, with optional grain, group-by, and filters; returns a time series or a single aggregate row per group.

### Example Usage

<!-- UsageSnippet language="python" operationID="TelemetryQuery" method="post" path="/v2/telemetry/query" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.telemetry.query()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `source`                                                                                  | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `from_`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `to`                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                      | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `compute`                                                                                 | List[[models.TraceCompute](../../models/tracecompute.md)]                                 | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `grain`                                                                                   | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Empty string and "none" are equivalent: a single row per group instead<br/> of a time series. |
| `group_by`                                                                                | List[*str*]                                                                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `filters`                                                                                 | List[[models.TraceFilter](../../models/tracefilter.md)]                                   | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `filter_operator`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `limit`                                                                                   | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `time_zone`                                                                               | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `include_totals`                                                                          | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.QueryTelemetryResponse](../../models/querytelemetryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |