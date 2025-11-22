# Knowledge
(*knowledge*)

## Overview

### Available Operations

* [list](#list) - List all knowledge bases
* [create](#create) - Create a knowledge
* [retrieve](#retrieve) - Retrieves a knowledge base
* [update](#update) - Updates a knowledge
* [delete](#delete) - Deletes a knowledge
* [search](#search) - Search knowledge base
* [list_datasources](#list_datasources) - List all datasources
* [create_datasource](#create_datasource) - Create a new datasource
* [retrieve_datasource](#retrieve_datasource) - Retrieve a datasource
* [delete_datasource](#delete_datasource) - Deletes a datasource
* [update_datasource](#update_datasource) - Update a datasource
* [create_chunks](#create_chunks) - Create chunks for a datasource
* [list_chunks](#list_chunks) - List all chunks for a datasource
* [delete_chunks](#delete_chunks) - Delete multiple chunks
* [list_chunks_paginated](#list_chunks_paginated) - List chunks with offset-based pagination
* [get_chunks_count](#get_chunks_count) - Get chunks total count
* [update_chunk](#update_chunk) - Update a chunk
* [delete_chunk](#delete_chunk) - Delete a chunk
* [retrieve_chunk](#retrieve_chunk) - Retrieve a chunk

## list

Returns a list of your knowledge bases. The knowledge bases are returned sorted by creation date, with the most recent knowledge bases appearing first

### Example Usage

<!-- UsageSnippet language="python" operationID="ListKnowledgeBases" method="get" path="/v2/knowledge" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.list(limit=10)

    assert res is not None

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

**[models.ListKnowledgeBasesResponseBody](../../models/listknowledgebasesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a knowledge

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateKnowledge" method="post" path="/v2/knowledge" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.create(request={
        "type": "internal",
        "key": "<key>",
        "embedding_model": "<value>",
        "path": "Default",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CreateKnowledgeRequestBody](../../models/createknowledgerequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CreateKnowledgeResponseBody](../../models/createknowledgeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieve a knowledge base with the settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOneKnowledge" method="get" path="/v2/knowledge/{knowledge_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve(knowledge_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the knowledge base                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOneKnowledgeResponseBody](../../models/getoneknowledgeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates a knowledge

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateKnowledge" method="patch" path="/v2/knowledge/{knowledge_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update(knowledge_id="<id>", request_body={
        "path": "Default",
        "type": "external",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `knowledge_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | The unique identifier of the knowledge base                                     |
| `request_body`                                                                  | [models.UpdateKnowledgeRequestBody](../../models/updateknowledgerequestbody.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UpdateKnowledgeResponseBody](../../models/updateknowledgeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a knowledge base. Deleting a knowledge base will delete all the datasources and chunks associated with it.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteKnowledge" method="delete" path="/v2/knowledge/{knowledge_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.knowledge.delete(knowledge_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## search

Search a Knowledge Base and return the most similar chunks, along with their search and rerank scores. Note that all configuration changes made in the API will override the settings in the UI.

### Example Usage

<!-- UsageSnippet language="python" operationID="SearchKnowledge" method="post" path="/v2/knowledge/{knowledge_id}/search" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.search(knowledge_id="<id>", query="<value>", search_type="hybrid_search", rerank_config={
        "model": "cohere/rerank-multilingual-v3.0",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `knowledge_id`                                                                                                                                                                       | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The unique identifier or key of the knowledge base                                                                                                                                   |
| `query`                                                                                                                                                                              | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | The query to use to search the knowledge base                                                                                                                                        |
| `top_k`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | The number of results to return. If not provided, will default to the knowledge base configured `top_k`.                                                                             |
| `threshold`                                                                                                                                                                          | *Optional[float]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                   | The threshold to apply to the search. If not provided, will default to the knowledge base configured `threshold`                                                                     |
| `search_type`                                                                                                                                                                        | [Optional[models.SearchType]](../../models/searchtype.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                   | The type of search to perform. If not provided, will default to the knowledge base configured `retrieval_type`                                                                       |
| `filter_by`                                                                                                                                                                          | [Optional[models.FilterBy]](../../models/filterby.md)                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                   | The metadata filter to apply to the search. Check the [Searching a Knowledge Base](https://dash.readme.com/project/orqai/v2.0/docs/searching-a-knowledge-base) for more information. |
| `search_options`                                                                                                                                                                     | [Optional[models.SearchOptions]](../../models/searchoptions.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Additional search options                                                                                                                                                            |
| `rerank_config`                                                                                                                                                                      | [Optional[models.RerankConfig]](../../models/rerankconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                   | Override the rerank configuration for this search. If not provided, will use the knowledge base configured rerank settings.                                                          |
| `agentic_rag_config`                                                                                                                                                                 | [Optional[models.AgenticRagConfig]](../../models/agenticragconfig.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                   | Override the agentic RAG configuration for this search. If not provided, will use the knowledge base configured agentic RAG settings.                                                |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[models.SearchKnowledgeResponseBody](../../models/searchknowledgeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_datasources

List all datasources

### Example Usage

<!-- UsageSnippet language="python" operationID="ListDatasources" method="get" path="/v2/knowledge/{knowledge_id}/datasources" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.list_datasources(knowledge_id="<id>", limit=50, status=[
        "completed",
        "failed",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | Unique identifier of the knowledge base                                                                                                                                                                                                                                                                                                 |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `q`                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Search query to find datasources by name.                                                                                                                                                                                                                                                                                               |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `status`                                                                                                                                                                                                                                                                                                                                | [Optional[models.Status]](../../models/status.md)                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter datasources by status.                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListDatasourcesResponseBody](../../models/listdatasourcesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_datasource

Create a new datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDatasource" method="post" path="/v2/knowledge/{knowledge_id}/datasources" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.create_datasource(knowledge_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                               | Type                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                | Description                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                      | The unique identifier of the knowledge base                                                                                                                                                                             |
| `display_name`                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                      | The display name for the datasource visible in the UI. If omitted, the display name is derived from the uploaded file. When both `display_name` and `file_id` are provided, the provided `display_name` is prioritized. |
| `file_id`                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                      | The unique identifier of the file used for datasource creation. If provided, the file is immediately queued for chunking.                                                                                               |
| `chunking_options`                                                                                                                                                                                                      | [Optional[models.ChunkingOptions]](../../models/chunkingoptions.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                      | Configuration options specifying how the datasource file is chunked. Required if `file_id` is specified. Defaults to standard chunking options if omitted.                                                              |
| `retries`                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                     |

### Response

**[models.CreateDatasourceResponseBody](../../models/createdatasourceresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_datasource

Retrieve a datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveDatasource" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_datasource(knowledge_id="<id>", datasource_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveDatasourceResponseBody](../../models/retrievedatasourceresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_datasource

Deletes a datasource from a knowledge base. Deleting a datasource will remove it from the knowledge base and all associated chunks. This action is irreversible and cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDatasource" method="delete" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.knowledge.delete_datasource(knowledge_id="<id>", datasource_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_datasource

Update a datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDatasource" method="patch" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update_datasource(knowledge_id="<id>", datasource_id="<id>", display_name="Tony_Roberts")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateDatasourceResponseBody](../../models/updatedatasourceresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_chunks

Create chunks for a datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateChunk" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.create_chunks(knowledge_id="<id>", datasource_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the knowledge                                  |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the datasource                                 |
| `request_body`                                                      | List[[models.RequestBody](../../models/requestbody.md)]             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_chunks

List all chunks for a datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="ListChunks" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.list_chunks(knowledge_id="<id>", datasource_id="<id>", limit=10, status=[
        "completed",
        "failed",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique identifier of the knowledge base                                                                                                                                                                                                                                                                                             |
| `datasource_id`                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique identifier of the datasource.                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `q`                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Search query to find datasources by name.                                                                                                                                                                                                                                                                                               |
| `status`                                                                                                                                                                                                                                                                                                                                | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md)                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter datasources by status.                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListChunksResponseBody](../../models/listchunksresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_chunks

Delete multiple chunks

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteChunks" method="delete" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.delete_chunks(knowledge_id="<id>", datasource_id="<id>", chunk_ids=[
        "<value 1>",
        "<value 2>",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `chunk_ids`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of chunk IDs to delete                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteChunksResponseBody](../../models/deletechunksresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_chunks_paginated

List chunks with offset-based pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="ListChunksPaginated" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/list" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.list_chunks_paginated(knowledge_id="<id>", datasource_id="<id>", q="", limit=100, page=1)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `q`                                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search query to find chunks by text content                         |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter chunks by enabled status                                     |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter chunks by processing status                                  |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListChunksPaginatedResponseBody](../../models/listchunkspaginatedresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_chunks_count

Get chunks total count

### Example Usage

<!-- UsageSnippet language="python" operationID="GetChunksCount" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/count" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.get_chunks_count(knowledge_id="<id>", datasource_id="<id>", q="")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the datasource.                            |
| `q`                                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Search query to find chunks by text content                         |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter chunks by enabled status                                     |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Filter chunks by processing status                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetChunksCountResponseBody](../../models/getchunkscountresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_chunk

Update a chunk

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateChunk" method="patch" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update_chunk(chunk_id="<id>", datasource_id="<id>", knowledge_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `chunk_id`                                                                                                              | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The unique identifier of the chunk                                                                                      |
| `datasource_id`                                                                                                         | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The unique identifier of the data source                                                                                |
| `knowledge_id`                                                                                                          | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The unique identifier of the knowledge base                                                                             |
| `text`                                                                                                                  | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | The text content of the chunk                                                                                           |
| `embedding`                                                                                                             | List[*float*]                                                                                                           | :heavy_minus_sign:                                                                                                      | The embedding vector of the chunk. If not provided the chunk will be embedded with the knowledge base embeddings model. |
| `metadata`                                                                                                              | Dict[str, [models.UpdateChunkMetadata](../../models/updatechunkmetadata.md)]                                            | :heavy_minus_sign:                                                                                                      | Metadata of the chunk                                                                                                   |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.UpdateChunkResponseBody](../../models/updatechunkresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_chunk

Delete a chunk

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteChunk" method="delete" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.knowledge.delete_chunk(chunk_id="<id>", datasource_id="<id>", knowledge_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chunk_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the chunk                                  |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the data source                            |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_chunk

Retrieve a chunk

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOneChunk" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_chunk(chunk_id="<id>", datasource_id="<id>", knowledge_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `chunk_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the chunk                                  |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the data source                            |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the knowledge base                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOneChunkResponseBody](../../models/getonechunkresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |