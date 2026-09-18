# Router.Classify

## Overview

### Available Operations

* [create](#create) - Classify

## create

**Beta.** Runs typed classification questions (`noul`, `choice`, `score`) against a classify model such as `typesafe/jev-latest`. The request and response proxy the TypeSafe classification contract 1:1; `model` in the response is the orq model id that served the request and `usage` carries the computed cost like the Responses API. This endpoint currently does not apply PII plugins or guardrails.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="support_ticket" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="typesafe/jev-latest", questions={
        "is_complaint": {
            "instructions": "Is the customer complaining?",
            "type": "noul",
        },
        "severity": {
            "criteria": [
                "Minor",
                "Moderate",
                "Severe",
            ],
            "instructions": "How severe is the issue?",
            "type": "score",
        },
        "topic": {
            "criteria": {
                "delivery": "Shipping or delivery issues",
                "other": "<value>",
                "product": "Product quality",
            },
            "instructions": "What is the message mainly about?",
            "type": "choice",
        },
    }, state="The parcel arrived two days late and the box was crushed.")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `model`                                                                                            | *str*                                                                                              | :heavy_check_mark:                                                                                 | ID of the classify model to use, for example typesafe/jev-latest.                                  |
| `questions`                                                                                        | Dict[str, [models.Questions](../../models/questions.md)]                                           | :heavy_check_mark:                                                                                 | Typed questions keyed by an identifier of your choice. Each answer is returned under the same key. |
| `state`                                                                                            | [models.State](../../models/state.md)                                                              | :heavy_check_mark:                                                                                 | The content to evaluate. A string, an object or an array.                                          |
| `identity`                                                                                         | [Optional[models.ResponseIdentity]](../../models/responseidentity.md)                              | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `metadata`                                                                                         | Dict[str, *str*]                                                                                   | :heavy_minus_sign:                                                                                 | Key-value metadata attached to the trace.                                                          |
| `name`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The name to display on the trace. If not specified, the default system name will be used.          |
| `retry`                                                                                            | [Optional[models.ClassifyRetryConfig]](../../models/classifyretryconfig.md)                        | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.CreateClassifyResponseBody](../../models/createclassifyresponsebody.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.CreateClassifyRouterClassifyResponseBody            | 400                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponseResponseBody    | 422                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse429ResponseBody | 429                                                        | application/json                                           |
| models.APIDefaultError                                     | 4XX, 5XX                                                   | \*/\*                                                      |