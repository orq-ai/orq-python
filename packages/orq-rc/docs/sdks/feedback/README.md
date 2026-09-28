# Feedback

## Overview

### Available Operations

* [remove_evaluation](#remove_evaluation)
* [create_evaluation](#create_evaluation)
* [remove](#remove)
* [create](#create)
* [submit](#submit) - Submit feedback

## remove_evaluation

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/evaluation/remove" method="post" path="/v2/feedback/evaluation/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.feedback.remove_evaluation()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.PostV2FeedbackEvaluationRemoveRequestBody](../../models/postv2feedbackevaluationremoverequestbody.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_evaluation

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/evaluation" method="post" path="/v2/feedback/evaluation" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.feedback.create_evaluation()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.PostV2FeedbackEvaluationRequestBody](../../models/postv2feedbackevaluationrequestbody.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## remove

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/remove" method="post" path="/v2/feedback/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.remove()

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
| models.APIDefaultError                          | 4XX, 5XX                                        | \*/\*                                           |

## create

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback" method="post" path="/v2/feedback" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.create()

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
| models.APIDefaultError                            | 4XX, 5XX                                          | \*/\*                                             |

## submit

Report problems or request features for Orq.ai APIs, MCP tools, SDKs, and documentation.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubmitFeedback" method="post" path="/v3/submit-feedback" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.submit(message="<value>", category="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `message`                                                                         | *str*                                                                             | :heavy_check_mark:                                                                | What happened, what was expected, and steps to reproduce. Do not include secrets. |
| `category`                                                                        | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `request_id`                                                                      | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `url`                                                                             | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.SubmitFeedbackResponse](../../models/submitfeedbackresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |