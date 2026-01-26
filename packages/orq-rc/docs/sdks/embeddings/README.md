# Router.Embeddings

## Overview

### Available Operations

* [create](#create) - Create embeddings

## create

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

### Example Usage

<!-- UsageSnippet language="python" operationID="createEmbedding" method="post" path="/v2/router/embeddings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.embeddings.create(input_=[
        "<value 1>",
        "<value 2>",
    ], model="V90", encoding_format="float", fallbacks=[
        {
            "model": "openai/text-embedding-3-small",
        },
    ], retry={
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
        "models": [
            {
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
        ],
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

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input`                                                                                                                                            | [models.CreateEmbeddingInput](../../models/createembeddinginput.md)                                                                                | :heavy_check_mark:                                                                                                                                 | Input text to embed, encoded as a string or array of tokens.                                                                                       |
| `model`                                                                                                                                            | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | ID of the model to use                                                                                                                             |
| `encoding_format`                                                                                                                                  | [Optional[models.EncodingFormat]](../../models/encodingformat.md)                                                                                  | :heavy_minus_sign:                                                                                                                                 | Type of the document element                                                                                                                       |
| `dimensions`                                                                                                                                       | *Optional[float]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                 | The number of dimensions the resulting output embeddings should have.                                                                              |
| `user`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | A unique identifier representing your end-user                                                                                                     |
| `name`                                                                                                                                             | *Optional[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                 | The name to display on the trace. If not specified, the default system name will be used.                                                          |
| `fallbacks`                                                                                                                                        | List[[models.CreateEmbeddingFallbacks](../../models/createembeddingfallbacks.md)]                                                                  | :heavy_minus_sign:                                                                                                                                 | Array of fallback models to use if primary model fails                                                                                             |
| `retry`                                                                                                                                            | [Optional[models.CreateEmbeddingRetry]](../../models/createembeddingretry.md)                                                                      | :heavy_minus_sign:                                                                                                                                 | Retry configuration for the request                                                                                                                |
| `cache`                                                                                                                                            | [Optional[models.CreateEmbeddingCache]](../../models/createembeddingcache.md)                                                                      | :heavy_minus_sign:                                                                                                                                 | Cache configuration for the request.                                                                                                               |
| `load_balancer`                                                                                                                                    | [Optional[models.CreateEmbeddingLoadBalancer]](../../models/createembeddingloadbalancer.md)                                                        | :heavy_minus_sign:                                                                                                                                 | Load balancer configuration for the request.                                                                                                       |
| `timeout`                                                                                                                                          | [Optional[models.CreateEmbeddingTimeout]](../../models/createembeddingtimeout.md)                                                                  | :heavy_minus_sign:                                                                                                                                 | Timeout configuration to apply to the request. If the request exceeds the timeout, it will be retried or fallback to the next model if configured. |
| `orq`                                                                                                                                              | [Optional[models.CreateEmbeddingOrq]](../../models/createembeddingorq.md)                                                                          | :heavy_minus_sign:                                                                                                                                 | N/A                                                                                                                                                |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.CreateEmbeddingResponseBody](../../models/createembeddingresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |