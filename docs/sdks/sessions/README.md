# Sessions
(*sessions*)

## Overview

### Available Operations

* [create](#create) - Create Trace Session
* [delete](#delete) - Delete Trace Session
* [get](#get) - Get Trace Session
* [update](#update) - Update Trace Session
* [list](#list) - List sessions

## create

Create a session for traces

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.create()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateSessionRequestBody](../../models/createsessionrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreateSessionResponseBody](../../models/createsessionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a trace session

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.sessions.delete(session_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the session                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get

Get a trace session

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.get(session_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the session                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSessionResponseBody](../../models/getsessionresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update

Update a trace session

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.update(session_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `session_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | Unique identifier of the session                                              |
| `id`                                                                          | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `external_id`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `duration`                                                                    | *Optional[float]*                                                             | :heavy_minus_sign:                                                            | Duration of the session in ms                                                 |
| `contact_ids`                                                                 | List[*str*]                                                                   | :heavy_minus_sign:                                                            | List of contact ids                                                           |
| `billing`                                                                     | [Optional[models.UpdateSessionBilling]](../../models/updatesessionbilling.md) | :heavy_minus_sign:                                                            | N/A                                                                           |
| `usage`                                                                       | [Optional[models.UpdateSessionUsage]](../../models/updatesessionusage.md)     | :heavy_minus_sign:                                                            | N/A                                                                           |
| `traces_count`                                                                | *Optional[float]*                                                             | :heavy_minus_sign:                                                            | Total traces of the session                                                   |
| `tags`                                                                        | List[*str*]                                                                   | :heavy_minus_sign:                                                            | N/A                                                                           |
| `workspace_id`                                                                | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The workspace id                                                              |
| `project_id`                                                                  | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | The project id                                                                |
| `started_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | The time when the session was created                                         |
| `updated_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | The time when the session was updated                                         |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.UpdateSessionResponseBody](../../models/updatesessionresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## list

Retrieves a paginated list of sessions for the current workspace.

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.list()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ListSessionsRequestBody](../../models/listsessionsrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ListSessionsResponseBody](../../models/listsessionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |