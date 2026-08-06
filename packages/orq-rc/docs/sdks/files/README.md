# Files

## Overview

### Available Operations

* [list](#list) - List all files
* [create](#create) - Upload a file
* [get_content](#get_content) - Download file content
* [get](#get) - Retrieve a file
* [delete](#delete) - Delete a file
* [update](#update) - Update a file

## list

Returns a list of the files that your account has access to. orq.ai sorts and returns the files by their creation dates, placing the most recently created files at the top.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileList" method="get" path="/v2/files" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.list(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Page size. Unset uses the server default.                                                                                                                                                                                                       |
| `starting_after`                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Cursor for forward pagination. Set to the `file_id` of the last item<br/> from the previous page.                                                                                                                                               |
| `ending_before`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Cursor for backward pagination. Set to the `file_id` of the first item<br/> from the previous page.                                                                                                                                             |
| `project_id`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |
| `purpose`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | Restrict results to files declared with this purpose. Accepts a purpose<br/> alias (`retrieval`, `knowledge_datasource`, `batch`, `code_interpreter`)<br/> or canonical `FILE_PURPOSE_*` name case-insensitively. Omit to list files<br/> of every purpose. |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |

### Response

**[models.ListFilesResponse](../../models/listfilesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Files are used to upload documents that can be used with features like Deployments.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileUpload" method="post" path="/v2/files" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.create(filename="example.file", content="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filename`                                                                                                                                                                 | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Name to store for the uploaded file, including extension when available.                                                                                                   |
| `content`                                                                                                                                                                  | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Base64-encoded file contents.                                                                                                                                              |
| `purpose`                                                                                                                                                                  | [Optional[models.FilePurpose]](../../models/filepurpose.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `content_type`                                                                                                                                                             | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | MIME type of the uploaded content, for example `application/pdf`.                                                                                                          |
| `project_id`                                                                                                                                                               | *Optional[str]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                         | Project the file is created in. Optional: project-scoped API keys default to the key's bound project; workspace-scoped callers default to the workspace's default project. |
| `retries`                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                        |

### Response

**[models.CreateFileResponse](../../models/createfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get_content

Returns a presigned URL for downloading the file content by file ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileContent" method="get" path="/v2/files/{file_id_or_path}/content" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.get_content(file_id_or_path="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id_or_path`                                                   | *str*                                                               | :heavy_check_mark:                                                  | File ID or path used to locate the file content.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFileContentResponse](../../models/getfilecontentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves the details of an existing file object. After you supply a unique file ID, orq.ai returns the corresponding file object.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileGet" method="get" path="/v2/files/{file_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.get(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID to retrieve.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFileResponse](../../models/getfileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a file and its stored content from the project.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileDelete" method="delete" path="/v2/files/{file_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.delete(file_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID to delete.                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteFileResponse](../../models/deletefileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates the metadata of an existing file object.

### Example Usage

<!-- UsageSnippet language="python" operationID="FileUpdate" method="patch" path="/v2/files/{file_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.update(file_id="<id>", file_name="example.file")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | File ID to update.                                                  |
| `file_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | New display file name, including extension when available.          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateFileResponse](../../models/updatefileresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |