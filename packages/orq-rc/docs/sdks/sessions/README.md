# Sessions

## Overview

### Available Operations

* [create](#create) - Create trace thread
* [get_count](#get_count) - Get thread count
* [list](#list) - List trace threads
* [list_tags](#list_tags) - List thread tags
* [get](#get) - Get trace thread
* [delete](#delete) - Delete trace thread
* [update](#update) - Update trace thread

## create

Create a thread for traces.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateSession" method="post" path="/v2/sessions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.create(external_id="<id>", duration=7329.24, contact_ids=[
        "<value 1>",
        "<value 2>",
    ], billing={
        "input_cost": 5975.95,
        "output_cost": 754.22,
        "total_cost": 2965.14,
    }, usage={
        "prompt_tokens": 424835,
        "completion_tokens": 793505,
        "total_tokens": 726901,
    }, traces_count=451437, tags=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `external_id`                                                        | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `duration`                                                           | *float*                                                              | :heavy_check_mark:                                                   | N/A                                                                  |
| `contact_ids`                                                        | List[*str*]                                                          | :heavy_check_mark:                                                   | N/A                                                                  |
| `billing`                                                            | [models.ThreadBilling](../../models/threadbilling.md)                | :heavy_check_mark:                                                   | N/A                                                                  |
| `usage`                                                              | [models.ThreadUsage](../../models/threadusage.md)                    | :heavy_check_mark:                                                   | N/A                                                                  |
| `traces_count`                                                       | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `tags`                                                               | List[*str*]                                                          | :heavy_check_mark:                                                   | N/A                                                                  |
| `project_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `started_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `client`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `repo`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `kind`                                                               | [Optional[models.ThreadKind]](../../models/threadkind.md)            | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.Thread](../../models/thread.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_count

Get total count of trace threads.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetSessionCount" method="post" path="/v2/sessions/count" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.get_count(filters={
        "interval": "SESSION_INTERVAL_LAST_30_MINUTES",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filters`                                                           | [models.ThreadFilters](../../models/threadfilters.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetThreadCountResponse](../../models/getthreadcountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list

List trace threads from your workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListSessions" method="post" path="/v2/sessions/query" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.list(filters={
        "interval": "SESSION_INTERVAL_LAST_7_DAYS",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filters`                                                           | [models.ThreadFilters](../../models/threadfilters.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListThreadsResponse](../../models/listthreadsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_tags

Retrieves all unique thread tags in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListSessionTags" method="get" path="/v2/sessions/tags" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.list_tags()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[str]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Get a trace thread.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetSession" method="get" path="/v2/sessions/{session_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.get(session_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Thread](../../models/thread.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Delete a trace thread.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteSession" method="delete" path="/v2/sessions/{session_id}" -->
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
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Update a trace thread.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateSession" method="patch" path="/v2/sessions/{session_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.sessions.update(session_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `session_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `external_id`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `duration`                                                           | *Optional[float]*                                                    | :heavy_minus_sign:                                                   | N/A                                                                  |
| `contact_ids`                                                        | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `billing`                                                            | [Optional[models.ThreadBilling]](../../models/threadbilling.md)      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `usage`                                                              | [Optional[models.ThreadUsage]](../../models/threadusage.md)          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `traces_count`                                                       | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `tags`                                                               | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `project_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `started_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `clear_contact_ids`                                                  | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Remove every contact id. Mutually exclusive with contact_ids.        |
| `clear_tags`                                                         | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Remove every tag. Mutually exclusive with tags.                      |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `client`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `repo`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `kind`                                                               | [Optional[models.ThreadKind]](../../models/threadkind.md)            | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.Thread](../../models/thread.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |