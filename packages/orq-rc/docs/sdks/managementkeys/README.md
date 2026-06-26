# ManagementKeys

## Overview

### Available Operations

* [list](#list) - List management keys
* [create](#create) - Create a new management key
* [list_capabilities](#list_capabilities) - List management capability catalog
* [get](#get) - Retrieve a management key
* [delete](#delete) - Delete a management key
* [update](#update) - Update a management key

## list

Returns management keys in the current workspace, ordered by creation time with the newest key first. The `api_key` and `token_hash` fields are never returned by this endpoint; only `token_prefix` is included.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyList" method="get" path="/v2/management-keys" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                       | *Optional[int]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Page size, 1–200. Unset uses the server default (25).                                                                         |
| `starting_after`                                                                                                              | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Cursor for forward pagination. Set to the `management_key_id` of the<br/> last item from the previous page.                   |
| `ending_before`                                                                                                               | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Cursor for backward pagination. Set to the `management_key_id` of the<br/> first item from the previous page.                 |
| `status`                                                                                                                      | [Optional[models.ManagementKeyStatus]](../../models/managementkeystatus.md)                                                   | :heavy_minus_sign:                                                                                                            | Optional filter: only return keys with this status.                                                                           |
| `search`                                                                                                                      | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Optional case-insensitive substring match against the management-key<br/> name. Empty means no name filter.                   |
| `permission_mode`                                                                                                             | List[[models.ManagementPermissionMode](../../models/managementpermissionmode.md)]                                             | :heavy_minus_sign:                                                                                                            | Optional filter: only return keys whose permission mode is one of<br/> the listed presets. Empty means no permission-mode filter. |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.ListManagementKeysResponse](../../models/listmanagementkeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Mints a new opaque management key (`sk-orq-<key_id>-<secret>`) in the workspace. The raw secret is returned ONCE in the response and is never retrievable afterwards. The stored record retains only `token_prefix` and a SHA-256 `token_hash`.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyCreate" method="post" path="/v2/management-keys" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.create(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                       | Human-readable name. Required.                                                                                                                                                                                                                                           |
| `permission_mode`                                                                                                                                                                                                                                                        | [Optional[models.ManagementPermissionMode]](../../models/managementpermissionmode.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                      |
| `access`                                                                                                                                                                                                                                                                 | Dict[str, *int*]                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Per-domain access map. Required when `permission_mode` =<br/> `MANAGEMENT_PERMISSION_MODE_RESTRICTED`. See `ManagementKey.access`<br/> for the catalog of valid keys (Domain.id) and AccessLevel string<br/> values, or fetch the live catalog via the capability catalog<br/> endpoint. |
| `expires_at`                                                                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Optional expiration. When set, the authenticate hot-path rejects<br/> the key once `expires_at` is in the past. Unset means the key<br/> never expires.                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                      |

### Response

**[models.CreateManagementKeyResponse](../../models/createmanagementkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_capabilities

Returns the management capability catalog: the set of workspace-admin permission domains that can be granted to a management key. Each entry includes the domain id, display name, group, and the read / write verb support. Drives the permissions UI in the dashboard.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyListCapabilities" method="get" path="/v2/management-keys/capabilities" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.list_capabilities()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListManagementCapabilitiesResponse](../../models/listmanagementcapabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the metadata for an existing management key by its unique identifier. The raw secret is never returned — only `token_prefix`, `permission_mode`, and lifecycle fields.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyGet" method="get" path="/v2/management-keys/{management_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.get(management_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `management_key_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | Management key id to retrieve (e.g. `01H...`).                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetManagementKeyResponse](../../models/getmanagementkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes a management key. Cache entries are invalidated immediately so an in-flight token cannot ride out the TTL. The response body is empty on success.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyDelete" method="delete" path="/v2/management-keys/{management_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.delete(management_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `management_key_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | Management key id to delete.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteManagementKeyResponse](../../models/deletemanagementkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates mutable fields of a management key: display name, status (active / disabled / revoked), permission mode and access map, and expiry. Omitted fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="ManagementKeyUpdate" method="patch" path="/v2/management-keys/{management_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.management_keys.update(management_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `management_key_id`                                                                                                                            | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | Management key id to update.                                                                                                                   |
| `name`                                                                                                                                         | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | New name. Omit to keep current.                                                                                                                |
| `status`                                                                                                                                       | [Optional[models.ManagementKeyStatus]](../../models/managementkeystatus.md)                                                                    | :heavy_minus_sign:                                                                                                                             | N/A                                                                                                                                            |
| `permission_mode`                                                                                                                              | [Optional[models.ManagementPermissionMode]](../../models/managementpermissionmode.md)                                                          | :heavy_minus_sign:                                                                                                                             | N/A                                                                                                                                            |
| `access`                                                                                                                                       | Dict[str, *int*]                                                                                                                               | :heavy_minus_sign:                                                                                                                             | Replacement access map. Required when changing to<br/> `MANAGEMENT_PERMISSION_MODE_RESTRICTED`; ignored otherwise. Provide<br/> an empty map to clear. |
| `expires_at`                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                           | :heavy_minus_sign:                                                                                                                             | New expiration. Omit to keep current. Set `clear_expires_at = true`<br/> to remove an existing expiration.                                     |
| `clear_expires_at`                                                                                                                             | *Optional[bool]*                                                                                                                               | :heavy_minus_sign:                                                                                                                             | Force-clear the expiration. Mutually exclusive with `expires_at`.                                                                              |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[models.UpdateManagementKeyResponse](../../models/updatemanagementkeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |