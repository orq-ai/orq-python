# Files

## Overview

### Available Operations

* [list](#list) - List all files
* [create](#create) - Create file
* [get_content](#get_content) - Download file content
* [delete](#delete) - Delete file
* [get](#get) - Retrieve a file
* [update](#update) - Update file

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

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `limit`                                                                               | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `starting_after`                                                                      | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A cursor for use in pagination. Defines your place in the list for the next page.     |
| `ending_before`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A cursor for use in pagination. Defines your place in the list for the previous page. |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.FileListResponseBody](../../models/filelistresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

    res = orq.files.create(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    }, purpose="retrieval")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file`                                                              | [models.FileUploadFile](../../models/fileuploadfile.md)             | :heavy_check_mark:                                                  | The file to be uploaded.                                            |
| `purpose`                                                           | [Optional[models.Purpose]](../../models/purpose.md)                 | :heavy_minus_sign:                                                  | The intended purpose of the uploaded file.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileUploadResponseBody](../../models/fileuploadresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_content

Signs the object name and redirects to a presigned URL for downloading the file content. Accepts either a file ID or an object storage path (URL-encoded).

### Example Usage

<!-- UsageSnippet language="python" operationID="FileContent" method="get" path="/v2/files/{file_id_or_path}/content" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.files.get_content(file_id_or_path="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id_or_path`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The file ID or object storage path to retrieve content for.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete file

### Example Usage

<!-- UsageSnippet language="python" operationID="FileDelete" method="delete" path="/v2/files/{file_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.files.delete(file_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the file                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the file                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileGetResponseBody](../../models/filegetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the file                                                  |
| `file_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileUpdateResponseBody](../../models/fileupdateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |