# Orq SDK

## Overview

orq.ai API: orq.ai API documentation

orq.ai Documentation
<https://docs.orq.ai>

### Available Operations

* [post_v2_feedback_evaluation_remove](#post_v2_feedback_evaluation_remove)
* [post_v2_feedback_evaluation](#post_v2_feedback_evaluation)

## post_v2_feedback_evaluation_remove

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/evaluation/remove" method="post" path="/v2/feedback/evaluation/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.post_v2_feedback_evaluation_remove()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.PostV2FeedbackEvaluationRemoveRequestBody](../../models/postv2feedbackevaluationremoverequestbody.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_v2_feedback_evaluation

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/evaluation" method="post" path="/v2/feedback/evaluation" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.post_v2_feedback_evaluation()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.PostV2FeedbackEvaluationRequestBody](../../models/postv2feedbackevaluationrequestbody.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |