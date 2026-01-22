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
    ], model="V90", encoding_format="float", orq={
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
        "load_balancer": [
            {
                "type": "weight_based",
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
            {
                "type": "weight_based",
                "model": "openai/gpt-4o",
                "weight": 0.7,
            },
        ],
        "timeout": {
            "call_timeout": 30000,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `input`                                                                   | [models.CreateEmbeddingInput](../../models/createembeddinginput.md)       | :heavy_check_mark:                                                        | Input text to embed, encoded as a string or array of tokens.              |
| `model`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | ID of the model to use                                                    |
| `encoding_format`                                                         | [Optional[models.EncodingFormat]](../../models/encodingformat.md)         | :heavy_minus_sign:                                                        | Type of the document element                                              |
| `dimensions`                                                              | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | The number of dimensions the resulting output embeddings should have.     |
| `user`                                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A unique identifier representing your end-user                            |
| `orq`                                                                     | [Optional[models.CreateEmbeddingOrq]](../../models/createembeddingorq.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateEmbeddingResponseBody](../../models/createembeddingresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |