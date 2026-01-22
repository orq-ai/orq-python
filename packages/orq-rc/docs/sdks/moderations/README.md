# Router.Moderations

## Overview

### Available Operations

* [create](#create) - Create moderation

## create

Create moderation

### Example Usage

<!-- UsageSnippet language="python" operationID="createModeration" method="post" path="/v2/router/moderations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.moderations.create(input_=[], model="Fiesta")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `input`                                                                                                                                       | [models.Input](../../models/input.md)                                                                                                         | :heavy_check_mark:                                                                                                                            | Input (or inputs) to classify. Can be a single string, an array of strings, or an array of multi-modal input objects similar to other models. |
| `model`                                                                                                                                       | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The content moderation model you would like to use. Defaults to omni-moderation-latest                                                        |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.CreateModerationResponseBody](../../models/createmoderationresponsebody.md)**

### Errors

| Error Type                                           | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| models.CreateModerationRouterModerationsResponseBody | 422                                                  | application/json                                     |
| models.APIError                                      | 4XX, 5XX                                             | \*/\*                                                |