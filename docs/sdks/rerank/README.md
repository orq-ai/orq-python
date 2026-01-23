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
    ], model="XTS", orq={
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
        "contact": {
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
| `orq`                                                                                                                                                     | [Optional[models.CreateRerankOrq]](../../models/creatererankorq.md)                                                                                       | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.CreateRerankResponseBody](../../models/creatererankresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |