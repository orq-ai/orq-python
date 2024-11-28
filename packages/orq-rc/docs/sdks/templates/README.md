# Templates
(*prompt.templates*)

## Overview

### Available Operations

* [get_all](#get_all) - Get all prompt templates

## get_all

Get all prompt templates

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as s:
    res = s.prompt.templates.get_all()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `page`                                                                                                | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `limit`                                                                                               | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `request_body`                                                                                        | [Optional[models.GetAllPromptTemplatesRequestBody]](../../models/getallprompttemplatesrequestbody.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.GetAllPromptTemplatesResponseBody](../../models/getallprompttemplatesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |