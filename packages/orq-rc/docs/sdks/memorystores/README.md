# MemoryStores

## Overview

### Available Operations

* [list](#list) - List memory stores
* [create](#create) - Create memory store
* [retrieve](#retrieve) - Retrieve memory store
* [update](#update) - Update memory store
* [delete](#delete) - Delete memory store
* [list_memories](#list_memories) - List all memories
* [create_memory](#create_memory) - Create a new memory
* [retrieve_memory](#retrieve_memory) - Retrieve a specific memory
* [update_memory](#update_memory) - Update a specific memory
* [delete_memory](#delete_memory) - Delete a specific memory
* [list_documents](#list_documents) - List all documents for a memory
* [create_document](#create_document) - Create a new memory document
* [retrieve_document](#retrieve_document) - Retrieve a specific memory document
* [update_document](#update_document) - Update a specific memory document
* [delete_document](#delete_document) - Delete a specific memory document

## list

Retrieves a paginated list of memory stores in the workspace. Use cursor-based pagination parameters to navigate through the results.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAllMemoryStores" method="get" path="/v2/memory-stores" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.list(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetAllMemoryStoresResponseBody](../../models/getallmemorystoresresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## create

Create memory store

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateMemoryStore" method="post" path="/v2/memory-stores" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.create(request={
        "key": "<key>",
        "embedding_config": {
            "model": "cohere/embed-multilingual-light-v3.0",
        },
        "description": "unlike excluding soulful quirkily hmph baseboard whereas gee deserted",
        "path": "Default",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateMemoryStoreRequestBody](../../models/creatememorystorerequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreateMemoryStoreResponseBody](../../models/creatememorystoreresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves detailed information about a specific memory store, including its configuration and metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveMemoryStore" method="get" path="/v2/memory-stores/{memory_store_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.retrieve(memory_store_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveMemoryStoreResponseBody](../../models/retrievememorystoreresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 401, 403, 404       | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update

Update the memory store configuration

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateMemoryStore" method="patch" path="/v2/memory-stores/{memory_store_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.update(memory_store_key="<value>", description="wherever cash since now exempt proliferate aha tabulate ack", path="Default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                                                                                          | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The unique key identifier of the memory store                                                                                                                               |
| `description`                                                                                                                                                               | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The description of the memory store. Be as precise as possible to help the AI to understand the purpose of the memory store.                                                |
| `ttl`                                                                                                                                                                       | *Optional[float]*                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                          | The default time to live of every memory document created within the memory store. Useful to control if the documents in the memory should be store for short or long term. |
| `path`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |

### Response

**[models.UpdateMemoryStoreResponseBody](../../models/updatememorystoreresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently delete a memory store, including memories and documents.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteMemoryStore" method="delete" path="/v2/memory-stores/{memory_store_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.memory_stores.delete(memory_store_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_memories

Retrieves a paginated list of memories for the memory store

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAllMemories" method="get" path="/v2/memory-stores/{memory_store_key}/memories" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.list_memories(memory_store_key="<value>", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique key identifier of the memory store                                                                                                                                                                                                                                                                                           |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `q`                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Search query to filter memories by entity_id                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetAllMemoriesResponseBody](../../models/getallmemoriesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_memory

Creates a new memory in the specified memory store.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateMemory" method="post" path="/v2/memory-stores/{memory_store_key}/memories" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.create_memory(memory_store_key="<value>", entity_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                            | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The unique key identifier of the memory store                                                                 |
| `entity_id`                                                                                                   | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Unique identifier for the entity this memory is associated with (e.g., user ID, session ID, conversation ID). |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CreateMemoryResponseBody](../../models/creatememoryresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_memory

Retrieves details of a specific memory by its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveMemory" method="get" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.retrieve_memory(memory_store_key="<value>", memory_entity_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `memory_entity_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the memory                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveMemoryResponseBody](../../models/retrievememoryresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_memory

Updates the details of a specific memory.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateMemory" method="patch" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.update_memory(memory_store_key="<value>", memory_entity_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `memory_entity_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the memory                                 |
| `metadata`                                                          | Dict[str, *str*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateMemoryResponseBody](../../models/updatememoryresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_memory

Permanently deletes a specific memory.

        Use this endpoint to:
        - Remove a memory from the store
        - Clean up unused memories
        - Manage memory storage space

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteMemory" method="delete" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.memory_stores.delete_memory(memory_store_key="<value>", memory_entity_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `memory_entity_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the memory                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_documents

Retrieves a paginated list of documents associated with a specific memory.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAllMemoryDocuments" method="get" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}/documents" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.list_documents(memory_store_key="<value>", memory_entity_id="<id>", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique key identifier of the memory store                                                                                                                                                                                                                                                                                           |
| `memory_entity_id`                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique identifier of the memory                                                                                                                                                                                                                                                                                                     |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `updated_after`                                                                                                                                                                                                                                                                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter documents updated after this ISO datetime                                                                                                                                                                                                                                                                                        |
| `updated_before`                                                                                                                                                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter documents updated before this ISO datetime                                                                                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetAllMemoryDocumentsResponseBody](../../models/getallmemorydocumentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_document

Creates a new document in the specified memory.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateMemoryDocument" method="post" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}/documents" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.create_document(memory_store_key="<value>", memory_entity_id="<id>", text="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The unique key identifier of the memory store                                                                                                                                                                                                                           |
| `memory_entity_id`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The unique entity_id provided during the memory store creation                                                                                                                                                                                                          |
| `text`                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The content of the memory document (whitespace trimmed).                                                                                                                                                                                                                |
| `metadata`                                                                                                                                                                                                                                                              | Dict[str, *str*]                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Flexible key-value pairs for custom filtering and categorization. Clients can add arbitrary string metadata to enable future filtering of memory documents based on their specific needs (e.g., document type, source, topic, relevance score, or any custom taxonomy). |
| `retries`                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                     |

### Response

**[models.CreateMemoryDocumentResponseBody](../../models/creatememorydocumentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_document

Retrieves details of a specific memory document by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveMemoryDocument" method="get" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}/documents/{document_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.retrieve_document(memory_store_key="<value>", memory_entity_id="<id>", document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `memory_entity_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the memory                                 |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveMemoryDocumentResponseBody](../../models/retrievememorydocumentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_document

Updates the details of a specific memory document.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateMemoryDocument" method="patch" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}/documents/{document_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.memory_stores.update_document(memory_store_key="<value>", memory_entity_id="<id>", document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `memory_store_key`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The unique key identifier of the memory store                                                                                                                                                                                                                           |
| `memory_entity_id`                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The unique identifier of the memory                                                                                                                                                                                                                                     |
| `document_id`                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                      | The unique identifier of the document                                                                                                                                                                                                                                   |
| `text`                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                      | The content of the memory document (whitespace trimmed).                                                                                                                                                                                                                |
| `metadata`                                                                                                                                                                                                                                                              | Dict[str, *str*]                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Flexible key-value pairs for custom filtering and categorization. Clients can add arbitrary string metadata to enable future filtering of memory documents based on their specific needs (e.g., document type, source, topic, relevance score, or any custom taxonomy). |
| `retries`                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                     |

### Response

**[models.UpdateMemoryDocumentResponseBody](../../models/updatememorydocumentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_document

Permanently deletes a specific memory document.

        Use this endpoint to:
        - Remove a document from a memory
        - Clean up unused documents
        - Manage document storage space

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteMemoryDocument" method="delete" path="/v2/memory-stores/{memory_store_key}/memories/{memory_entity_id}/documents/{document_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.memory_stores.delete_document(memory_store_key="<value>", memory_entity_id="<id>", document_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `memory_store_key`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the memory store                       |
| `memory_entity_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the memory                                 |
| `document_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the document                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |