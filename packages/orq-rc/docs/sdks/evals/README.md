# Evals

## Overview

### Available Operations

* [all](#all) - Get all Evaluators
* [create](#create) - Create an Evaluator
* [get](#get) - Retrieve an Evaluator
* [delete](#delete) - Delete an Evaluator
* [update](#update) - Update an Evaluator
* [list_versions](#list_versions) - List evaluator versions
* [get_version](#get_version) - Get evaluator version
* [invoke](#invoke) - Invoke a Custom Evaluator

## all

List all evaluators in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetEvals" method="get" path="/v2/evaluators" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.all(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size, 1-200. Unset uses the server default (10).               |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sort`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListEvaluatorsResponse](../../models/listevaluatorsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Create a new evaluator in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateEval" method="post" path="/v2/evaluators" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.create(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateEvalRequestBody](../../models/createevalrequestbody.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.EvaluatorDocumentResponse](../../models/evaluatordocumentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieve a single evaluator by ID with more detail than the list endpoint: full type-specific config, owner, domain_id, metadata, enabled, and output_type.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetEval" method="get" path="/v2/evaluators/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.get(id="01JMDPA3QW5C1V0NJ1PW34T4E5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EvaluatorDocumentResponse](../../models/evaluatordocumentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Delete an evaluator by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteEval" method="delete" path="/v2/evaluators/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteEvaluatorResponse](../../models/deleteevaluatorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Update an evaluator by ID with the provided fields.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateEval" method="patch" path="/v2/evaluators/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.update(id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `request_body`                                                        | [models.UpdateEvalRequestBody](../../models/updateevalrequestbody.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.EvaluatorDocumentResponse](../../models/evaluatordocumentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_versions

Returns version history for a specific evaluator.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListEvalVersions" method="get" path="/v2/evaluators/{id}/versions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.list_versions(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page size, 1-200. Unset uses the server default (10).               |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListEvaluatorVersionsResponse](../../models/listevaluatorversionsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_version

Returns a specific version of an evaluator.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetEvalVersion" method="get" path="/v2/evaluators/{id}/versions/{version_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.get_version(id="<id>", version_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetEvaluatorVersionResponse](../../models/getevaluatorversionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## invoke

Runs an evaluator that already exists in the workspace. Accepts either a conversation or the structured input and output fields; when both are present the conversation wins.

### Example Usage

<!-- UsageSnippet language="python" operationID="InvokeEval" method="post" path="/v3/evaluators/{id}/invoke" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.evals.invoke(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                       | Accepts a bare id, `id@version`, or `id@environment`.                                                                                                                                                                                    |
| `context`                                                                                                                                                                                                                                | [Optional[models.EvaluationContext]](../../models/evaluationcontext.md)                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                       | The data to grade. When `messages` is present it is the conversation and<br/> `input.user_query` is ignored; `output.response` is appended only when the<br/> conversation carries no assistant turn. Mirrors graders-api buildGraderRequest. |
| `model`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | Model to grade with, as a catalog id such as "openai/gpt-4o".<br/><br/> Only meaningful for a hub template of type llm_eval or ragas, which has no<br/> model of its own. A stored evaluator uses the model on its own definition<br/> and ignores this. |
| `query`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | Latest user message. Folds into `context.input.user_query`.                                                                                                                                                                              |
| `output`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | The generated response from the model. Folds into<br/> `context.output.response`.                                                                                                                                                        |
| `reference`                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                       | The reference used to compare the output. Folds into<br/> `context.input.expected_output`.                                                                                                                                               |
| `retrievals`                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                       | Knowledge base retrievals. Folds into `context.input.retrievals`.                                                                                                                                                                        |
| `messages`                                                                                                                                                                                                                               | List[[models.InvokeEvaluatorRequestMessages](../../models/invokeevaluatorrequestmessages.md)]                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                       | The conversation that produced the output. Folds into<br/> `context.messages`.                                                                                                                                                           |
| `variables`                                                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                       | Template variables for evaluator prompt substitution. Folds into<br/> `context.variables`.                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                      |

### Response

**[models.InvokeEvaluatorResponse](../../models/invokeevaluatorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |