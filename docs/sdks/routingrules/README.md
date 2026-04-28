# RoutingRules

## Overview

### Available Operations

* [list](#list) - List routing rules
* [create](#create) - Create routing rule
* [delete](#delete) - Delete routing rule
* [retrieve](#retrieve) - Get routing rule
* [update](#update) - Update routing rule

## list

Returns a paginated list of routing rules for the current project, ordered by priority ascending.

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
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A cursor for use in pagination.                                     |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A cursor for use in pagination.                                     |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional filter by project ID.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoutingRuleListResponseBody](../../models/routingrulelistresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new routing rule with expression, models configuration, and priority settings.

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

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `display_name`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `description`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `enabled`                                                                    | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `expression`                                                                 | [Optional[models.ExpressionInput]](../../models/expressioninput.md)          | :heavy_minus_sign:                                                           | N/A                                                                          |
| `models_config`                                                              | [Optional[models.ModelsConfig]](../../models/modelsconfig.md)                | :heavy_minus_sign:                                                           | N/A                                                                          |
| `priority`                                                                   | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `project_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Optional project ID. If null/omitted, the entity is global (workspace-wide). |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.RoutingRuleCreateResponseBody](../../models/routingrulecreateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing routing rule by ID.

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
| `routing_rule_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the routing rule                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves the details of an existing routing rule by ID.

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
| `routing_rule_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the routing rule                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoutingRuleGetResponseBody](../../models/routingrulegetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Partially updates an existing routing rule. Only provided fields are updated.

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `routing_rule_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the routing rule                                          |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expression`                                                        | [Optional[models.ExpressionInput]](../../models/expressioninput.md) | :heavy_minus_sign:                                                  | N/A                                                                 |
| `models_config`                                                     | [Optional[models.ModelsConfig]](../../models/modelsconfig.md)       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `priority`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoutingRuleUpdateResponseBody](../../models/routingruleupdateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |