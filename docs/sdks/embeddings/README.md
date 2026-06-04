# Router.Embeddings

## Overview

### Available Operations

* [create](#create) - Create embeddings

## create

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

### Example Usage: array_of_strings

<!-- UsageSnippet language="python" operationID="createEmbedding" method="post" path="/v2/router/embeddings" example="array_of_strings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.embeddings.create(input=[
        "The food was delicious",
        "And the waiter was friendly",
    ], model="openai/text-embedding-3-small", orq={
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
    })

    # Handle response
    print(res)

```
### Example Usage: single_string

<!-- UsageSnippet language="python" operationID="createEmbedding" method="post" path="/v2/router/embeddings" example="single_string" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.embeddings.create(input="The food was delicious and the waiter...", model="openai/text-embedding-3-small", orq={
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
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `input`                                                                                     | [models.CreateEmbeddingInput](../../models/createembeddinginput.md)                         | :heavy_check_mark:                                                                          | Input text to embed, encoded as a string or array of tokens.                                |
| `model`                                                                                     | *str*                                                                                       | :heavy_check_mark:                                                                          | ID of the model to use.                                                                     |
| `cache`                                                                                     | [Optional[models.EmbeddingCacheConfig]](../../models/embeddingcacheconfig.md)               | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `dimensions`                                                                                | *Optional[int]*                                                                             | :heavy_minus_sign:                                                                          | The number of dimensions the resulting output embeddings should have.                       |
| `encoding_format`                                                                           | [Optional[models.EncodingFormat]](../../models/encodingformat.md)                           | :heavy_minus_sign:                                                                          | The format to return the embeddings in. Can be either float or base64.                      |
| `fallbacks`                                                                                 | List[[models.FallbackConfig](../../models/fallbackconfig.md)]                               | :heavy_minus_sign:                                                                          | Array of fallback models to use if primary model fails.                                     |
| `load_balancer`                                                                             | [Optional[models.EmbeddingLoadBalancerConfig]](../../models/embeddingloadbalancerconfig.md) | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `name`                                                                                      | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | The name to display on the trace. If not specified, the default system name will be used.   |
| `orq`                                                                                       | [Optional[models.EmbeddingOrqParams]](../../models/embeddingorqparams.md)                   | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `retry`                                                                                     | [Optional[models.EmbeddingRetryConfig]](../../models/embeddingretryconfig.md)               | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `timeout`                                                                                   | [Optional[models.EmbeddingTimeoutConfig]](../../models/embeddingtimeoutconfig.md)           | :heavy_minus_sign:                                                                          | N/A                                                                                         |
| `user`                                                                                      | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | A unique identifier representing your end-user.                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.CreateEmbeddingResponseBody](../../models/createembeddingresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |