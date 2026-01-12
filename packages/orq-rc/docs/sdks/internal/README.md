# Internal

## Overview

### Available Operations

* [create_conversation_response](#create_conversation_response) - Create internal response

## create_conversation_response

Creates a response for a freeform conversation without an agent. Uses a default model for generation.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateConversationResponse" method="post" path="/v2/conversations/{conversation_id}/responses" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.internal.create_conversation_response(conversation_id="<id>", message={
        "role": "user",
        "parts": [
            {
                "kind": "text",
                "text": "Hello!",
            },
        ],
    }, model="Prius", stream=True)

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `conversation_id`                                                                  | *str*                                                                              | :heavy_check_mark:                                                                 | The unique identifier of the conversation                                          |
| `message`                                                                          | [models.UserMessageRequest](../../models/usermessagerequest.md)                    | :heavy_check_mark:                                                                 | The user message to send to the model                                              |
| `model`                                                                            | *str*                                                                              | :heavy_check_mark:                                                                 | The model to use for generation in format provider/model_id (e.g., openai/gpt-4o). |
| `task_id`                                                                          | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Task ID for continuing a previous conversation turn                                |
| `stream`                                                                           | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether to stream the response (default: true)                                     |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[Union[eventstreaming.EventStream[models.CreateConversationResponseResponseBody], eventstreaming.EventStreamAsync[models.CreateConversationResponseResponseBody]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |