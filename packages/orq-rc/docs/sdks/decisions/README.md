# Router.Decisions

## Overview

### Available Operations

* [create](#create) - Decisions

## create

**Beta.** Evaluate content against named questions and receive structured answers, probabilities, and usage costs. Send the content as `state` and define each entry in `questions` as:

- `noul`: estimate the probability that a statement is true.
- `choice`: select an option from a set.
- `score`: rate the content on an ordered scale.
- `box`: locate one target in an image and return its bounding box. Beta, TypeSafe `jev-preview` only.

Instructions and criteria accept strings or structured JSON. TypeSafe models also accept inline images through `assets` (beta).

Use a native decision model or a supported chat model. Configure ordered `fallbacks`, optional `retry`, `timeout.call_timeout` in milliseconds, and an exact-match `cache`. Each retry and fallback gets a fresh timeout; omit `retry` to move directly to the next fallback on timeout. The response identifies the model that answered.

Requires the `classify` API-key permission. PII plugins and guardrails are not applied. See the [Decisions guide](/ai-gateway/features/decisions) for supported models, probability interpretation, and refusals.

### Example Usage: fallback_retry_identity

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="fallback_retry_identity" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="openai/gpt-6-luna", questions={
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
    }, timeout={
        "call_timeout": 2000,
    })

    # Handle response
    print(res)

```
### Example Usage: openai_answers

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="openai_answers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="Impala", questions={
        "key": {
            "instructions": {

            },
            "type": "noul",
        },
    }, state="California")

    # Handle response
    print(res)

```
### Example Usage: openai_inline_image

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="openai_inline_image" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="openai/gpt-6-luna", questions={
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

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="openai_text" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="openai/gpt-6-luna", questions={
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

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="partial_refusal" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="Impala", questions={
        "key": {
            "instructions": {

            },
            "type": "noul",
        },
    }, state="California")

    # Handle response
    print(res)

```
### Example Usage: support_ticket

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="support_ticket" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="typesafe/jev-latest", questions={
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
### Example Usage: typesafe_image_box

<!-- UsageSnippet language="python" operationID="CreateDecisions" method="post" path="/v3/router/decisions" example="typesafe_image_box" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.router.decisions.create(model="typesafe/jev-preview", questions={
        "mug": {
            "instructions": "the coffee mug in `photo`",
            "type": "box",
        },
        "mug_visible": {
            "instructions": "Is there a coffee mug in `photo`?",
            "type": "noul",
        },
    }, state={
        "photo": "kitchen-photo",
    }, assets={
        "kitchen-photo": {
            "data_base64": "<base64 JPEG>",
            "format_": "jpg",
            "type": "image",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ID of a model that supports native or emulated classify, including openai/gpt-6-luna.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `questions`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Dict[str, [models.CreateDecisionsQuestions](../../models/createdecisionsquestions.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Typed questions keyed by an identifier of your choice. Each answer is returned under the same key. Native OpenAI accepts 1 to 400 questions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `state`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [models.CreateDecisionsState](../../models/createdecisionsstate.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The content to evaluate. A string, an object or an array. For TypeSafe models, reference images declared in assets by writing their reference string. Native OpenAI accepts messages and function/custom-tool history. User messages support input_text, input_image and input_json; images can use inline base64 data URLs or public HTTP(S) URLs. At most 128 images across state and question instructions. Shared text/image parts support explicit prompt_cache_breakpoint markers. File IDs, audio, item references and bare content parts are unsupported. Other objects and arrays are serialized as text. |
| `assets`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Dict[str, [models.ClassifyAsset](../../models/classifyasset.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Beta, TypeSafe models only. Inline images keyed by a reference string. Write the reference in state, instructions or criteria wherever the image belongs; every asset must be referenced. Required for box questions.                                                                                                                                                                                                                                                                                                                                                                                              |
| `cache`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.ClassifyCacheConfig]](../../models/classifycacheconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `fallback_on_codes`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | List[*int*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | HTTP status codes that trigger fallback. Defaults to [408,429,500,502,503,504,529]. Each code must be unique and between 400 and 599.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `fallbacks`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | List[[models.FallbackConfig](../../models/fallbackconfig.md)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Up to 10 fallback models in order. The gateway retries a model for matching error codes before trying the next model. Every model must support classification and satisfy access checks. Requests with images in state require native OpenAI image-capable fallbacks; requests with assets or box questions require TypeSafe fallbacks.                                                                                                                                                                                                                                                                            |
| `identity`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.ResponseIdentity]](../../models/responseidentity.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Dict[str, *str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Key-value metadata attached to the trace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The name to display on the trace. If not specified, the default system name will be used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `prompt_cache_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Native OpenAI only. Partitions reuse of shared input across requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `prompt_cache_options`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [Optional[models.ClassifyPromptCacheOptions]](../../models/classifypromptcacheoptions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `retry`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[models.ClassifyRetryConfig]](../../models/classifyretryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `timeout`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[models.ClassifyTimeoutConfig]](../../models/classifytimeoutconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.CreateDecisionsResponseBody](../../models/createdecisionsresponsebody.md)**

### Errors

| Error Type                                                   | Status Code                                                  | Content Type                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| models.CreateDecisionsRouterDecisionsResponseBody            | 400                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponseResponseBody    | 401                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse403ResponseBody | 403                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse408ResponseBody | 408                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse422ResponseBody | 422                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse429ResponseBody | 429                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse500ResponseBody | 500                                                          | application/json                                             |
| models.CreateDecisionsRouterDecisionsResponse502ResponseBody | 502                                                          | application/json                                             |
| models.APIDefaultError                                       | 4XX, 5XX                                                     | \*/\*                                                        |