# Files
(*files*)

## Overview

### Available Operations

* [upload](#upload) - Upload file
* [list](#list) - List all files
* [get](#get) - Get file by ID
* [update](#update) - Update file name
* [delete](#delete) - Delete file
* [bulk_upload](#bulk_upload) - Bulk upload file

## upload

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.upload()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.FileUploadRequestBody](../../models/fileuploadrequestbody.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.FileUploadResponseBody](../../models/fileuploadresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

List all files

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.list()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `last_id`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `first_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileListResponseBody](../../models/filelistresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Get file by ID

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.get(file_id="<id>")

    assert res is not None

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

Update file name

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.update(file_id="<id>", file_name="example.file")

    assert res is not None

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

## delete

Delete file

### Example Usage

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

## bulk_upload

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.files.bulk_upload(files=[
        {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    ], purpose="retrieval")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `files`                                                                 | List[[models.BulkFileUploadFiles](../../models/bulkfileuploadfiles.md)] | :heavy_check_mark:                                                      | N/A                                                                     |
| `purpose`                                                               | [models.BulkFileUploadPurpose](../../models/bulkfileuploadpurpose.md)   | :heavy_check_mark:                                                      | The intended purpose of the uploaded file.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |