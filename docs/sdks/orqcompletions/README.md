# OrqCompletions
(*router.chat.completions*)

## Overview

### Available Operations

* [create](#create) - Create Chat Completion

## create

For sending requests to chat completion models

### Example Usage

```python
import orq_ai_sdk
from orq_ai_sdk import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.router.chat.completions.create(request={
    "model": "Fiesta",
    "messages": [
        {
            "role": orq_ai_sdk.RouterChatCompletionsMessagesRole.USER,
            "content": "<value>",
        },
        {
            "role": orq_ai_sdk.MessagesRole.SYSTEM,
            "content": [
                {
                    "type": orq_ai_sdk.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
                {
                    "type": orq_ai_sdk.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
                {
                    "type": orq_ai_sdk.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
            ],
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.RouterChatCompletionsRequestBody](../../models/routerchatcompletionsrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.RouterChatCompletionsResponse](../../models/routerchatcompletionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |