# Workspaces

## Overview

### Available Operations

* [list](#list) - List workspaces
* [get](#get) - Retrieve a workspace
* [update](#update) - Update a workspace

## list

Returns workspaces the caller can access. A user session lists every membership. A management key lists only the workspace bound to the key. Project keys are rejected.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceList" method="get" path="/v2/workspaces" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspaces.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListWorkspacesResponse](../../models/listworkspacesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a workspace by its key. A user session must be a member and does not need a workspace-scoped token. A management key may only retrieve the workspace bound to the key.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceGet" method="get" path="/v2/workspaces/{key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspaces.get(key="<key>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWorkspaceResponse](../../models/getworkspaceresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates a workspace. Omit a field to leave it unchanged. Set `archived` to true to archive, false to restore. The workspace key cannot be changed.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceUpdate" method="patch" path="/v2/workspaces/{key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspaces.update(key="<key>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `key`                                                                                             | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `display_name`                                                                                    | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `logo_url`                                                                                        | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `archived`                                                                                        | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `settings`                                                                                        | [Optional[models.WorkspaceSettingsFields]](../../models/workspacesettingsfields.md)               | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `metadata`                                                                                        | [Optional[models.UpdateWorkspaceRequestMetadata]](../../models/updateworkspacerequestmetadata.md) | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `enforce_enabled_models`                                                                          | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.UpdateWorkspaceResponse](../../models/updateworkspaceresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |