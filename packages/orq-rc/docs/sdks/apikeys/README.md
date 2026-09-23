# ApiKeys

## Overview

### Available Operations

* [list](#list) - List API keys
* [create](#create) - Create a new API key
* [list_capabilities](#list_capabilities) - List capability catalog
* [delete](#delete) - Delete an API key
* [get](#get) - Retrieve an API key
* [update](#update) - Update an API key

## list

Returns API keys visible to the current workspace as a JSON array sorted by name. Raw tokens are never included; the `token` field contains a masked display value.

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

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                       | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Only return keys bound to this project. When omitted, every key visible to the caller is returned. |
| `source`                                                                                           | [Optional[models.QueryParamSource]](../../models/queryparamsource.md)                              | :heavy_minus_sign:                                                                                 | Only return keys of this source.                                                                   |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[List[models.APIKeyRestResponse]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Mints a new API key in the workspace, bound to the single project in `projects` or to every project when omitted. The raw token is returned once in the `token` field and is never retrievable afterwards. Unknown body fields are rejected.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyCreate" method="post" path="/v2/api-keys" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.create(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Display name of the key.                                                                                        |
| `access`                                                                                                        | Dict[str, *str*]                                                                                                | :heavy_minus_sign:                                                                                              | Per-domain access level (none, read or write) for restricted keys; domain ids come from the capability catalog. |
| `constraints`                                                                                                   | [Optional[models.Constraints]](../../models/constraints.md)                                                     | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `expiration`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                            | :heavy_minus_sign:                                                                                              | Legacy expiry as an RFC 3339 timestamp; prefer constraints.expires_at.                                          |
| `owner`                                                                                                         | [Optional[models.Owner]](../../models/owner.md)                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `permission_mode`                                                                                               | [Optional[models.PermissionMode]](../../models/permissionmode.md)                                               | :heavy_minus_sign:                                                                                              | Permission preset; restricted keys hold only the domains granted in access.                                     |
| `project_scope`                                                                                                 | [Optional[models.ProjectScope]](../../models/projectscope.md)                                                   | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `projects`                                                                                                      | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | Legacy single-project binding; prefer project_scope.                                                            |
| `source`                                                                                                        | [Optional[models.APIKeyCreateSource]](../../models/apikeycreatesource.md)                                       | :heavy_minus_sign:                                                                                              | Origin of the key; router keys are minted for the AI router.                                                    |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.APIKeyRestResponse](../../models/apikeyrestresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_capabilities

Returns the capability catalog: the set of permission domains that can be granted to an API key. Each entry includes the domain id, display name, group, allowed project scopes and whether it can be granted read or write access. No credentials are required.

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

**[models.APIKeyListCapabilitiesResponseBody](../../models/apikeylistcapabilitiesresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes an API key. The key is revoked immediately; in-flight requests using it will fail. The response body is empty on success.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyDelete" method="delete" path="/v2/api-keys/{api_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.api_keys.delete(api_key_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the API key.                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves the metadata for an existing API key by its unique identifier. The raw secret is never returned; `token` carries a masked display value.

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
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the API key.                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.APIKeyRestResponse](../../models/apikeyrestresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates mutable fields of an API key: display name, status (active / disabled / revoked), permission mode and access map, project scope and constraints. Omitted fields keep their current values. Unknown body fields are rejected.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiKeyUpdate" method="patch" path="/v2/api-keys/{api_key_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.api_keys.update(api_key_id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `api_key_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | Unique identifier of the API key.                                                         |
| `access`                                                                                  | Dict[str, *str*]                                                                          | :heavy_minus_sign:                                                                        | Per-domain access level (none, read or write) for restricted keys.                        |
| `active`                                                                                  | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | Legacy toggle mirrored onto status: false disables, true re-enables.                      |
| `constraints`                                                                             | [Optional[models.Constraints]](../../models/constraints.md)                               | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `name`                                                                                    | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | New display name.                                                                         |
| `permission_mode`                                                                         | [Optional[models.APIKeyUpdatePermissionMode]](../../models/apikeyupdatepermissionmode.md) | :heavy_minus_sign:                                                                        | Permission preset; a restricted key must keep at least one granted domain.                |
| `project_scope`                                                                           | [Optional[models.ProjectScope]](../../models/projectscope.md)                             | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `status`                                                                                  | [Optional[models.APIKeyUpdateStatus]](../../models/apikeyupdatestatus.md)                 | :heavy_minus_sign:                                                                        | Lifecycle status; revoked is terminal.                                                    |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.APIKeyRestResponse](../../models/apikeyrestresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |