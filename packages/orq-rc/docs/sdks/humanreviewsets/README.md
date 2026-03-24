# HumanReviewSets

## Overview

### Available Operations

* [get_v2_human_eval_sets](#get_v2_human_eval_sets) - Get all human review sets
* [post_v2_human_eval_sets](#post_v2_human_eval_sets) - Create a human review set
* [get_v2_human_eval_sets_id_](#get_v2_human_eval_sets_id_) - Get a human review set by ID
* [patch_v2_human_eval_sets_id_](#patch_v2_human_eval_sets_id_) - Update a human review set
* [delete_v2_human_eval_sets_id_](#delete_v2_human_eval_sets_id_) - Delete a human review set

## get_v2_human_eval_sets

Get all human review sets

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/human-eval-sets" method="get" path="/v2/human-eval-sets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.human_review_sets.get_v2_human_eval_sets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional project ID to filter human review sets by project          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetV2HumanEvalSetsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## post_v2_human_eval_sets

Create a human review set

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/human-eval-sets" method="post" path="/v2/human-eval-sets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.human_review_sets.post_v2_human_eval_sets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.PostV2HumanEvalSetsRequestBody](../../models/postv2humanevalsetsrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.PostV2HumanEvalSetsResponseBody](../../models/postv2humanevalsetsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_v2_human_eval_sets_id_

Get a human review set by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/human-eval-sets/{id}" method="get" path="/v2/human-eval-sets/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.human_review_sets.get_v2_human_eval_sets_id_(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the human review set to retrieve                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2HumanEvalSetsIDResponseBody](../../models/getv2humanevalsetsidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## patch_v2_human_eval_sets_id_

Update a human review set

### Example Usage

<!-- UsageSnippet language="python" operationID="patch_/v2/human-eval-sets/{id}" method="patch" path="/v2/human-eval-sets/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.human_review_sets.patch_v2_human_eval_sets_id_(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                    | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the human review set to retrieve                                                              |
| `request_body`                                                                                          | [Optional[models.PatchV2HumanEvalSetsIDRequestBody]](../../models/patchv2humanevalsetsidrequestbody.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.PatchV2HumanEvalSetsIDResponseBody](../../models/patchv2humanevalsetsidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_v2_human_eval_sets_id_

Delete a human review set

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/v2/human-eval-sets/{id}" method="delete" path="/v2/human-eval-sets/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.human_review_sets.delete_v2_human_eval_sets_id_(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the human review set to retrieve                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |