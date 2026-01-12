# Conversations

## Overview

### Available Operations

* [list](#list) - List conversations
* [create](#create) - Create conversation
* [generate_name](#generate_name) - Generate conversation name
* [retrieve](#retrieve) - Retrieve conversation
* [update](#update) - Update conversation
* [delete](#delete) - Delete conversation
* [create_conversation_response](#create_conversation_response) - Create internal response

## list

Retrieves a paginated list of conversations in your workspace. Conversations are returned sorted by creation date (newest first). Use pagination parameters to efficiently navigate through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListConversations" method="get" path="/v2/conversations/" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.list(limit=25, starting_after="conv_01jj1hdhn79xas7a01wb3hysdb", ending_before="conv_01jj1hdhn79xas7a01wb3hysdb", entity_id="agent_01jj1hdhn79xas7a01wb3hysdb")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      | Example                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `limit`                                                                                                                                          | *Optional[int]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Maximum number of conversations to return. Range: 1-100. Default: 10.                                                                            | 25                                                                                                                                               |
| `starting_after`                                                                                                                                 | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Pagination cursor. Returns conversations created after the specified conversation ID.                                                            | conv_01jj1hdhn79xas7a01wb3hysdb                                                                                                                  |
| `ending_before`                                                                                                                                  | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Pagination cursor. Returns conversations created before the specified conversation ID.                                                           | conv_01jj1hdhn79xas7a01wb3hysdb                                                                                                                  |
| `entity_id`                                                                                                                                      | *Optional[str]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                               | Filter by parent entity. When specified, returns only conversations associated with this entity. When omitted, returns standalone conversations. | agent_01jj1hdhn79xas7a01wb3hysdb                                                                                                                 |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |                                                                                                                                                  |

### Response

**[models.ListConversationsResponseBody](../../models/listconversationsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new conversation in the workspace. Conversations serve as containers for organizing related messages and interactions. Each conversation is assigned a unique identifier and timestamps for tracking.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateConversation" method="post" path="/v2/conversations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.create(project_id="prj_01jj1hdhn79xas7a01wb3hysdb", display_name="Customer Support Session", metadata={
        "entity_id": "agent_01jj1hdhn79xas7a01wb3hysdb",
        "model": "openai/gpt-4o",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `project_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | Project identifier to associate the conversation with.                                    | prj_01jj1hdhn79xas7a01wb3hysdb                                                            |
| `display_name`                                                                            | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Human-readable name for the conversation. Defaults to "Untitled" if omitted.              | Customer Support Session                                                                  |
| `metadata`                                                                                | [Optional[models.CreateConversationMetadata]](../../models/createconversationmetadata.md) | :heavy_minus_sign:                                                                        | Optional metadata to attach to the conversation.                                          |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.CreateConversationResponseBody](../../models/createconversationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## generate_name

Generates a display name for a conversation using AI based on the provided context. Updates the conversation with the generated name and sets generatingTitle to false.

### Example Usage

<!-- UsageSnippet language="python" operationID="GenerateConversationName" method="post" path="/v2/conversations/{conversation_id}/generate-name" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.generate_name(conversation_id="conv_01jj1hdhn79xas7a01wb3hysdb", context="How do I integrate the SDK with my Node.js application?")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  | Example                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `conversation_id`                                                                                                            | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | The unique identifier of the conversation to generate a name for                                                             | conv_01jj1hdhn79xas7a01wb3hysdb                                                                                              |
| `context`                                                                                                                    | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | Conversation context used to generate a meaningful display name. Typically the first user message or a conversation summary. | How do I integrate the SDK with my Node.js application?                                                                      |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |                                                                                                                              |

### Response

**[models.GenerateConversationNameResponseBody](../../models/generateconversationnameresponsebody.md)**

### Errors

| Error Type                                                       | Status Code                                                      | Content Type                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| models.GenerateConversationNameConversationsResponseBody         | 400                                                              | application/json                                                 |
| models.GenerateConversationNameConversationsResponseResponseBody | 404                                                              | application/json                                                 |
| models.APIError                                                  | 4XX, 5XX                                                         | \*/\*                                                            |

## retrieve

Retrieves detailed information about a specific conversation identified by its unique ID. Returns the complete conversation object including metadata and timestamps.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveConversation" method="get" path="/v2/conversations/{conversation_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.retrieve(conversation_id="conv_01jj1hdhn79xas7a01wb3hysdb")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the conversation to retrieve               | conv_01jj1hdhn79xas7a01wb3hysdb                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ConversationWithMessagesResponse](../../models/conversationwithmessagesresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.RetrieveConversationResponseBody | 404                                     | application/json                        |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## update

Modifies an existing conversation's properties. Only the fields provided in the request body will be updated; all other fields remain unchanged. Changes are applied immediately.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateConversation" method="patch" path="/v2/conversations/{conversation_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.update(conversation_id="conv_01jj1hdhn79xas7a01wb3hysdb", display_name="Updated Support Session")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `conversation_id`                                                                         | *str*                                                                                     | :heavy_check_mark:                                                                        | The unique identifier of the conversation to update                                       | conv_01jj1hdhn79xas7a01wb3hysdb                                                           |
| `display_name`                                                                            | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | New display name for the conversation. Maximum 100 characters.                            | Updated Support Session                                                                   |
| `metadata`                                                                                | [Optional[models.UpdateConversationMetadata]](../../models/updateconversationmetadata.md) | :heavy_minus_sign:                                                                        | Metadata fields to update. Only provided fields are modified.                             |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.UpdateConversationResponseBody](../../models/updateconversationresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.UpdateConversationConversationsResponseBody | 404                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## delete

Permanently removes a conversation from the workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteConversation" method="delete" path="/v2/conversations/{conversation_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.conversations.delete(conversation_id="conv_01jj1hdhn79xas7a01wb3hysdb")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the conversation to delete                 | conv_01jj1hdhn79xas7a01wb3hysdb                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.DeleteConversationResponseBody | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

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

    res = orq.conversations.create_conversation_response(conversation_id="<id>", message={
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