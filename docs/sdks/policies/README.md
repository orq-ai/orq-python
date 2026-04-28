# Policies

## Overview

### Available Operations

* [list](#list) - List policies
* [create](#create) - Create policy
* [delete](#delete) - Delete policy
* [retrieve](#retrieve) - Get policy
* [update](#update) - Update policy

## list

Returns a paginated list of policies for the current project.

### Example Usage

<!-- UsageSnippet language="python" operationID="PolicyList" method="get" path="/v2/policies" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.policies.list(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A cursor for use in pagination.                                     |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A cursor for use in pagination.                                     |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional filter by project ID.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PolicyListResponseBody](../../models/policylistresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new router policy with model configuration, evaluators, retry settings, and limits.

### Example Usage

<!-- UsageSnippet language="python" operationID="PolicyCreate" method="post" path="/v2/policies" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.policies.create(display_name="Zelda80")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `display_name`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `description`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `enabled`                                                                    | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `evaluators`                                                                 | List[[models.EvaluatorRef](../../models/evaluatorref.md)]                    | :heavy_minus_sign:                                                           | N/A                                                                          |
| `limits`                                                                     | [Optional[models.Limits]](../../models/limits.md)                            | :heavy_minus_sign:                                                           | N/A                                                                          |
| `models_config`                                                              | [Optional[models.ModelsConfig]](../../models/modelsconfig.md)                | :heavy_minus_sign:                                                           | N/A                                                                          |
| `project_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Optional project ID. If null/omitted, the entity is global (workspace-wide). |
| `retry_config`                                                               | [Optional[models.PolicyRetryConfig]](../../models/policyretryconfig.md)      | :heavy_minus_sign:                                                           | N/A                                                                          |
| `timeout`                                                                    | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.PolicyCreateResponseBody](../../models/policycreateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing policy by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="PolicyDelete" method="delete" path="/v2/policies/{policy_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.policies.delete(policy_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the policy                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves the details of an existing policy by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="PolicyGet" method="get" path="/v2/policies/{policy_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.policies.retrieve(policy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the policy                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PolicyGetResponseBody](../../models/policygetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Partially updates an existing policy. Only provided fields are updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="PolicyUpdate" method="patch" path="/v2/policies/{policy_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.policies.update(policy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `policy_id`                                                             | *str*                                                                   | :heavy_check_mark:                                                      | The ID of the policy                                                    |
| `description`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `display_name`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `enabled`                                                               | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | N/A                                                                     |
| `evaluators`                                                            | List[[models.EvaluatorRef](../../models/evaluatorref.md)]               | :heavy_minus_sign:                                                      | N/A                                                                     |
| `limits`                                                                | [Optional[models.Limits]](../../models/limits.md)                       | :heavy_minus_sign:                                                      | N/A                                                                     |
| `models_config`                                                         | [Optional[models.ModelsConfig]](../../models/modelsconfig.md)           | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retry_config`                                                          | [Optional[models.PolicyRetryConfig]](../../models/policyretryconfig.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `timeout`                                                               | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PolicyUpdateResponseBody](../../models/policyupdateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |