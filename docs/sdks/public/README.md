# Public
(*public*)

## Overview

### Available Operations

* [delete_v2_deployments_invalidate_deployment_id_](#delete_v2_deployments_invalidate_deployment_id_) - Invalidates cache

## delete_v2_deployments_invalidate_deployment_id_

Explicitly invalidate a cache of a deployment

### Example Usage

```python
from orq_ai_sdk import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

s.public.delete_v2_deployments_invalidate_deployment_id_(deployment_id="2f8f323e-7a21-40c4-8729-612ffe6e2dcb")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deployment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |