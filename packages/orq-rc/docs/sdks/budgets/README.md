# Budgets

## Overview

### Available Operations

* [list](#list) - List budgets
* [create](#create) - Create a new budget
* [check](#check) - Check budget enforcement
* [get](#get) - Retrieve a budget
* [delete](#delete) - Delete a budget
* [update](#update) - Update a budget
* [get_consumption](#get_consumption) - Get current-period consumption
* [reset_consumption](#reset_consumption) - Reset budget consumption

## list

Returns budgets visible to the current workspace, ordered by creation time with the newest first. Supports filtering by scope kind, scope target id, period, and active state, plus an optional free-text query that searches across denormalized target names via Typesense.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetList" method="get" path="/v2/budgets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Page size, 1–200. Unset uses the server default (25).                                                                                                                                        |
| `starting_after`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Cursor for forward pagination. Set to the `budget_id` of the last<br/> item from the previous page.                                                                                          |
| `ending_before`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Cursor for backward pagination. Set to the `budget_id` of the<br/> first item from the previous page.                                                                                        |
| `scope_kind`                                                                                                                                                                                 | List[[models.BudgetScopeKind](../../models/budgetscopekind.md)]                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Optional filter: only return budgets whose scope kind matches one<br/> of the listed values. Empty means no scope-kind filter.                                                               |
| `scope_target_id`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Optional filter: only return budgets whose scope target id matches.                                                                                                                          |
| `is_active`                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Optional filter: only return budgets with this active state.                                                                                                                                 |
| `period`                                                                                                                                                                                     | List[[models.BudgetPeriod](../../models/budgetperiod.md)]                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                           | Optional filter: only return budgets whose limits.period matches<br/> one of the listed values. Empty means no period filter.                                                                |
| `query`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | Optional free-text query. Server translates this into a Typesense<br/> search over the denormalized `scope_target_name` and id fields on<br/> the per-workspace `{workspace_id}_budgets` collection. |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |

### Response

**[models.ListBudgetsResponse](../../models/listbudgetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new budget in the workspace. Exactly one scope variant must be set (workspace / project / identity / api_key / provider / model). At least one of `limits.amount`, `limits.token_limit`, or `rate_limit.requests_per_minute` MUST be provided. Uniqueness is enforced across (workspace_id, scope_kind, scope_target_id).

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetCreate" method="post" path="/v2/budgets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`                                                                                                                                                                                                                                                    | [Optional[models.BudgetScope]](../../models/budgetscope.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                         | Structured scope. Mutually exclusive with `match`: provide a scope<br/> for the six canonical kinds (the server derives the matching CEL),<br/> or provide `match` for a dynamic budget. Exactly one of the two<br/> must be set; the handler enforces that invariant. |
| `match`                                                                                                                                                                                                                                                    | [Optional[models.BudgetMatch]](../../models/budgetmatch.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                         | Raw CEL matching expression for dynamic budgets (e.g.<br/> `metadata.team == "ml" && provider == "openai"`). Validated via<br/> CEL parse at write time. Mutually exclusive with `scope`.                                                                  |
| `limits`                                                                                                                                                                                                                                                   | [Optional[models.BudgetLimits]](../../models/budgetlimits.md)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                         | At least one of amount / token_limit / rate_limit.requests_per_minute<br/> must be provided on the budget; the handler enforces that invariant.                                                                                                            |
| `rate_limit`                                                                                                                                                                                                                                               | [Optional[models.RateLimit]](../../models/ratelimit.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                         | Optional rate limit.                                                                                                                                                                                                                                       |
| `is_active`                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                         | Whether the budget should be active immediately. Defaults to true<br/> when omitted (handler enforces).                                                                                                                                                    |
| `expires_at`                                                                                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                         | Optional expiration. When set in combination with is_active=true,<br/> the value MUST be in the future; the handler rejects past values.                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                        |

### Response

**[models.CreateBudgetResponse](../../models/createbudgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## check

Internal endpoint used by the gateway to resolve applicable budgets and check enforcement gates for a request. Returns allowed/rejected status with dimension info for rate-limit headers.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetCheck" method="post" path="/v2/budgets/check" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.check()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                           | Type                                                                                                                                                | Required                                                                                                                                            | Description                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key_id`                                                                                                                                        | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | API key that issued the request (if any).                                                                                                           |
| `project_id`                                                                                                                                        | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Project the request targets (if any).                                                                                                               |
| `identity_external_id`                                                                                                                              | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Identity external id for contact-scoped budgets (if any).                                                                                           |
| `provider`                                                                                                                                          | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Provider enum value for provider-scoped budgets (if any).                                                                                           |
| `model_id`                                                                                                                                          | *Optional[str]*                                                                                                                                     | :heavy_minus_sign:                                                                                                                                  | Full model reference for model-scoped budgets (if any), exactly as<br/> the caller sent it: "provider/model" or "workspaceKey@provider/model".      |
| `metadata`                                                                                                                                          | [Optional[models.Metadata]](../../models/metadata.md)                                                                                               | :heavy_minus_sign:                                                                                                                                  | Request metadata forwarded for dynamic-budget matching<br/> (`metadata.team == "ml"`). Free-form JSON object from the request<br/> body's `metadata` field. |
| `headers`                                                                                                                                           | Dict[str, *str*]                                                                                                                                    | :heavy_minus_sign:                                                                                                                                  | Request headers (lowercase keys) forwarded for dynamic-budget<br/> matching (`headers["x-env"] == "prod"`).                                         |
| `retries`                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                    | :heavy_minus_sign:                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                 |

### Response

**[models.CheckBudgetsResponse](../../models/checkbudgetsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the metadata for an existing budget by its unique identifier. Returns `NotFound` when the budget does not exist in the caller's workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetGet" method="get" path="/v2/budgets/{budget_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.get(budget_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `budget_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Budget id to retrieve.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBudgetResponse](../../models/getbudgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes a budget. Consumption counters in Redis for this budget are cleared immediately. The response body is empty on success.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetDelete" method="delete" path="/v2/budgets/{budget_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.delete(budget_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `budget_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Budget id to delete.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteBudgetResponse](../../models/deletebudgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates mutable fields of a budget: limits, rate limit, activation, and expiration. The scope is immutable — to change a budget's target, delete and recreate it. Omitted fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetUpdate" method="patch" path="/v2/budgets/{budget_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.update(budget_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `budget_id`                                                                                                                                                                             | *str*                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                      | Budget id to update.                                                                                                                                                                    |
| `limits`                                                                                                                                                                                | [Optional[models.BudgetLimits]](../../models/budgetlimits.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                      | New limits. Omit to keep current.                                                                                                                                                       |
| `rate_limit`                                                                                                                                                                            | [Optional[models.RateLimit]](../../models/ratelimit.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | New rate limit. Omit to keep current.                                                                                                                                                   |
| `is_active`                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | New active state. Omit to keep current.                                                                                                                                                 |
| `expires_at`                                                                                                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                      | New expiration. Omit to keep current. Set `clear_expires_at = true`<br/> to remove an existing expiration.                                                                              |
| `clear_expires_at`                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Force-clear the expiration. Mutually exclusive with `expires_at`.                                                                                                                       |
| `match`                                                                                                                                                                                 | [Optional[models.BudgetMatch]](../../models/budgetmatch.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                      | New matching expression. Only valid for dynamic budgets (no<br/> structured scope) — the scope of a scoped budget is immutable, so<br/> its derived expression is too. Validated via CEL parse. |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |

### Response

**[models.UpdateBudgetResponse](../../models/updatebudgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_consumption

Returns the current-period cost, token, and per-minute request counters for the budget. Values reflect the live Redis state for the active period bucket.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetGetConsumption" method="get" path="/v2/budgets/{budget_id}/consumption" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.get_consumption(budget_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `budget_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Budget id whose counters should be returned.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBudgetConsumptionResponse](../../models/getbudgetconsumptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reset_consumption

Clears the current-period cost, token, and request counters for the budget. The budget record itself is preserved; only the Redis counters are reset.

### Example Usage

<!-- UsageSnippet language="python" operationID="BudgetResetConsumption" method="post" path="/v2/budgets/{budget_id}/reset-consumption" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.budgets.reset_consumption(budget_id="<id>", reset_budget_consumption_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `budget_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | Budget id whose current-period counters should be cleared.                            |
| `reset_budget_consumption_request`                                                    | [models.ResetBudgetConsumptionRequest](../../models/resetbudgetconsumptionrequest.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ResetBudgetConsumptionResponse](../../models/resetbudgetconsumptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |