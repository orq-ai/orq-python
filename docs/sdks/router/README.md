# Router

## Overview

### Available Operations

* [ocr](#ocr) - Extracts text content while maintaining document structure and hierarchy

## ocr

Extracts text content while maintaining document structure and hierarchy

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/router/ocr" method="post" path="/v2/router/ocr" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.router.ocr(model="Golf", document={
        "type": "document_url",
        "document_url": "https://fond-pants.net/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `model`                                                                                               | *str*                                                                                                 | :heavy_check_mark:                                                                                    | ID of the model to use for OCR.                                                                       |
| `document`                                                                                            | [models.Document](../../models/document.md)                                                           | :heavy_check_mark:                                                                                    | Document to run OCR on. Can be a DocumentURLChunk or ImageURLChunk.                                   |
| `pages`                                                                                               | List[*int*]                                                                                           | :heavy_minus_sign:                                                                                    | Specific pages to process. Can be a single number, range, or list. Starts from 0. Null for all pages. |
| `ocr_settings`                                                                                        | [Optional[models.OcrSettings]](../../models/ocrsettings.md)                                           | :heavy_minus_sign:                                                                                    | Optional settings for the OCR run                                                                     |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.PostV2RouterOcrResponseBody](../../models/postv2routerocrresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |