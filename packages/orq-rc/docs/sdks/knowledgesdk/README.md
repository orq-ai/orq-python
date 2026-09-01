# Knowledge

## Overview

### Available Operations

* [list](#list) - List all knowledge bases
* [create](#create) - Create a knowledge
* [retrieve](#retrieve) - Retrieves a knowledge base
* [delete](#delete) - Deletes a knowledge
* [update](#update) - Updates a knowledge
* [list_datasources](#list_datasources) - List all datasources
* [create_datasource](#create_datasource) - Create a new datasource
* [preview_chunks](#preview_chunks) - Preview datasource chunks
* [retrieve_datasource](#retrieve_datasource) - Retrieve a datasource
* [delete_datasource](#delete_datasource) - Deletes a datasource
* [update_datasource](#update_datasource) - Update a datasource
* [list_chunks](#list_chunks) - List all chunks for a datasource
* [create_chunks](#create_chunks) - Create chunks for a datasource
* [delete_chunks](#delete_chunks) - Delete multiple chunks
* [get_chunks_count](#get_chunks_count) - Get chunks total count
* [list_chunks_paginated](#list_chunks_paginated) - List chunks with offset-based pagination
* [retrieve_chunk](#retrieve_chunk) - Retrieve a chunk
* [delete_chunk](#delete_chunk) - Delete a chunk
* [update_chunk](#update_chunk) - Update a chunk
* [toggle_chunk](#toggle_chunk) - Set a chunk's enabled status
* [retrieve_processing_status](#retrieve_processing_status) - Retrieve datasource processing status
* [search](#search) - Search knowledge base
* [retrieve_file_url](#retrieve_file_url) - Retrieve a file upload URL

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

    res = orq.knowledge.list(limit=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 300, and the default is 25                                                                                                                                                                                                                               |
| `search`                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter knowledge bases by key (case-insensitive match)                                                                                                                                                                                                                                                                                  |
| `updated_by`                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter by the users who last updated the knowledge base. Accepts a comma-separated list of user IDs                                                                                                                                                                                                                                     |
| `type`                                                                                                                                                                                                                                                                                                                                  | [Optional[models.ListKnowledgeBasesQueryParamType]](../../models/listknowledgebasesqueryparamtype.md)                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter knowledge bases by type                                                                                                                                                                                                                                                                                                          |
| `project_id`                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter knowledge bases by project ID                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.KnowledgeBasesServiceListResponse](../../models/knowledgebasesservicelistresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates an internal or external knowledge base. Internal knowledge bases embed and index uploaded content; external knowledge bases query the configured external retrieval API.

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

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.KnowledgeBasesServiceCreateRequest](../../models/knowledgebasesservicecreaterequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.Knowledge](../../models/knowledge.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Knowledge](../../models/knowledge.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates a knowledge base. Omitted optional fields retain their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateKnowledge" method="patch" path="/v2/knowledge/{knowledge_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update(knowledge_id="<id>", knowledge_bases_service_update_request={
        "path": "Default",
        "type": "external",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `knowledge_bases_service_update_request`                                                        | [models.KnowledgeBasesServiceUpdateRequest](../../models/knowledgebasesserviceupdaterequest.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.Knowledge](../../models/knowledge.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_datasources

Returns the datasources in a knowledge base. Use cursors to page through results and optional query or status filters to narrow the list.

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
| `status`                                                                                                                                                                                                                                                                                                                                | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md)                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter datasources by status.                                                                                                                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.DatasourcesServiceListResponse](../../models/datasourcesservicelistresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_datasource

Creates a datasource shell when only a display name is provided. When file_id is provided, the uploaded file is queued for chunking and ingestion.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDatasource" method="post" path="/v2/knowledge/{knowledge_id}/datasources" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.create_datasource(knowledge_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `display_name`                                                                          | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `description`                                                                           | *OptionalNullable[str]*                                                                 | :heavy_minus_sign:                                                                      | The description of the knowledge base                                                   |
| `file_id`                                                                               | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `chunking_options`                                                                      | [Optional[models.DatasourceChunkingOptions]](../../models/datasourcechunkingoptions.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `id`                                                                                    | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Compatibility fields used by the former datasource shell/legacy route.                  |
| `attachment`                                                                            | [Optional[models.DatasourceAttachment]](../../models/datasourceattachment.md)           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `metadata`                                                                              | [Optional[models.CountMetadata]](../../models/countmetadata.md)                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.Datasource](../../models/datasource.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## preview_chunks

Parses an uploaded file and returns the chunks it would produce for the given chunking options without creating a datasource.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreviewDatasourceChunks" method="post" path="/v2/knowledge/{knowledge_id}/datasources/preview-chunks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.preview_chunks(knowledge_id="<id>", file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `file_id`                                                                               | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `chunking_options`                                                                      | [Optional[models.DatasourceChunkingOptions]](../../models/datasourcechunkingoptions.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.DatasourcesServicePreviewChunksResponse](../../models/datasourcesservicepreviewchunksresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve_datasource

Retrieves a datasource and its current processing status and chunk count.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveDatasource" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_datasource(knowledge_id="<id>", datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Datasource](../../models/datasource.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_datasource

Updates the display name of a datasource.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDatasource" method="patch" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update_datasource(knowledge_id="<id>", datasource_id="<id>", display_name="Tony_Roberts")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Datasource](../../models/datasource.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_chunks

Returns chunks using cursor pagination, with optional text and processing-status filters.

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

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique identifier of the knowledge base                                                                                                                                                                                                                                                                                             |
| `datasource_id`                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique identifier of the datasource.                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `q`                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Search query to find datasources by name.                                                                                                                                                                                                                                                                                               |
| `status`                                                                                                                                                                                                                                                                                                                                | [Optional[models.ListChunksQueryParamStatus]](../../models/listchunksqueryparamstatus.md)                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter chunks by status.                                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ChunksServiceListResponse](../../models/chunksservicelistresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create_chunks

Creates between 1 and 100 chunks. Chunks with supplied embeddings are indexed immediately; chunks without embeddings are queued for embedding.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateChunk" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.create_chunks(knowledge_id="<id>", datasource_id="<id>", request_body=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_body`                                                      | List[[models.UpsertChunk](../../models/upsertchunk.md)]             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.KnowledgeChunk]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_chunks

Deletes up to 100 chunks and reports IDs that were not found or could not be deleted.

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

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `chunk_ids`                                                         | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of chunk IDs to delete                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChunksServiceDeleteManyResponse](../../models/chunksservicedeletemanyresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_chunks_count

Returns the total count of chunks in a datasource. When `q` is provided, the count reflects indexed chunks only — recently created chunks may not be counted until embedding completes.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetChunksCount" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/count" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.get_chunks_count(knowledge_id="<id>", datasource_id="<id>", q="")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                      | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `datasource_id`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `q`                                                                                                 | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `enabled`                                                                                           | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `status`                                                                                            | [Optional[models.ChunksServiceCountRequestStatus]](../../models/chunksservicecountrequeststatus.md) | :heavy_minus_sign:                                                                                  | Filter chunks by processing status                                                                  |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ChunksServiceCountResponse](../../models/chunksservicecountresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_chunks_paginated

Returns a page of chunks, with optional text, enabled-state, and processing-status filters.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListChunksPaginated" method="post" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/list" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.list_chunks_paginated(knowledge_id="<id>", datasource_id="<id>", q="", limit=100, page=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                      | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `datasource_id`                                                                                                     | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `q`                                                                                                                 | *Optional[str]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `enabled`                                                                                                           | *Optional[bool]*                                                                                                    | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `status`                                                                                                            | [Optional[models.ChunksServiceListPaginatedRequestStatus]](../../models/chunksservicelistpaginatedrequeststatus.md) | :heavy_minus_sign:                                                                                                  | Filter chunks by processing status                                                                                  |
| `limit`                                                                                                             | *Optional[int]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `page`                                                                                                              | *Optional[int]*                                                                                                     | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.ChunksServiceListPaginatedResponse](../../models/chunksservicelistpaginatedresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve_chunk

Retrieves a chunk by its chunk identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOneChunk" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_chunk(knowledge_id="<id>", datasource_id="<id>", chunk_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `chunk_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.KnowledgeChunk](../../models/knowledgechunk.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_chunk

Deletes a chunk from the datasource and its vector index.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteChunk" method="delete" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.knowledge.delete_chunk(knowledge_id="<id>", datasource_id="<id>", chunk_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `chunk_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update_chunk

Updates chunk text, metadata, or a supplied embedding. Changing text without an embedding queues the chunk for re-embedding.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateChunk" method="patch" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.update_chunk(knowledge_id="<id>", datasource_id="<id>", chunk_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                             | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `datasource_id`                                                                                            | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `chunk_id`                                                                                                 | *str*                                                                                                      | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `text`                                                                                                     | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | The text content of the chunk                                                                              |
| `embedding`                                                                                                | List[*float*]                                                                                              | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |
| `metadata`                                                                                                 | Dict[str, [models.ChunksServiceUpdateRequestMetadata](../../models/chunksserviceupdaterequestmetadata.md)] | :heavy_minus_sign:                                                                                         | Metadata of the chunk                                                                                      |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[models.KnowledgeChunk](../../models/knowledgechunk.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## toggle_chunk

Enables or disables a chunk for retrieval. If the vector-index document is missing, enabling the chunk queues it for embedding.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateChunkEnabled" method="patch" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/chunks/{chunk_id}/enabled" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.toggle_chunk(knowledge_id="<id>", datasource_id="<id>", chunk_id="<id>", enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `chunk_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.KnowledgeChunk](../../models/knowledgechunk.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve_processing_status

Returns aggregate queued, completed, passed, and failed chunk counts together with the datasource and chunk processing attempts.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOneDatasourceProcessingStatus" method="get" path="/v2/knowledge/{knowledge_id}/datasources/{datasource_id}/datasource-processing-status" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_processing_status(knowledge_id="<id>", datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DatasourcesServiceGetProcessingStatusResponse](../../models/datasourcesservicegetprocessingstatusresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

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

    res = orq.knowledge.search(knowledge_id="<id>", query="<value>", rerank_config={
        "model": "cohere/rerank-multilingual-v3.0",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                                                                                                         | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | The unique identifier or key of the knowledge base.                                                                                                                    |
| `query`                                                                                                                                                                | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | The query to use to search the knowledge base                                                                                                                          |
| `top_k`                                                                                                                                                                | *Optional[int]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | The number of results to return. If not provided, will default to the knowledge base configured `top_k`.                                                               |
| `threshold`                                                                                                                                                            | *Optional[float]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                     | The threshold to apply to the search. If not provided, will default to the knowledge base configured `threshold`                                                       |
| `search_type`                                                                                                                                                          | [Optional[models.SearchType]](../../models/searchtype.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                     | N/A                                                                                                                                                                    |
| `filter_by`                                                                                                                                                            | [Optional[models.FilterBy]](../../models/filterby.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                     | The metadata filter to apply to the search. Check the [Searching a Knowledge Base](https://docs.orq.ai/docs/knowledge/api#knowledge-base-search) for more information. |
| `search_options`                                                                                                                                                       | [Optional[models.SearchOptions]](../../models/searchoptions.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Additional search options                                                                                                                                              |
| `rerank_config`                                                                                                                                                        | [Optional[models.SearchRerankConfig]](../../models/searchrerankconfig.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                     | Override the rerank configuration for this search. If not provided, will use the knowledge base configured rerank settings.                                            |
| `agentic_rag_config`                                                                                                                                                   | [OptionalNullable[models.SearchKnowledgeRequestAgenticRagConfig]](../../models/searchknowledgerequestagenticragconfig.md)                                              | :heavy_minus_sign:                                                                                                                                                     | Override the agentic RAG configuration for this search. If not provided, will use the knowledge base configured agentic RAG settings.                                  |
| `retrieval_config`                                                                                                                                                     | [Optional[models.SearchRetrievalConfig]](../../models/searchretrievalconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                                     | Override the stored retrieval configuration for this search. If not provided, the knowledge base configuration is used.                                                |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |

### Response

**[models.SearchKnowledgeResponse](../../models/searchknowledgeresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve_file_url

Creates a presigned upload policy for a file that will be attached to a knowledge-base datasource. Submit the returned form fields and file directly to the returned URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOneFileUploadUrl" method="get" path="/v2/knowledge/{knowledge_id}/upload-file" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.knowledge.retrieve_file_url(knowledge_id="<id>", file_name="example.file", content_type="<value>", datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `knowledge_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `file_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The name of the file to upload.                                     |
| `content_type`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The media type of the file to upload.                               |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The datasource identifier that will own the uploaded file.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUploadFileURLResponse](../../models/getuploadfileurlresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.KnowledgeAPIError | 500                      | application/json         |
| models.APIDefaultError   | 4XX, 5XX                 | \*/\*                    |