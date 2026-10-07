# ~~Router.Classify~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

### Available Operations

* [~~create~~](#create) - Classify :warning: **Deprecated**

## ~~create~~

**Deprecated.** Use `POST /v3/router/decisions` and `orq.router.decisions.create()` for new integrations. This endpoint remains available for backward compatibility with the same request and response contract.

**Beta.** Runs typed classification questions (`noul`, `choice`, `score`) against a native classify provider, including OpenAI Decisions with `openai/gpt-6-luna`, or a chat model that supports classify emulation. Emulated models answer through one structured-output call and their probabilities are model-reported rather than calibrated. Native providers can return `refusal` for individual questions; refused answers contain only `type`. The request and response follow the TypeSafe classification contract; `model` in the response identifies the primary or fallback model that answered and `usage` carries the computed cost like the Responses API. Both `/v3/router/classify` and `/v3/router/decisions` use this contract, including ordered `fallbacks`, request-level `retry`, and `identity` attribution. Both require `classify.execute`. This endpoint currently does not apply PII plugins or guardrails.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage: fallback_retry_identity

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="fallback_retry_identity" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="openai/gpt-6-luna", questions={
        "positive": {
            "criteria": {
                "false": "The customer is unhappy.",
                "true": "The customer is happy.",
            },
            "instructions": "Is the sentiment positive?",
            "type": "noul",
        },
        "rating": {
            "criteria": [
                "Negative",
                "Neutral",
                "Positive",
            ],
            "instructions": "Rate sentiment.",
            "type": "score",
        },
        "sentiment": {
            "criteria": {
                "negative": "Negative sentiment",
                "neutral": "<value>",
                "positive": "Positive sentiment",
            },
            "instructions": "Classify sentiment.",
            "type": "choice",
        },
    }, state="The customer says: I love this product. It is wonderful!", fallbacks=[
        {
            "model": "openai/gpt-5.6-luna",
        },
    ], identity={
        "display_name": "Sample customer",
        "id": "customer-demo",
    }, retry={
        "count": 2,
        "on_codes": [
            429,
            502,
            503,
            504,
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: openai_answers

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="openai_answers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="LeBaron", questions={

    }, state={

    })

    # Handle response
    print(res)

```
### Example Usage: openai_inline_image

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="openai_inline_image" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="openai/gpt-6-luna", questions={
        "contains_text": {
            "instructions": "Does the image contain text?",
            "type": "noul",
        },
    }, state={
        "0": {
            "content": [
                {
                    "text": "Evaluate this image.",
                    "type": "input_text",
                },
                {
                    "image_url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACLSURBVHgBdY8NDYAgEIXBBEQgAhG0gRGMYBNtoA2M4EygDYygDfCxvdMbk7d9A453f8ZQMcYAWuBVzIHujeGyxE8nYz7dJWYl01p749zxDKABEzhYfDNaMPZSAUymJLZLuvSsSVUhx4G7VM2xpSzQ5YYhLUHDCGoad47ixXjxY84qi1a9QPgZpdYLPVkbtsfywz3jAAAAAElFTkSuQmCC",
                    "type": "input_image",
                },
            ],
            "role": "user",
        },
    })

    # Handle response
    print(res)

```
### Example Usage: openai_text

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="openai_text" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="openai/gpt-6-luna", questions={
        "positive": {
            "criteria": {
                "false": "The customer is unhappy.",
                "true": "The customer is happy.",
            },
            "instructions": "Is the sentiment positive?",
            "type": "noul",
        },
        "rating": {
            "criteria": [
                "Negative",
                "Neutral",
                "Positive",
            ],
            "instructions": "Rate sentiment.",
            "type": "score",
        },
        "sentiment": {
            "criteria": {
                "negative": "Negative sentiment",
                "neutral": "<value>",
                "positive": "Positive sentiment",
            },
            "instructions": "Classify sentiment.",
            "type": "choice",
        },
    }, state="The customer says: I love this product. It is wonderful!")

    # Handle response
    print(res)

```
### Example Usage: partial_refusal

<!-- UsageSnippet language="python" operationID="CreateClassify" method="post" path="/v3/router/classify" example="partial_refusal" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.classify.create(model="LeBaron", questions={

    }, state={

    })

    # Handle response
    print(res)

```
### Example Usage: support_ticket

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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                         | ID of a model that supports native or emulated classify, including openai/gpt-6-luna.                                                                                                                                                                                                                                                                                                                                                      |
| `questions`                                                                                                                                                                                                                                                                                                                                                                                                                                | Dict[str, [models.Questions](../../models/questions.md)]                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                         | Typed questions keyed by an identifier of your choice. Each answer is returned under the same key.                                                                                                                                                                                                                                                                                                                                         |
| `state`                                                                                                                                                                                                                                                                                                                                                                                                                                    | [models.State](../../models/state.md)                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                         | The content to evaluate. A string, an object or an array. For OpenAI GPT-6 Luna, strings are passed as text and objects or ordinary JSON arrays are serialized as text. User-message arrays accept string content or input_text/input_image parts. Images must be inline base64 data URLs, with at most 128 images across the request. Remote image URLs, file IDs, audio, non-user roles, bare content parts and tool items are rejected. |
| `fallbacks`                                                                                                                                                                                                                                                                                                                                                                                                                                | List[[models.FallbackConfig](../../models/fallbackconfig.md)]                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | Up to 10 fallback models in order. The gateway retries a model for matching error codes before trying the next model. Every model must support classification and satisfy access checks. Image requests require native OpenAI image-capable fallbacks.                                                                                                                                                                                     |
| `identity`                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.ResponseIdentity]](../../models/responseidentity.md)                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                 | Dict[str, *str*]                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | Key-value metadata attached to the trace.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `name`                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | The name to display on the trace. If not specified, the default system name will be used.                                                                                                                                                                                                                                                                                                                                                  |
| `retry`                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[models.ClassifyRetryConfig]](../../models/classifyretryconfig.md)                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.CreateClassifyResponseBody](../../models/createclassifyresponsebody.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.CreateClassifyRouterClassifyResponseBody            | 400                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponseResponseBody    | 401                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse403ResponseBody | 403                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse422ResponseBody | 422                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse429ResponseBody | 429                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse500ResponseBody | 500                                                        | application/json                                           |
| models.CreateClassifyRouterClassifyResponse502ResponseBody | 502                                                        | application/json                                           |
| models.APIDefaultError                                     | 4XX, 5XX                                                   | \*/\*                                                      |