# Pii

## Overview

### Available Operations

* [detect](#detect) - Detect PII
* [redact](#redact) - Redact PII
* [restore](#restore) - Restore redacted text

## detect

Reports whether the supplied text contains personally identifiable information, optionally with a per-type entity breakdown.

### Example Usage

<!-- UsageSnippet language="python" operationID="PIIDetect" method="post" path="/v2/pii/detect" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.pii.detect()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `text`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Text to analyse.                                                            |
| `language`                                                                  | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | BCP-47 language code. Unset means auto-detect.                              |
| `threshold`                                                                 | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | Global minimum recognizer score (0.0-1.0). Unset uses the provider default. |
| `include_entities`                                                          | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | When true, the response includes a per-type entity breakdown.               |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.DetectResponse](../../models/detectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## redact

Replaces detected PII with placeholders and returns the reverse mapping needed to restore the original text.

### Example Usage

<!-- UsageSnippet language="python" operationID="PIIRedact" method="post" path="/v2/pii/redact" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.pii.redact()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `text`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `language`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `threshold`                                                         | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RedactResponse](../../models/redactresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## restore

Reverses a redaction, substituting placeholders back to their original values using the mapping returned by Redact.

### Example Usage

<!-- UsageSnippet language="python" operationID="PIIRestore" method="post" path="/v2/pii/restore" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.pii.restore()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `redacted_text`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `mappings`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | Placeholder-to-original mapping produced by Redact.                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RestoreResponse](../../models/restoreresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |