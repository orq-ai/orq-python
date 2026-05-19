# Feedback

## Overview

### Available Operations

* [post_v2_feedback](#post_v2_feedback)
* [post_v2_feedback_remove](#post_v2_feedback_remove)

## post_v2_feedback

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback" method="post" path="/v2/feedback" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.post_v2_feedback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.PostV2FeedbackRequestBody](../../models/postv2feedbackrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.PostV2FeedbackResponseBody](../../models/postv2feedbackresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.PostV2FeedbackFeedbackResponseBody         | 400                                               | application/json                                  |
| models.PostV2FeedbackFeedbackResponseResponseBody | 404                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## post_v2_feedback_remove

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/remove" method="post" path="/v2/feedback/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.post_v2_feedback_remove()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.PostV2FeedbackRemoveRequestBody](../../models/postv2feedbackremoverequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.PostV2FeedbackRemoveResponseBody](../../models/postv2feedbackremoveresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.PostV2FeedbackRemoveFeedbackResponseBody | 404                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |