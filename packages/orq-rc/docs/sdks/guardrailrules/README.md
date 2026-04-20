# GuardrailRules

## Overview

### Available Operations

* [list](#list) - List guardrail rules
* [create](#create) - Create guardrail rule
* [delete](#delete) - Delete guardrail rule
* [retrieve](#retrieve) - Get guardrail rule
* [update](#update) - Update guardrail rule

## list

Returns a paginated list of guardrail rules for the current project.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleList" method="get" path="/v2/guardrail-rules" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.list(limit=10)

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

**[models.GuardrailRuleListResponseBody](../../models/guardrailrulelistresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new guardrail rule with expression, guardrails configuration, and timeout settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleCreate" method="post" path="/v2/guardrail-rules" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.create(display_name="Rosemarie_Wisoky")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `display_name`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `enabled`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `expression`                                                                        | [Optional[models.OptionalExpressionInput]](../../models/optionalexpressioninput.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `guardrails`                                                                        | List[[models.GuardrailRef](../../models/guardrailref.md)]                           | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `project_id`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Optional project ID. If null/omitted, the entity is global (workspace-wide).        |
| `timeout`                                                                           | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GuardrailRuleCreateResponseBody](../../models/guardrailrulecreateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing guardrail rule by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleDelete" method="delete" path="/v2/guardrail-rules/{guardrail_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.guardrail_rules.delete(guardrail_rule_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guardrail_rule_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the guardrail rule                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves the details of an existing guardrail rule by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleGet" method="get" path="/v2/guardrail-rules/{guardrail_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.retrieve(guardrail_rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guardrail_rule_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the guardrail rule                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GuardrailRuleGetResponseBody](../../models/guardrailrulegetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Partially updates an existing guardrail rule. Only provided fields are updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleUpdate" method="patch" path="/v2/guardrail-rules/{guardrail_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.update(guardrail_rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `guardrail_rule_id`                                                                 | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the guardrail rule                                                        |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `display_name`                                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `enabled`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `expression`                                                                        | [Optional[models.OptionalExpressionInput]](../../models/optionalexpressioninput.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `guardrails`                                                                        | List[[models.GuardrailRef](../../models/guardrailref.md)]                           | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `timeout`                                                                           | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GuardrailRuleUpdateResponseBody](../../models/guardrailruleupdateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |