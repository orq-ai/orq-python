# SmartRouters

## Overview

### Available Operations

* [list](#list) - List Smart Routers
* [create](#create) - Create a Smart Router
* [get](#get) - Retrieve a Smart Router
* [delete](#delete) - Delete a Smart Router
* [update](#update) - Update a Smart Router

## list

Lists Smart Routers in the current workspace, ordered newest first. Use cursor pagination and optional key, profile, or enabled-state filters to narrow the results.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterList" method="get" path="/v2/smart-routers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `starting_after`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `ending_before`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `search`                                                              | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `profile`                                                             | List[[models.SmartRouterProfile](../../models/smartrouterprofile.md)] | :heavy_minus_sign:                                                    | N/A                                                                   |
| `enabled`                                                             | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListSmartRoutersResponse](../../models/listsmartroutersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a Smart Router in the current workspace from 2 to 50 distinct eligible models. The key must be unique in the workspace and becomes part of the model reference used in AI Gateway requests.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterCreate" method="post" path="/v2/smart-routers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.create(key="<key>", models=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], profile="SMART_ROUTER_PROFILE_QUALITY")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `key`                                                                                              | *str*                                                                                              | :heavy_check_mark:                                                                                 | Unique key for the Smart Router within the workspace. Use lowercase letters, numbers, and hyphens. |
| `models`                                                                                           | List[*str*]                                                                                        | :heavy_check_mark:                                                                                 | Pool of 2 to 50 distinct eligible models. Each value uses `provider/model` format.                 |
| `profile`                                                                                          | [models.SmartRouterProfile](../../models/smartrouterprofile.md)                                    | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.CreateSmartRouterResponse](../../models/createsmartrouterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a Smart Router by ID from the current workspace, including its model reference, model pool, routing profile, and enabled state.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterGet" method="get" path="/v2/smart-routers/{smart_router_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.get(smart_router_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `smart_router_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSmartRouterResponse](../../models/getsmartrouterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a Smart Router and removes its AI Gateway model configuration. A Smart Router referenced by an experiment cannot be deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterDelete" method="delete" path="/v2/smart-routers/{smart_router_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.delete(smart_router_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `smart_router_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteSmartRouterResponse](../../models/deletesmartrouterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates the model pool, routing profile, or both. Omitted fields retain their current values. The router key and model reference cannot be changed.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterUpdate" method="patch" path="/v2/smart-routers/{smart_router_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.update(smart_router_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `smart_router_id`                                                                                                             | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `models`                                                                                                                      | List[*str*]                                                                                                                   | :heavy_minus_sign:                                                                                                            | Replacement pool of 2 to 50 distinct eligible models. Each value uses `provider/model` format. Omit to keep the current pool. |
| `profile`                                                                                                                     | [Optional[models.SmartRouterProfile]](../../models/smartrouterprofile.md)                                                     | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.UpdateSmartRouterResponse](../../models/updatesmartrouterresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |