# Router.Rerank

## Overview

### Available Operations

* [create](#create) - Create rerank

## create

Rerank a list of documents based on their relevance to a query.

### Example Usage

<!-- UsageSnippet language="python" operationID="createRerank" method="post" path="/v2/router/rerank" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.rerank.create(query="<value>", documents=[
        "<value 1>",
    ], model="XTS", retry={
        "on_codes": [
            429,
            500,
            502,
            503,
            504,
        ],
    }, cache={
        "ttl": 3600,
        "type": "exact_match",
    }, load_balancer={
        "type": "weight_based",
        "models": [],
    }, timeout={
        "call_timeout": 30000,
    }, orq={
        "fallbacks": [
            {
                "model": "openai/gpt-4o-mini",
            },
        ],
        "cache": {
            "ttl": 3600,
            "type": "exact_match",
        },
        "retry": {
            "on_codes": [
                429,
                500,
                502,
                503,
                504,
            ],
        },
        "identity": {
            "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "display_name": "Jane Doe",
            "email": "jane.doe@example.com",
            "metadata": [
                {
                    "department": "Engineering",
                    "role": "Senior Developer",
                },
            ],
            "logo_url": "https://example.com/avatars/jane-doe.jpg",
            "tags": [
                "hr",
                "engineering",
            ],
        },
        "load_balancer": {
            "type": "weight_based",
            "models": [
                {
                    "model": "openai/gpt-4o",
                    "weight": 0.7,
                },
                {
                    "model": "anthropic/claude-3-5-sonnet",
                    "weight": 0.3,
                },
            ],
        },
        "timeout": {
            "call_timeout": 30000,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                   | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The search query                                                                                                                                          |
| `documents`                                                                                                                                               | List[*str*]                                                                                                                                               | :heavy_check_mark:                                                                                                                                        | A list of texts that will be compared to the `query`. For optimal performance we recommend against sending more than 1,000 documents in a single request. |
| `model`                                                                                                                                                   | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The identifier of the model to use                                                                                                                        |
| `top_n`                                                                                                                                                   | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | The number of most relevant documents or indices to return, defaults to the length of the documents                                                       |
| `filename`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                        | The filename of the document to rerank                                                                                                                    |
| `name`                                                                                                                                                    | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | The name to display on the trace. If not specified, the default system name will be used.                                                                 |
| `fallbacks`                                                                                                                                               | List[[models.CreateRerankFallbacks](../../models/creatererankfallbacks.md)]                                                                               | :heavy_minus_sign:                                                                                                                                        | Array of fallback models to use if primary model fails                                                                                                    |
| `retry`                                                                                                                                                   | [Optional[models.CreateRerankRetry]](../../models/creatererankretry.md)                                                                                   | :heavy_minus_sign:                                                                                                                                        | Retry configuration for the request                                                                                                                       |
| `cache`                                                                                                                                                   | [Optional[models.CreateRerankCache]](../../models/creatererankcache.md)                                                                                   | :heavy_minus_sign:                                                                                                                                        | Cache configuration for the request.                                                                                                                      |
| `load_balancer`                                                                                                                                           | [Optional[models.CreateRerankLoadBalancer]](../../models/creatererankloadbalancer.md)                                                                     | :heavy_minus_sign:                                                                                                                                        | Load balancer configuration for the request.                                                                                                              |
| `timeout`                                                                                                                                                 | [Optional[models.CreateRerankTimeout]](../../models/createreranktimeout.md)                                                                               | :heavy_minus_sign:                                                                                                                                        | Timeout configuration to apply to the request. If the request exceeds the timeout, it will be retried or fallback to the next model if configured.        |
| `orq`                                                                                                                                                     | [Optional[models.CreateRerankOrq]](../../models/creatererankorq.md)                                                                                       | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CreateRerankResponseBody](../../models/creatererankresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |