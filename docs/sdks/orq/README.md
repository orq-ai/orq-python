# Orq SDK

## Overview

orq.ai API: orq.ai API documentation

orq.ai Documentation
<https://docs.orq.ai>

### Available Operations

* [post_v2_feedback](#post_v2_feedback)
* [post_v2_feedback_evaluation_remove](#post_v2_feedback_evaluation_remove)
* [post_v2_feedback_evaluation](#post_v2_feedback_evaluation)
* [post_v2_feedback_remove](#post_v2_feedback_remove)
* [get_v2_human_evals](#get_v2_human_evals)
* [post_v2_human_evals](#post_v2_human_evals)
* [get_v2_human_evals_id_](#get_v2_human_evals_id_)
* [patch_v2_human_evals_id_](#patch_v2_human_evals_id_)
* [delete_v2_human_evals_id_](#delete_v2_human_evals_id_)

## post_v2_feedback

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback" method="post" path="/v2/feedback" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.post_v2_feedback()

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

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.PostV2FeedbackResponseResponseBody    | 400                                          | application/json                             |
| models.PostV2FeedbackResponse404ResponseBody | 404                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

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

## post_v2_feedback_remove

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/feedback/remove" method="post" path="/v2/feedback/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.post_v2_feedback_remove()

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
| models.PostV2FeedbackRemoveResponseResponseBody | 404                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## get_v2_human_evals

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/human-evals" method="get" path="/v2/human-evals" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.get_v2_human_evals()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional project ID to filter human reviews by project              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.GetV2HumanEvalsResponseBody | 404                                | application/json                   |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |

## post_v2_human_evals

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/human-evals" method="post" path="/v2/human-evals" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.post_v2_human_evals()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.PostV2HumanEvalsRequestBody](../../models/postv2humanevalsrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.PostV2HumanEvalsResponseBody](../../models/postv2humanevalsresponsebody.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.PostV2HumanEvalsResponseResponseBody | 404                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## get_v2_human_evals_id_

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/human-evals/{id}" method="get" path="/v2/human-evals/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.get_v2_human_evals_id_(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The id of the resource                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2HumanEvalsIDResponseBody](../../models/getv2humanevalsidresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.GetV2HumanEvalsIDResponseResponseBody | 404                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## patch_v2_human_evals_id_

### Example Usage

<!-- UsageSnippet language="python" operationID="patch_/v2/human-evals/{id}" method="patch" path="/v2/human-evals/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.patch_v2_human_evals_id_(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *str*                                                                                             | :heavy_check_mark:                                                                                | The id of the resource                                                                            |
| `request_body`                                                                                    | [Optional[models.PatchV2HumanEvalsIDRequestBody]](../../models/patchv2humanevalsidrequestbody.md) | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.PatchV2HumanEvalsIDResponseBody](../../models/patchv2humanevalsidresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.PatchV2HumanEvalsIDResponseResponseBody | 404                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## delete_v2_human_evals_id_

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/v2/human-evals/{id}" method="delete" path="/v2/human-evals/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.delete_v2_human_evals_id_(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The id of the resource                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteV2HumanEvalsIDResponseBody](../../models/deletev2humanevalsidresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.DeleteV2HumanEvalsIDResponseResponseBody | 404                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |