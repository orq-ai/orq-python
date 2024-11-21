# Metrics
(*deployments.metrics*)

## Overview

### Available Operations

* [create](#create) - Add metrics

## create

Add metrics to a deployment

### Example Usage

```python
from orq_ai_sdk import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.deployments.metrics.create(id="<id>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | Deployment ID                                                                                 |
| `request_body`                                                                                | [models.DeploymentCreateMetricRequestBody](../../models/deploymentcreatemetricrequestbody.md) | :heavy_check_mark:                                                                            | The deployment request payload                                                                |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.DeploymentCreateMetricResponseBody](../../models/deploymentcreatemetricresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |