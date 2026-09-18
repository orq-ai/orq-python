# GuardrailRules

## Overview

### Available Operations

* [list](#list) - List guardrail rules
* [create](#create) - Create a guardrail rule
* [list_used_guardrails](#list_used_guardrails) - List guardrails used by guardrail rules
* [retrieve](#retrieve) - Retrieve a guardrail rule
* [delete](#delete) - Delete a guardrail rule
* [update](#update) - Update a guardrail rule

## list

Returns guardrail rules with cursor pagination, search, status, project, sort, and referenced-guardrail filters.

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
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `sort_by`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `guardrail_id`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListGuardrailRulesResponse](../../models/listguardrailrulesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a guardrail rule with metadata and optional evaluator, plugin, and matching configuration. Rules default to disabled when `enabled` is omitted.

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
| `project_id`                                                                        | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Optional project scope. Omit for a workspace-wide rule.                             |
| `enabled`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether the rule is active. Defaults to false when omitted.                         |
| `expression`                                                                        | [Optional[models.GuardrailRuleExpression]](../../models/guardrailruleexpression.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `guardrails`                                                                        | List[[models.GuardrailRuleGuardrail](../../models/guardrailruleguardrail.md)]       | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `plugins`                                                                           | List[[models.GuardrailRulePlugin](../../models/guardrailruleplugin.md)]             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreateGuardrailRuleResponse](../../models/createguardrailruleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_used_guardrails

Returns the distinct guardrail identifiers used by guardrail rules in the requested scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleListUsedGuardrails" method="get" path="/v2/guardrail-rules/used-guardrails" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.list_used_guardrails()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListGuardrailRuleUsedGuardrailsResponse](../../models/listguardrailruleusedguardrailsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves a guardrail rule by its unique identifier.

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
| `guardrail_rule_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGuardrailRuleResponse](../../models/getguardrailruleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a guardrail rule.

### Example Usage

<!-- UsageSnippet language="python" operationID="GuardrailRuleDelete" method="delete" path="/v2/guardrail-rules/{guardrail_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.guardrail_rules.delete(guardrail_rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guardrail_rule_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteGuardrailRuleResponse](../../models/deleteguardrailruleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates guardrail-rule metadata or configuration. Project scope is immutable.

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
| `guardrail_rule_id`                                                                 | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `display_name`                                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `enabled`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `expression`                                                                        | [Optional[models.GuardrailRuleExpression]](../../models/guardrailruleexpression.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `guardrails`                                                                        | List[[models.GuardrailRuleGuardrail](../../models/guardrailruleguardrail.md)]       | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `plugins`                                                                           | List[[models.GuardrailRulePlugin](../../models/guardrailruleplugin.md)]             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UpdateGuardrailRuleResponse](../../models/updateguardrailruleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |