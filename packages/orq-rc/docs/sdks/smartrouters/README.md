# SmartRouters

## Overview

### Available Operations

* [list](#list) - List Smart Routers
* [create](#create) - Create a Smart Router
* [get](#get) - Retrieve a Smart Router
* [delete](#delete) - Delete a Smart Router
* [update](#update) - Update a Smart Router
* [set_enabled](#set_enabled) - Enable or disable a Smart Router

## list

Returns Smart Routers in the caller's workspace, ordered newest first. Supports cursor pagination, name search, profile filtering, and enabled-state filtering.

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a workspace Smart Router from an ordered pool of autorouter-eligible models. The router key becomes the stable model identifier used by gateway requests.

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

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `key`                                                                    | *str*                                                                    | :heavy_check_mark:                                                       | Required. Stable lowercase key containing letters, numbers, and hyphens. |
| `models`                                                                 | List[*str*]                                                              | :heavy_check_mark:                                                       | Required. Ordered pool of distinct models in provider/model format.      |
| `profile`                                                                | [models.SmartRouterProfile](../../models/smartrouterprofile.md)          | :heavy_check_mark:                                                       | N/A                                                                      |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[models.CreateSmartRouterResponse](../../models/createsmartrouterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves a Smart Router by ID within the caller's workspace.

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes a Smart Router and removes its gateway model configuration.

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Partially updates the routing models or profile. The router key is immutable.

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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `smart_router_id`                                                         | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `models`                                                                  | List[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `profile`                                                                 | [Optional[models.SmartRouterProfile]](../../models/smartrouterprofile.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.UpdateSmartRouterResponse](../../models/updatesmartrouterresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## set_enabled

Controls whether the Smart Router is available to gateway requests in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="SmartRouterSetEnabled" method="post" path="/v2/smart-routers/{smart_router_id}/enabled" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.smart_routers.set_enabled(smart_router_id="<id>", enabled=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `smart_router_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetSmartRouterEnabledResponse](../../models/setsmartrouterenabledresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |