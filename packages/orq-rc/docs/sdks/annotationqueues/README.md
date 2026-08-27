# AnnotationQueues

## Overview

### Available Operations

* [list](#list) - List annotation queues
* [create](#create) - Create an annotation queue
* [retrieve](#retrieve) - Retrieve an annotation queue
* [delete](#delete) - Delete an annotation queue
* [update](#update) - Update an annotation queue
* [clear](#clear) - Clear an annotation queue
* [list_items](#list_items) - Query items from an annotation queue
* [add_items](#add_items) - Add items to an annotation queue
* [remove_items](#remove_items) - Remove items from an annotation queue
* [retrieve_item](#retrieve_item) - Retrieve an annotation queue item

## list

Returns annotation queues in the workspace, newest first.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListAnnotationQueues" method="get" path="/v2/annotation-queues" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.list(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `limit`                                                                                        | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | Optional. Number of annotation queues to return. Defaults to 10 and must be between 1 and 200. |
| `starting_after`                                                                               | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for forward pagination. Set to the `_id` of the last item from the previous page.       |
| `ending_before`                                                                                | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Cursor for backward pagination. Set to the `_id` of the first item from the previous page.     |
| `search`                                                                                       | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Optional. Case-insensitive substring match on the annotation queue display name.               |
| `updated_by`                                                                                   | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Optional. Comma-separated account IDs; returns queues last updated by any of them.             |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.ListAnnotationQueuesResponse](../../models/listannotationqueuesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates an annotation queue in a project.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAnnotationQueue" method="post" path="/v2/annotation-queues" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.create(display_name="Vernice_Fadel", description="categorise egg foolishly", project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Required. The display name of the annotation queue.                 |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Required. The description of the annotation queue.                  |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Required. The project to link this annotation queue to.             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnnotationQueue](../../models/annotationqueue.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves an existing annotation queue by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveAnnotationQueue" method="get" path="/v2/annotation-queues/{annotation_queue_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.retrieve(annotation_queue_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `annotation_queue_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnnotationQueue](../../models/annotationqueue.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes an annotation queue, its items, and the queue references stored on the annotated spans.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAnnotationQueue" method="delete" path="/v2/annotation-queues/{annotation_queue_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.delete(annotation_queue_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `annotation_queue_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAnnotationQueueResponse](../../models/deleteannotationqueueresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates an existing annotation queue. Setting `project_id` clears the legacy `human_review_ids` selection.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAnnotationQueue" method="patch" path="/v2/annotation-queues/{annotation_queue_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.update(annotation_queue_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `annotation_queue_id`                                                                         | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `display_name`                                                                                | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Optional. New display name.                                                                   |
| `description`                                                                                 | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Optional. New description.                                                                    |
| `project_id`                                                                                  | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | Optional. New project. Setting this clears the legacy `human_review_ids` selection.           |
| `human_review_ids`                                                                            | List[*str*]                                                                                   | :heavy_minus_sign:                                                                            | Legacy: update manually selected human review IDs. Only applied when `project_id` is not set. |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AnnotationQueue](../../models/annotationqueue.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## clear

Removes every item from the annotation queue without deleting the queue itself.

### Example Usage

<!-- UsageSnippet language="python" operationID="ClearAnnotationQueue" method="delete" path="/v2/annotation-queues/{annotation_queue_id}/clear" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.clear(annotation_queue_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `annotation_queue_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClearAnnotationQueueResponse](../../models/clearannotationqueueresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_items

Queries items from the specified annotation queue. Items whose span no longer exists are skipped.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListAnnotationQueueItems" method="get" path="/v2/annotation-queues/{annotation_queue_id}/items" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.list_items(annotation_queue_id="<id>", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `annotation_queue_id`                                                                      | *str*                                                                                      | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `limit`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Optional. Number of items to return. Defaults to 10 and must be between 1 and 200.         |
| `starting_after`                                                                           | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for forward pagination. Set to the `_id` of the last item from the previous page.   |
| `ending_before`                                                                            | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for backward pagination. Set to the `_id` of the first item from the previous page. |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[models.ListAnnotationQueueItemsResponse](../../models/listannotationqueueitemsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## add_items

Adds spans to the annotation queue. Spans already present are skipped; the response contains only the newly created items.

### Example Usage

<!-- UsageSnippet language="python" operationID="AddAnnotationQueueItems" method="post" path="/v2/annotation-queues/{annotation_queue_id}/items" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.add_items(annotation_queue_id="<id>", items=[
        {
            "span_id": "<id>",
            "trace_id": "<id>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `annotation_queue_id`                                                         | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `items`                                                                       | List[[models.AnnotationQueueItemRef](../../models/annotationqueueitemref.md)] | :heavy_check_mark:                                                            | The spans to add to the annotation queue.                                     |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AddAnnotationQueueItemsResponse](../../models/addannotationqueueitemsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## remove_items

Removes the referenced spans from the annotation queue.

### Example Usage

<!-- UsageSnippet language="python" operationID="RemoveAnnotationQueueItems" method="post" path="/v2/annotation-queues/{annotation_queue_id}/items/remove" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.remove_items(annotation_queue_id="<id>", span_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `annotation_queue_id`                                                        | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `span_ids`                                                                   | List[*str*]                                                                  | :heavy_check_mark:                                                           | The unique identifiers of the spans to be removed from the annotation queue. |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.RemoveAnnotationQueueItemsResponse](../../models/removeannotationqueueitemsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve_item

Retrieves an item from the specified annotation queue in its expanded form. An annotation queue item is a pointer to a span; this endpoint returns the fully resolved span the item references.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveAnnotationQueueItem" method="get" path="/v2/annotation-queues/{annotation_queue_id}/items/{item_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.annotation_queues.retrieve_item(annotation_queue_id="<id>", item_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `annotation_queue_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `item_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveAnnotationQueueItemResponseBody](../../models/retrieveannotationqueueitemresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |