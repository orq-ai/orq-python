# Orq SDK

## Overview

[Dev] orq.ai API: orq.ai API documentation

orq.ai Documentation
<https://docs.orq.ai>

### Available Operations

* [post_v2_traces_sessions_count](#post_v2_traces_sessions_count) - Get total count of sessions

## post_v2_traces_sessions_count

Get total count of sessions

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.post_v2_traces_sessions_count()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.PostV2TracesSessionsCountRequestBody](../../models/postv2tracessessionscountrequestbody.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.PostV2TracesSessionsCountResponseBody](../../models/postv2tracessessionscountresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |