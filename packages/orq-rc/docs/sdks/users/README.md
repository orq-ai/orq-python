# Users

## Overview

### Available Operations

* [list](#list) - List workspace users
* [get](#get) - Retrieve a workspace user
* [delete](#delete) - Delete a workspace user
* [update](#update) - Update a workspace user
* [create](#create) - Create or add workspace users

## list

Returns all users in the current workspace, including their team memberships and workspace roles. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="UserList" method="get" path="/v3/users" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.users.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListUsersResponse](../../models/listusersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves one workspace user by workspace-user ID. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="UserGet" method="get" path="/v3/users/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.users.get(user_id="46d1da91-d6b8-4643-b90e-0499b802a82f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `user_id`                                                                         | *str*                                                                             | :heavy_check_mark:                                                                | Workspace-user UUID returned by List workspace users. This is not the account ID. |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GetUserResponse](../../models/getuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Removes a user from the current workspace, refreshes membership state, and revokes API keys owned by that workspace user. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="UserDelete" method="delete" path="/v3/users/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.users.delete(user_id="a1e4d9ad-bb47-4084-a2ef-008e99397b27")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `user_id`                                                                         | *str*                                                                             | :heavy_check_mark:                                                                | Workspace-user UUID returned by List workspace users. This is not the account ID. |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.DeleteUserResponse](../../models/deleteuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates a user's last-activity timestamp and/or workspace role. Omitted fields remain unchanged. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="UserUpdate" method="patch" path="/v3/users/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.users.update(user_id="ecfae87a-aa48-43a0-be97-757addd58c16")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `user_id`                                                                         | *str*                                                                             | :heavy_check_mark:                                                                | Workspace-user UUID returned by List workspace users. This is not the account ID. |
| `last_activity`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)              | :heavy_minus_sign:                                                                | N/A                                                                               |
| `role`                                                                            | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | One effective workspace role. Omit to preserve the existing role.                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.UpdateUserResponse](../../models/updateuserresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates accounts when necessary, adds each user to the current workspace and specified team, assigns the workspace role, and sends the welcome email for newly created accounts. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="UserCreate" method="post" path="/v3/users/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.users.create(team_id="5bd4792a-28bd-4190-a240-0333fc47343d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `team_id`                                                                                                                         | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | Destination team UUID for every created or added workspace user.                                                                  |
| `emails`                                                                                                                          | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `roles`                                                                                                                           | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | One effective workspace role is required. The first entry is retained for<br/> wire compatibility with the legacy invitation payload. |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.CreateUsersResponse](../../models/createusersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |