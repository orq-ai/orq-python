# Identities

## Overview

### Available Operations

* [list](#list) - List identities
* [create](#create) - Create an identity
* [retrieve](#retrieve) - Retrieve an identity
* [delete](#delete) - Delete an identity
* [update](#update) - Update an identity

## list

Retrieves a paginated list of identities in your workspace. Use pagination parameters to navigate through large identity lists efficiently.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListIdentities" method="get" path="/v2/identities" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.identities.list(limit=10, search="john", include_metrics=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | N/A                                                                                                                                                                              |
| `starting_after`                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | Cursor for forward pagination. Set to the `_id` of the last item from<br/> the previous page.                                                                                    |
| `ending_before`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | Cursor for backward pagination. Set to the `_id` of the first item from<br/> the previous page.                                                                                  |
| `search`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | Case-insensitive search text matched against identity profile fields.                                                                                                            |
| `filter_by_tags`                                                                                                                                                                 | List[*str*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                               | Return only identities that have at least one of these tags.                                                                                                                     |
| `include_metrics`                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Include aggregate usage metrics on each returned identity.                                                                                                                       |
| `sort_by`                                                                                                                                                                        | [Optional[models.IdentitySortField]](../../models/identitysortfield.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                                               | Field used to order the list.                                                                                                                                                    |
| `include_budget`                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | When true, embed each identity's identity-scoped budget (config and<br/> limits only, no live usage) on the returned records. Adds one budget<br/> lookup for the page; omit to skip it. |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.ListIdentitiesResponse](../../models/listidentitiesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a new identity with a unique external_id. If an identity with the same external_id already exists, the operation will fail.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateIdentity" method="post" path="/v2/identities" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.identities.create(external_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_id`                                                                                | *str*                                                                                        | :heavy_check_mark:                                                                           | Customer-provided stable identifier for this identity. Must be unique<br/> within the workspace. |
| `display_name`                                                                               | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Human-readable display name for the identity.                                                |
| `email`                                                                                      | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Email address associated with the identity.                                                  |
| `avatar_url`                                                                                 | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | URL of the identity avatar image.                                                            |
| `tags`                                                                                       | List[*str*]                                                                                  | :heavy_minus_sign:                                                                           | Free-form labels used to organize and filter identities.                                     |
| `metadata`                                                                                   | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | Custom JSON metadata stored with the identity.                                               |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[models.CreateIdentityResponse](../../models/createidentityresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves detailed information about a specific identity using their identity ID or external ID from your system.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveIdentity" method="get" path="/v2/identities/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.identities.retrieve(id="<id>", include_metrics=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | Identity ID to retrieve.                                                                                     |
| `include_metrics`                                                                                            | *Optional[bool]*                                                                                             | :heavy_minus_sign:                                                                                           | Include aggregate usage metrics on the returned identity.                                                    |
| `include_budget`                                                                                             | *Optional[bool]*                                                                                             | :heavy_minus_sign:                                                                                           | When true, embed the identity-scoped budget (config and limits only,<br/> no live usage) on the returned record. |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[models.RetrieveIdentityResponse](../../models/retrieveidentityresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes an identity from your workspace and cleans up associated budget configurations.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteIdentity" method="delete" path="/v2/identities/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.identities.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Identity ID to delete.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteIdentityResponse](../../models/deleteidentityresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates specific fields of an existing identity. Only the fields provided in the request body will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateIdentity" method="patch" path="/v2/identities/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.identities.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Identity ID to update.                                              |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New display name. Omit to keep the current display name.            |
| `email`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New email address. Omit to keep the current email.                  |
| `avatar_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New avatar image URL. Omit to keep the current avatar URL.          |
| `tags`                                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | Replacement tag list. Leave empty to clear tags.                    |
| `metadata`                                                          | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | Replacement custom JSON metadata.                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateIdentityResponse](../../models/updateidentityresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |