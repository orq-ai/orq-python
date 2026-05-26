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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filter_by_tags`                                                    | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_metrics`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListIdentitiesResponse](../../models/listidentitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

    res = orq.identities.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `external_id`                                                                                   | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `display_name`                                                                                  | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `email`                                                                                         | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `avatar_url`                                                                                    | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `tags`                                                                                          | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `metadata`                                                                                      | [Optional[models.CreateIdentityRequestMetadata]](../../models/createidentityrequestmetadata.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CreateIdentityResponse](../../models/createidentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `include_metrics`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveIdentityResponse](../../models/retrieveidentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteIdentityResponse](../../models/deleteidentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

    res = orq.identities.update(id_param="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `id_param`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `id`                                                                                            | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `display_name`                                                                                  | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `email`                                                                                         | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `avatar_url`                                                                                    | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `tags`                                                                                          | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `metadata`                                                                                      | [Optional[models.UpdateIdentityRequestMetadata]](../../models/updateidentityrequestmetadata.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.UpdateIdentityResponse](../../models/updateidentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |