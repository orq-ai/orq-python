# Feedback
(*feedback*)

## Overview

### Available Operations

* [create](#create) - Submit feedback

## create

Submit feedback for the LLM transaction via the API

### Example Usage

```python
from orq_ai_sdk import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.feedback.create(request={
    "property": "rating",
    "value": [
        "good",
    ],
    "trace_id": "67HTZ65Z9W91HSF51CW68KK1QH",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CreateFeedbackRequestBody](../../models/createfeedbackrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateFeedbackResponseBody](../../models/createfeedbackresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |