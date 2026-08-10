# Annotations

## Overview

### Available Operations

* [create](#create) - Annotate a span
* [delete](#delete) - Remove an annotation from a span

## create

Attach one or more annotations to a specific span. A standard annotation references a human review by key and supplies a value. A correction references an existing evaluator output by parent_annotation_id and supplies the corrected value, validated against that evaluator's output schema.

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

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Remove one or more annotations from a specific span by their evaluator keys, or remove corrections by the eval ids of their parent annotations.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAnnotation" method="delete" path="/v2/traces/{trace_id}/spans/{span_id}/annotation" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.annotations.delete(trace_id="<id>", span_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `trace_id`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the trace                                                        |
| `span_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | Unique identifier of the span                                                         |
| `keys`                                                                                | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Unique keys of the reviews to remove                                                  |
| `parent_annotation_ids`                                                               | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Eval ids whose corrections should be removed                                          |
| `metadata`                                                                            | [Optional[models.DeleteAnnotationMetadata]](../../models/deleteannotationmetadata.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |