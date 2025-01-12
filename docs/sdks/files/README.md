# Files
(*files*)

## Overview

### Available Operations

* [upload](#upload) - Upload file
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