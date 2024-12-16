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

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.feedback.create(field="rating", value=[
        "good",
    ], trace_id="67HTZ65Z9W91HSF51CW68KK1QH")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `field`                                                                                                                                               | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | A string describing the specific property or aspect rated.                                                                                            |
| `value`                                                                                                                                               | [models.Value](../../models/value.md)                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string. |
| `trace_id`                                                                                                                                            | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints                              |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.CreateFeedbackResponseBody](../../models/createfeedbackresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |