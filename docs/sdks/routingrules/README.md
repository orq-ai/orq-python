# RoutingRules

## Overview

### Available Operations

* [list](#list) - List routing rules
* [create](#create) - Create a routing rule
* [list_used_models](#list_used_models) - List models used by routing rules
* [retrieve](#retrieve) - Retrieve a routing rule
* [delete](#delete) - Delete a routing rule
* [update](#update) - Update a routing rule

## list

Returns routing rules ordered by ascending priority. Supports cursor pagination, search, status, project, and referenced-model filters.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleList" method="get" path="/v2/routing-rules" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.routing_rules.list(limit=10)

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
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListRoutingRulesResponse](../../models/listroutingrulesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a routing rule with metadata and optional model, plugin, priority, and matching configuration. Rules default to disabled when `enabled` is omitted.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleCreate" method="post" path="/v2/routing-rules" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.routing_rules.create(display_name="Freeda_Beahan")

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
| `expression`                                                                        | [Optional[models.RoutingRuleExpression]](../../models/routingruleexpression.md)     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `models_config`                                                                     | [Optional[models.RoutingRuleModelsConfig]](../../models/routingrulemodelsconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `plugins`                                                                           | List[[models.RoutingRulePlugin](../../models/routingruleplugin.md)]                 | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `priority`                                                                          | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `cache_config`                                                                      | [Optional[models.RoutingRuleCacheConfig]](../../models/routingrulecacheconfig.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.RoutingRule](../../models/routingrule.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_used_models

Returns the distinct model references used by routing rules in the requested scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleListUsedModels" method="get" path="/v2/routing-rules/used-models" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.routing_rules.list_used_models()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListRoutingRuleUsedModelsResponse](../../models/listroutingruleusedmodelsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves a routing rule by its unique identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleGet" method="get" path="/v2/routing-rules/{routing_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.routing_rules.retrieve(routing_rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `routing_rule_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoutingRule](../../models/routingrule.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a routing rule.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleDelete" method="delete" path="/v2/routing-rules/{routing_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.routing_rules.delete(routing_rule_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `routing_rule_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates routing-rule metadata or configuration. Project scope is immutable.

### Example Usage

<!-- UsageSnippet language="python" operationID="RoutingRuleUpdate" method="patch" path="/v2/routing-rules/{routing_rule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.routing_rules.update(routing_rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `routing_rule_id`                                                                   | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `display_name`                                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `enabled`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `expression`                                                                        | [Optional[models.RoutingRuleExpression]](../../models/routingruleexpression.md)     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `models_config`                                                                     | [Optional[models.RoutingRuleModelsConfig]](../../models/routingrulemodelsconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `plugins`                                                                           | List[[models.RoutingRulePlugin](../../models/routingruleplugin.md)]                 | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `priority`                                                                          | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `cache_config`                                                                      | [Optional[models.RoutingRuleCacheConfig]](../../models/routingrulecacheconfig.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.RoutingRule](../../models/routingrule.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |