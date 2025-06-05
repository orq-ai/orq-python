# Evals
(*evals*)

## Overview

### Available Operations

* [all](#all) - Get all Evaluators
* [create](#create) - Create an Evaluator
* [update](#update) - Update an Evaluator
* [delete](#delete) - Delete an Evaluator
* [bert_score](#bert_score) - Run BertScore Evaluator
* [bleu_score](#bleu_score) - Run BLEU Score Evaluator
* [contains_all](#contains_all) - Run Contains All Evaluator
* [contains_any](#contains_any) - Run Contains Any Evaluator
* [contains_email](#contains_email) - Run Contains Email Evaluator
* [contains_none](#contains_none) - Run Contains None Evaluator
* [contains_url](#contains_url) - Run Contains URL Evaluator
* [contains_valid_link](#contains_valid_link) - Run Contains Valid Link Evaluator
* [contains](#contains) - Run Contains Evaluator
* [ends_with](#ends_with) - Run Ends With Evaluator
* [exact_match](#exact_match) - Run Exact Match Evaluator
* [length_between](#length_between) - Run Length Between Evaluator
* [length_greater_than](#length_greater_than) - Run Length Greater Than Evaluator
* [length_less_than](#length_less_than) - Run Length Less Than Evaluator
* [valid_json](#valid_json) - Run JSON Validation Evaluator
* [age_appropriate](#age_appropriate) - Run Age Appropriate Evaluator
* [bot_detection](#bot_detection) - Run Bot Detection Evaluator
* [fact_checking_knowledge_base](#fact_checking_knowledge_base) - Run Fact Checking Knowledge Base Evaluator
* [grammar](#grammar) - Run Grammar Evaluator
* [localization](#localization) - Run Localization Evaluator
* [pii](#pii) - Run PII Evaluator
* [sentiment_classification](#sentiment_classification) - Run Sentiment Classification Evaluator
* [summarization](#summarization) - Run Summarization Evaluator
* [tone_of_voice](#tone_of_voice) - Run Tone of Voice Evaluator
* [translation](#translation) - Run Translation Evaluator
* [ragas_coherence](#ragas_coherence) - Run Coherence Evaluator
* [ragas_conciseness](#ragas_conciseness) - Run Conciseness Evaluator
* [ragas_context_precision](#ragas_context_precision) - Run Context Precision Evaluator
* [ragas_correctness](#ragas_correctness) - Run Correctness Evaluator
* [ragas_faithfulness](#ragas_faithfulness) - Run Faithfulness Evaluator
* [ragas_harmfulness](#ragas_harmfulness) - Run Harmfulness Evaluator
* [ragas_maliciousness](#ragas_maliciousness) - Run Maliciousness Evaluator
* [ragas_response_relevancy](#ragas_response_relevancy) - Run Response Relevancy Evaluator
* [ragas_summarization](#ragas_summarization) - Run Summarization Evaluator
* [invoke](#invoke) - Invoke a Custom Evaluator

## all

Get all Evaluators

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.all(limit=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetEvalsResponseBody](../../models/getevalsresponsebody.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.GetEvalsEvalsResponseBody | 404                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## create

Create an Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.create(request={
        "type": "http_eval",
        "url": "https://total-unit.name",
        "method": "GET",
        "headers": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "payload": {
            "key": "<value>",
        },
        "path": "Default",
        "description": "",
        "key": "<key>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateEvalRequestBody](../../models/createevalrequestbody.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateEvalResponseBody](../../models/createevalresponsebody.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.CreateEvalEvalsResponseBody | 404                                | application/json                   |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |

## update

Update an Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.update(id="<id>", request_body={
        "type": "llm_eval",
        "path": "Default",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `request_body`                                                                  | [Optional[models.UpdateEvalRequestBody]](../../models/updateevalrequestbody.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UpdateEvalResponseBody](../../models/updateevalresponsebody.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.UpdateEvalEvalsResponseBody | 404                                | application/json                   |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |

## delete

Delete an Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.evals.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.DeleteEvalResponseBody | 404                           | application/json              |
| models.APIError               | 4XX, 5XX                      | \*/\*                         |

## bert_score

Run BertScore Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.bert_score()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.EvalsBertScoreRequestBody](../../models/evalsbertscorerequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.EvalsBertScoreResponseBody](../../models/evalsbertscoreresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EvalsBertScoreEvalsResponseBody         | 404                                            | application/json                               |
| models.EvalsBertScoreEvalsResponseResponseBody | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## bleu_score

Run BLEU Score Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.bleu_score()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.EvalsBleuScoreRequestBody](../../models/evalsbleuscorerequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.EvalsBleuScoreResponseBody](../../models/evalsbleuscoreresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EvalsBleuScoreEvalsResponseBody         | 404                                            | application/json                               |
| models.EvalsBleuScoreEvalsResponseResponseBody | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## contains_all

Run Contains All Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_all()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.EvalsContainsAllRequestBody](../../models/evalscontainsallrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EvalsContainsAllResponseBody](../../models/evalscontainsallresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EvalsContainsAllEvalsResponseBody         | 404                                              | application/json                                 |
| models.EvalsContainsAllEvalsResponseResponseBody | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## contains_any

Run Contains Any Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_any()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.EvalsContainsAnyRequestBody](../../models/evalscontainsanyrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EvalsContainsAnyResponseBody](../../models/evalscontainsanyresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EvalsContainsAnyEvalsResponseBody         | 404                                              | application/json                                 |
| models.EvalsContainsAnyEvalsResponseResponseBody | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## contains_email

Run Contains Email Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_email()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.EvalsContainsEmailRequestBody](../../models/evalscontainsemailrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EvalsContainsEmailResponseBody](../../models/evalscontainsemailresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EvalsContainsEmailEvalsResponseBody         | 404                                                | application/json                                   |
| models.EvalsContainsEmailEvalsResponseResponseBody | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## contains_none

Run Contains None Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_none()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.EvalsContainsNoneRequestBody](../../models/evalscontainsnonerequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EvalsContainsNoneResponseBody](../../models/evalscontainsnoneresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EvalsContainsNoneEvalsResponseBody         | 404                                               | application/json                                  |
| models.EvalsContainsNoneEvalsResponseResponseBody | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## contains_url

Run Contains URL Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_url()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.EvalsContainsURLRequestBody](../../models/evalscontainsurlrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EvalsContainsURLResponseBody](../../models/evalscontainsurlresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EvalsContainsURLEvalsResponseBody         | 404                                              | application/json                                 |
| models.EvalsContainsURLEvalsResponseResponseBody | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## contains_valid_link

Run Contains Valid Link Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains_valid_link()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.EvalsContainsValidLinkRequestBody](../../models/evalscontainsvalidlinkrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.EvalsContainsValidLinkResponseBody](../../models/evalscontainsvalidlinkresponsebody.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.EvalsContainsValidLinkEvalsResponseBody         | 404                                                    | application/json                                       |
| models.EvalsContainsValidLinkEvalsResponseResponseBody | 500                                                    | application/json                                       |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## contains

Run Contains Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.contains()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.EvalsContainsRequestBody](../../models/evalscontainsrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.EvalsContainsResponseBody](../../models/evalscontainsresponsebody.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.EvalsContainsEvalsResponseBody         | 404                                           | application/json                              |
| models.EvalsContainsEvalsResponseResponseBody | 500                                           | application/json                              |
| models.APIError                               | 4XX, 5XX                                      | \*/\*                                         |

## ends_with

Run Ends With Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ends_with()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.EvalsEndsWithRequestBody](../../models/evalsendswithrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.EvalsEndsWithResponseBody](../../models/evalsendswithresponsebody.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.EvalsEndsWithEvalsResponseBody         | 404                                           | application/json                              |
| models.EvalsEndsWithEvalsResponseResponseBody | 500                                           | application/json                              |
| models.APIError                               | 4XX, 5XX                                      | \*/\*                                         |

## exact_match

Run Exact Match Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.exact_match()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.EvalsExactMatchRequestBody](../../models/evalsexactmatchrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.EvalsExactMatchResponseBody](../../models/evalsexactmatchresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.EvalsExactMatchEvalsResponseBody         | 404                                             | application/json                                |
| models.EvalsExactMatchEvalsResponseResponseBody | 500                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## length_between

Run Length Between Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.length_between()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.EvalsLengthBetweenRequestBody](../../models/evalslengthbetweenrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EvalsLengthBetweenResponseBody](../../models/evalslengthbetweenresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EvalsLengthBetweenEvalsResponseBody         | 404                                                | application/json                                   |
| models.EvalsLengthBetweenEvalsResponseResponseBody | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## length_greater_than

Run Length Greater Than Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.length_greater_than()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.EvalsLengthGreaterThanRequestBody](../../models/evalslengthgreaterthanrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.EvalsLengthGreaterThanResponseBody](../../models/evalslengthgreaterthanresponsebody.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.EvalsLengthGreaterThanEvalsResponseBody         | 404                                                    | application/json                                       |
| models.EvalsLengthGreaterThanEvalsResponseResponseBody | 500                                                    | application/json                                       |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## length_less_than

Run Length Less Than Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.length_less_than()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.EvalsLengthLessThanRequestBody](../../models/evalslengthlessthanrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.EvalsLengthLessThanResponseBody](../../models/evalslengthlessthanresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.EvalsLengthLessThanEvalsResponseBody         | 404                                                 | application/json                                    |
| models.EvalsLengthLessThanEvalsResponseResponseBody | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## valid_json

Run JSON Validation Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.valid_json()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.EvalsValidJSONRequestBody](../../models/evalsvalidjsonrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.EvalsValidJSONResponseBody](../../models/evalsvalidjsonresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.EvalsValidJSONEvalsResponseBody         | 404                                            | application/json                               |
| models.EvalsValidJSONEvalsResponseResponseBody | 500                                            | application/json                               |
| models.APIError                                | 4XX, 5XX                                       | \*/\*                                          |

## age_appropriate

Run Age Appropriate Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.age_appropriate()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.EvalsAgeAppropriateRequestBody](../../models/evalsageappropriaterequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.EvalsAgeAppropriateResponseBody](../../models/evalsageappropriateresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.EvalsAgeAppropriateEvalsResponseBody         | 404                                                 | application/json                                    |
| models.EvalsAgeAppropriateEvalsResponseResponseBody | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## bot_detection

Run Bot Detection Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.bot_detection()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.EvalsBotDetectionRequestBody](../../models/evalsbotdetectionrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EvalsBotDetectionResponseBody](../../models/evalsbotdetectionresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EvalsBotDetectionEvalsResponseBody         | 404                                               | application/json                                  |
| models.EvalsBotDetectionEvalsResponseResponseBody | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## fact_checking_knowledge_base

Run Fact Checking Knowledge Base Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.fact_checking_knowledge_base()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.EvalsFactCheckingKnowledgeBaseRequestBody](../../models/evalsfactcheckingknowledgebaserequestbody.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.EvalsFactCheckingKnowledgeBaseResponseBody](../../models/evalsfactcheckingknowledgebaseresponsebody.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| models.EvalsFactCheckingKnowledgeBaseEvalsResponseBody         | 404                                                            | application/json                                               |
| models.EvalsFactCheckingKnowledgeBaseEvalsResponseResponseBody | 500                                                            | application/json                                               |
| models.APIError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

## grammar

Run Grammar Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.grammar()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.EvalsGrammarRequestBody](../../models/evalsgrammarrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.EvalsGrammarResponseBody](../../models/evalsgrammarresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.EvalsGrammarEvalsResponseBody         | 404                                          | application/json                             |
| models.EvalsGrammarEvalsResponseResponseBody | 500                                          | application/json                             |
| models.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## localization

Run Localization Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.localization()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.EvalsLocalizationRequestBody](../../models/evalslocalizationrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EvalsLocalizationResponseBody](../../models/evalslocalizationresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.EvalsLocalizationEvalsResponseBody         | 404                                               | application/json                                  |
| models.EvalsLocalizationEvalsResponseResponseBody | 500                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## pii

Run PII Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.pii()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EvalsPiiRequestBody](../../models/evalspiirequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EvalsPiiResponseBody](../../models/evalspiiresponsebody.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.EvalsPiiEvalsResponseBody         | 404                                      | application/json                         |
| models.EvalsPiiEvalsResponseResponseBody | 500                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## sentiment_classification

Run Sentiment Classification Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.sentiment_classification()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                 | [models.EvalsSentimentClassificationRequestBody](../../models/evalssentimentclassificationrequestbody.md) | :heavy_check_mark:                                                                                        | The request object to use for the request.                                                                |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.EvalsSentimentClassificationResponseBody](../../models/evalssentimentclassificationresponsebody.md)**

### Errors

| Error Type                                                   | Status Code                                                  | Content Type                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| models.EvalsSentimentClassificationEvalsResponseBody         | 404                                                          | application/json                                             |
| models.EvalsSentimentClassificationEvalsResponseResponseBody | 500                                                          | application/json                                             |
| models.APIError                                              | 4XX, 5XX                                                     | \*/\*                                                        |

## summarization

Run Summarization Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.summarization()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.EvalsSummarizationRequestBody](../../models/evalssummarizationrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EvalsSummarizationResponseBody](../../models/evalssummarizationresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EvalsSummarizationEvalsResponseBody         | 404                                                | application/json                                   |
| models.EvalsSummarizationEvalsResponseResponseBody | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## tone_of_voice

Run Tone of Voice Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.tone_of_voice()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.EvalsToneOfVoiceRequestBody](../../models/evalstoneofvoicerequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EvalsToneOfVoiceResponseBody](../../models/evalstoneofvoiceresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EvalsToneOfVoiceEvalsResponseBody         | 404                                              | application/json                                 |
| models.EvalsToneOfVoiceEvalsResponseResponseBody | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## translation

Run Translation Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.translation()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.EvalsTranslationRequestBody](../../models/evalstranslationrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.EvalsTranslationResponseBody](../../models/evalstranslationresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EvalsTranslationEvalsResponseBody         | 404                                              | application/json                                 |
| models.EvalsTranslationEvalsResponseResponseBody | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## ragas_coherence

Run Coherence Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_coherence()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.EvalsRagasCoherenceRequestBody](../../models/evalsragascoherencerequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.EvalsRagasCoherenceResponseBody](../../models/evalsragascoherenceresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.EvalsRagasCoherenceEvalsResponseBody         | 404                                                 | application/json                                    |
| models.EvalsRagasCoherenceEvalsResponseResponseBody | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## ragas_conciseness

Run Conciseness Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_conciseness()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.EvalsRagasConcisenessRequestBody](../../models/evalsragasconcisenessrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.EvalsRagasConcisenessResponseBody](../../models/evalsragasconcisenessresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EvalsRagasConcisenessEvalsResponseBody         | 404                                                   | application/json                                      |
| models.EvalsRagasConcisenessEvalsResponseResponseBody | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## ragas_context_precision

Run Context Precision Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_context_precision()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.EvalsRagasContextPrecisionRequestBody](../../models/evalsragascontextprecisionrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.EvalsRagasContextPrecisionResponseBody](../../models/evalsragascontextprecisionresponsebody.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.EvalsRagasContextPrecisionEvalsResponseBody         | 404                                                        | application/json                                           |
| models.EvalsRagasContextPrecisionEvalsResponseResponseBody | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## ragas_correctness

Run Correctness Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_correctness()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.EvalsRagasCorrectnessRequestBody](../../models/evalsragascorrectnessrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.EvalsRagasCorrectnessResponseBody](../../models/evalsragascorrectnessresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EvalsRagasCorrectnessEvalsResponseBody         | 404                                                   | application/json                                      |
| models.EvalsRagasCorrectnessEvalsResponseResponseBody | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## ragas_faithfulness

Run Faithfulness Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_faithfulness()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.EvalsRagasFaithfulnessRequestBody](../../models/evalsragasfaithfulnessrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.EvalsRagasFaithfulnessResponseBody](../../models/evalsragasfaithfulnessresponsebody.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| models.EvalsRagasFaithfulnessEvalsResponseBody         | 404                                                    | application/json                                       |
| models.EvalsRagasFaithfulnessEvalsResponseResponseBody | 500                                                    | application/json                                       |
| models.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## ragas_harmfulness

Run Harmfulness Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_harmfulness()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.EvalsRagasHarmfulnessRequestBody](../../models/evalsragasharmfulnessrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.EvalsRagasHarmfulnessResponseBody](../../models/evalsragasharmfulnessresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.EvalsRagasHarmfulnessEvalsResponseBody         | 404                                                   | application/json                                      |
| models.EvalsRagasHarmfulnessEvalsResponseResponseBody | 500                                                   | application/json                                      |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## ragas_maliciousness

Run Maliciousness Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_maliciousness()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.EvalsRagasMaliciousnessRequestBody](../../models/evalsragasmaliciousnessrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.EvalsRagasMaliciousnessResponseBody](../../models/evalsragasmaliciousnessresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.EvalsRagasMaliciousnessEvalsResponseBody         | 404                                                     | application/json                                        |
| models.EvalsRagasMaliciousnessEvalsResponseResponseBody | 500                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## ragas_response_relevancy

Run Response Relevancy Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_response_relevancy()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.EvalsRagasResponseRelevancyRequestBody](../../models/evalsragasresponserelevancyrequestbody.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.EvalsRagasResponseRelevancyResponseBody](../../models/evalsragasresponserelevancyresponsebody.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.EvalsRagasResponseRelevancyEvalsResponseBody         | 404                                                         | application/json                                            |
| models.EvalsRagasResponseRelevancyEvalsResponseResponseBody | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## ragas_summarization

Run Summarization Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.ragas_summarization()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.EvalsRagasSummarizationRequestBody](../../models/evalsragassummarizationrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.EvalsRagasSummarizationResponseBody](../../models/evalsragassummarizationresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.EvalsRagasSummarizationEvalsResponseBody         | 404                                                     | application/json                                        |
| models.EvalsRagasSummarizationEvalsResponseResponseBody | 500                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## invoke

Invoke a Custom Evaluator

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.invoke(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | Evaluator ID                                                            |
| `input`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Latest user message                                                     |
| `output`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The generated response from the model                                   |
| `reference`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The reference used to compare the output                                |
| `retrievals`                                                            | List[*str*]                                                             | :heavy_minus_sign:                                                      | Knowledge base retrievals                                               |
| `messages`                                                              | List[[models.InvokeEvalMessages](../../models/invokeevalmessages.md)]   | :heavy_minus_sign:                                                      | The messages used to generate the output, without the last user message |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.InvokeEvalResponseBody](../../models/invokeevalresponsebody.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.InvokeEvalEvalsResponseBody         | 404                                        | application/json                           |
| models.InvokeEvalEvalsResponseResponseBody | 500                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |