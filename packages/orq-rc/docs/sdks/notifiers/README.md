# Notifiers

## Overview

### Available Operations

* [list](#list) - List notifiers
* [create](#create) - Create a notifier
* [get](#get) - Retrieve a notifier
* [delete](#delete) - Delete a notifier
* [update](#update) - Update a notifier

## list

Returns notifier destinations visible to the caller, ordered by creation time with the newest notifier first.

### Example Usage

<!-- UsageSnippet language="python" operationID="NotifierList" method="get" path="/v2/notifiers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.notifiers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `limit`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Optional. Number of notifiers to return. Defaults to 25 and must be between 1 and 200.     |
| `starting_after`                                                                           | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for forward pagination. Set to the `_id` of the last item from the previous page.   |
| `ending_before`                                                                            | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for backward pagination. Set to the `_id` of the first item from the previous page. |
| `project_id`                                                                               | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Restrict results to one project. Must be a project the caller is authorized for.           |
| `search`                                                                                   | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Optional. Case-insensitive substring match on the notifier name.                           |
| `type`                                                                                     | List[[models.NotifierType](../../models/notifiertype.md)]                                  | :heavy_minus_sign:                                                                         | Optional. Restrict results to these notifier types.                                        |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[models.ListNotifiersResponse](../../models/listnotifiersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a notifier destination in a project. Choose `NOTIFIER_TYPE_EMAIL`, `NOTIFIER_TYPE_SLACK_WEBHOOK`, or `NOTIFIER_TYPE_WEBHOOK` and provide the matching destination fields.

### Example Usage

<!-- UsageSnippet language="python" operationID="NotifierCreate" method="post" path="/v2/notifiers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.notifiers.create(request={
        "type": "NOTIFIER_TYPE_UNSPECIFIED",
        "incoming_webhook_url": "https://far-wear.org/",
        "display_name": "Dennis48",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateNotifierRequest](../../models/createnotifierrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateNotifierResponse](../../models/createnotifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves an existing notifier by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="NotifierGet" method="get" path="/v2/notifiers/{notifier_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.notifiers.get(notifier_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `notifier_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNotifierResponse](../../models/getnotifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes an existing notifier by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="NotifierDelete" method="delete" path="/v2/notifiers/{notifier_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.notifiers.delete(notifier_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `notifier_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteNotifierResponse](../../models/deletenotifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Partially updates an existing notifier. When changing `type`, provide the destination fields required by the new notifier type.

### Example Usage

<!-- UsageSnippet language="python" operationID="NotifierUpdate" method="patch" path="/v2/notifiers/{notifier_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.notifiers.update(notifier_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                       | Type                                                                                                                                                                                            | Required                                                                                                                                                                                        | Description                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `notifier_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                              | N/A                                                                                                                                                                                             |
| `project_id`                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Optional. New containing project. Workspace-scoped callers may set an empty value to make the notifier workspace-wide. Project-scoped API keys remain pinned to the API key's project.          |
| `display_name`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Optional. New human-readable notifier name.                                                                                                                                                     |
| `metadata`                                                                                                                                                                                      | [Optional[models.UpdateNotifierRequestMetadata]](../../models/updatenotifierrequestmetadata.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Optional. Replacement custom JSON metadata.                                                                                                                                                     |
| `type`                                                                                                                                                                                          | [Optional[models.NotifierType]](../../models/notifiertype.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                              | N/A                                                                                                                                                                                             |
| `emails`                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                              | Optional replacement email recipients. Required when changing `type` to `NOTIFIER_TYPE_EMAIL`.                                                                                                  |
| `incoming_webhook_url`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Optional replacement Slack incoming webhook URL. Required when changing `type` to `NOTIFIER_TYPE_SLACK_WEBHOOK`.                                                                                |
| `webhook_url`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Optional replacement generic webhook URL. Required when changing `type` to `NOTIFIER_TYPE_WEBHOOK`.                                                                                             |
| `headers`                                                                                                                                                                                       | [Optional[models.Headers]](../../models/headers.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                              | Optional replacement generic webhook headers. Secret header values returned by GET or LIST are masked as an empty string; omit those entries or replace them with the real value when updating. |
| `retries`                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                             |

### Response

**[models.UpdateNotifierResponse](../../models/updatenotifierresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |