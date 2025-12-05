# Conversations
(*conversations*)

## Overview

### Available Operations

* [list](#list) - List conversations
* [create](#create) - Create conversation
* [retrieve](#retrieve) - Retrieve conversation
* [update](#update) - Update conversation
* [delete](#delete) - Delete conversation

## list

Retrieves a paginated list of conversations in your workspace. Conversations are returned sorted by creation date (newest first). Use pagination parameters to efficiently navigate through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListConversations" method="get" path="/v2/conversations" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.conversations.list(limit=10, starting_after="conv_01jj1hdhn79xas7a01wb3hysdb", ending_before="conv_01jj1hdhn79xas7a01wb3hysdb")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                | Example                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                    | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. | 10                                                                                                         |
| `starting_after`                                                                                           | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | A cursor for use in pagination. `starting_after` is a conversation ID that defines your place in the list. | conv_01jj1hdhn79xas7a01wb3hysdb                                                                            |
| `ending_before`                                                                                            | *Optional[str]*                                                                                            | :heavy_minus_sign:                                                                                         | A cursor for use in pagination. `ending_before` is a conversation ID that defines your place in the list.  | conv_01jj1hdhn79xas7a01wb3hysdb                                                                            |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |                                                                                                            |

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

    res = orq.conversations.create(display_name="Support Chat #1234")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `display_name`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | Display name for the conversation. Can be auto-generated or set by the user. | Support Chat #1234                                                           |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.CreateConversationResponseBody](../../models/createconversationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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

**[models.RetrieveConversationResponseBody](../../models/retrieveconversationresponsebody.md)**

### Errors

| Error Type                                           | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| models.RetrieveConversationConversationsResponseBody | 404                                                  | application/json                                     |
| models.APIError                                      | 4XX, 5XX                                             | \*/\*                                                |

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

    res = orq.conversations.update(conversation_id="conv_01jj1hdhn79xas7a01wb3hysdb", display_name="Renamed Conversation")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `conversation_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the conversation to update                 | conv_01jj1hdhn79xas7a01wb3hysdb                                     |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Updated display name for the conversation.                          | Renamed Conversation                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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