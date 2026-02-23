# Annotations

## Overview

### Available Operations

* [create](#create) - Annotate a span
* [delete](#delete) - Remove an annotation from a span

## create

Annotate a span

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAnnotation" method="post" path="/v2/traces/{trace_id}/spans/{span_id}/annotation" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.annotations.create(trace_id="<id>", span_id="<id>", annotations=[])

    # Use the SDK ...

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `trace_id`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | Unique identifier of the trace                                                          |
| `span_id`                                                                               | *str*                                                                                   | :heavy_check_mark:                                                                      | Unique identifier of the span                                                           |
| `annotations`                                                                           | List[[models.CreateAnnotationAnnotations](../../models/createannotationannotations.md)] | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `metadata`                                                                              | [Optional[models.CreateAnnotationMetadata]](../../models/createannotationmetadata.md)   | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Remove an annotation from a span

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAnnotation" method="delete" path="/v2/traces/{trace_id}/spans/{span_id}/annotation" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.annotations.delete(trace_id="<id>", span_id="<id>", keys=[
        "<value 1>",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trace_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the trace                                      |
| `span_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the span                                       |
| `keys`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |