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


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.deployments.metrics.create(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | Deployment ID                                                                                                                                                                                            |
| `metadata`                                                                                                                                                                                               | Dict[str, *Any*]                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Your own custom key-value pairs can be attached to the logs. This is useful for storing additional information related to your interactions with the LLM providers or specifics within your application. |
| `usage`                                                                                                                                                                                                  | [Optional[models.Usage]](../../models/usage.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Usage statistics to add to the deployment                                                                                                                                                                |
| `performance`                                                                                                                                                                                            | [Optional[models.Performance]](../../models/performance.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                       | N/A                                                                                                                                                                                                      |
| `messages`                                                                                                                                                                                               | List[[models.DeploymentCreateMetricMessages](../../models/deploymentcreatemetricmessages.md)]                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                       | A list of messages sent to the model.                                                                                                                                                                    |
| `choices`                                                                                                                                                                                                | List[[models.Choices](../../models/choices.md)]                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | A list of completion choices. If you are using a `completion` model then you must provide the `completion content` with the chat completion format                                                       |
| `feedback`                                                                                                                                                                                               | [Optional[models.DeploymentCreateMetricFeedback]](../../models/deploymentcreatemetricfeedback.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                       | Feedback from the user on the completion                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                      |

### Response

**[models.DeploymentCreateMetricResponseBody](../../models/deploymentcreatemetricresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |