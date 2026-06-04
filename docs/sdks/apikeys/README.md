# ApiKeys

## Overview

### Available Operations

* [list](#list) - List API keys
* [create](#create) - Create a new API key
* [list_capabilities](#list_capabilities) - List capability catalog
* [get](#get) - Retrieve an API key
* [delete](#delete) - Delete an API key
* [update](#update) - Update an API key

## list

Returns API keys visible to the current workspace, ordered by creation time with the newest key first. The `api_key` and `token_hash` fields are never returned by this endpoint; only `token_prefix` is included.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyList" method="get" path="/v2/api-keys" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `limit`                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Page size, 1–200. Unset uses the server default (25).                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Cursor for forward pagination. Set to the `api_key_id` of the last<br/> item from the previous page.                                                                                                                                                                                 |
| `ending_before`                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Cursor for backward pagination. Set to the `api_key_id` of the<br/> first item from the previous page.                                                                                                                                                                               |
| `project_id`                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Optional filter: only return keys belonging to this project. When<br/> omitted, returns workspace-scoped and any single-project keys.                                                                                                                                                |
| `status`                                                                                                                                                                                                                                                                             | [Optional[models.APIKeyStatus]](../../models/apikeystatus.md)                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Optional filter: only return keys with this status.                                                                                                                                                                                                                                  |
| `search`                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Optional case-insensitive substring match against the api-key<br/> name. Empty means no name filter.                                                                                                                                                                                 |
| `owner_type`                                                                                                                                                                                                                                                                         | List[[models.OwnerType](../../models/ownertype.md)]                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Optional filter: only return keys whose `owner.kind` matches<br/> one of the requested types. Combines the user / service-account<br/> oneof cases into a single repeated enum so the wire stays flat<br/> and multi-select filters travel as a single field. Empty means<br/> no owner-type filter. |
| `permission_mode`                                                                                                                                                                                                                                                                    | List[[models.PermissionMode](../../models/permissionmode.md)]                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Optional filter: only return keys whose permission mode is one<br/> of the listed presets. Empty means no permission-mode filter.                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                  |

### Response

**[models.ListAPIKeysResponse](../../models/listapikeysresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Mints a new opaque API key (`sk-orq-<key_id>-<secret>`) in the workspace. The raw secret is returned ONCE in the response and is never retrievable afterwards. The stored record retains only `token_prefix` and a SHA-256 `token_hash`.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyCreate" method="post" path="/v2/api-keys" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                    | Human-readable name. Required.                                                                                                                                                                                                                        |
| `owner`                                                                                                                                                                                                                                               | [Optional[models.APIKeyOwner]](../../models/apikeyowner.md)                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                    | Owner attribution. Defaults to service_account when omitted.                                                                                                                                                                                          |
| `project_scope`                                                                                                                                                                                                                                       | [Optional[models.ProjectScope]](../../models/projectscope.md)                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                    | Project authorization scope. Defaults to all-projects when omitted.                                                                                                                                                                                   |
| `permission_mode`                                                                                                                                                                                                                                     | [Optional[models.PermissionMode]](../../models/permissionmode.md)                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                                   |
| `access`                                                                                                                                                                                                                                              | Dict[str, *int*]                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                    | Per-domain access map. Required when `permission_mode` =<br/> `PERMISSION_MODE_RESTRICTED`. See `ApiKey.access` for the full<br/> catalog of valid keys (Domain.id) and AccessLevel string values,<br/> or fetch the live catalog via the `ListCapabilities` RPC. |
| `expires_at`                                                                                                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                    | Optional expiration. When set, the authenticate hot-path rejects<br/> the key once `expires_at` is in the past. Unset means the key<br/> never expires.                                                                                               |
| `retries`                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                   |

### Response

**[models.CreateAPIKeyResponse](../../models/createapikeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_capabilities

Returns the capability catalog: the set of permission domains that can be granted to an API key. Each entry includes the domain id, display name, group, allowed project scopes, and the read / write verb sets resolved at authorize() time. Drives the permissions UI in the dashboard.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyListCapabilities" method="get" path="/v2/api-keys/capabilities" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.list_capabilities()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListCapabilitiesResponse](../../models/listcapabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the metadata for an existing API key by its unique identifier. The raw secret is never returned — only `token_prefix`, `permission_mode`, `project_scope`, and lifecycle fields.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyGet" method="get" path="/v2/api-keys/{api_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.get(api_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | API key id to retrieve (e.g. `01H...`).                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAPIKeyResponse](../../models/getapikeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes an API key. Cache entries in `API_KEYS_KV` are invalidated immediately so an in-flight token cannot ride out the TTL. The response body is empty on success.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyDelete" method="delete" path="/v2/api-keys/{api_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.delete(api_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | API key id to delete.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAPIKeyResponse](../../models/deleteapikeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates mutable fields of an API key: display name, status (active / disabled / revoked), permission mode and access map, project scope, and constraints (budget / rate limit / expiry). Omitted fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyUpdate" method="patch" path="/v2/api-keys/{api_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.update(api_key_id_param="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key_id_param`                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                | API key id to update.                                                                                                                                                                                                                                                                             |
| `api_key_id`                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | API key id to update.                                                                                                                                                                                                                                                                             |
| `name`                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | New name. Omit to keep current.                                                                                                                                                                                                                                                                   |
| `status`                                                                                                                                                                                                                                                                                          | [Optional[models.APIKeyStatus]](../../models/apikeystatus.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                               |
| `permission_mode`                                                                                                                                                                                                                                                                                 | [Optional[models.PermissionMode]](../../models/permissionmode.md)                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                               |
| `access`                                                                                                                                                                                                                                                                                          | Dict[str, *int*]                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | Replacement access map. Required when changing to<br/> `PERMISSION_MODE_RESTRICTED`; ignored otherwise. Provide an empty<br/> map to clear. See `ApiKey.access` for the full catalog of valid<br/> keys (Domain.id) and AccessLevel string values, or fetch the<br/> live catalog via the `ListCapabilities` RPC. |
| `project_scope`                                                                                                                                                                                                                                                                                   | [Optional[models.ProjectScope]](../../models/projectscope.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | New project scope. Omit to keep current.                                                                                                                                                                                                                                                          |
| `expires_at`                                                                                                                                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | New expiration. Omit to keep current. Set `clear_expires_at = true`<br/> to remove an existing expiration (a zero Timestamp here would still<br/> mean "no change" because of optional semantics).                                                                                                |
| `clear_expires_at`                                                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | Force-clear the expiration. Mutually exclusive with `expires_at`.                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                               |

### Response

**[models.UpdateAPIKeyResponse](../../models/updateapikeyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |