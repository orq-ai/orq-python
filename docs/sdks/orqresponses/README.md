# Agents.Responses

## Overview

### Available Operations

* [create](#create) - Create response
* [get](#get) - Get response

## create

Initiates an agent conversation and returns a complete response. This endpoint manages the full lifecycle of an agent interaction, from receiving the initial message through all processing steps until completion. Supports synchronous execution (waits for completion) and asynchronous execution (returns immediately with task ID). The response includes all messages exchanged, tool calls made, and token usage statistics. Ideal for request-response patterns where you need the complete interaction result.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAgentResponseRequest" method="post" path="/v2/agents/{agent_key}/responses" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.responses.create(agent_key="<value>", message={
        "role": "tool",
        "parts": [],
    }, identity={
        "id": "contact_01ARZ3NDEKTSV4RRFFQ69G5FAV",
        "display_name": "Jane Doe",
        "email": "jane.doe@example.com",
        "metadata": [
            {
                "department": "Engineering",
                "role": "Senior Developer",
            },
        ],
        "logo_url": "https://example.com/avatars/jane-doe.jpg",
        "tags": [
            "hr",
            "engineering",
        ],
    }, thread={
        "id": "thread_01ARZ3NDEKTSV4RRFFQ69G5FAV",
        "tags": [
            "customer-support",
            "priority-high",
        ],
    }, background=False, stream=False)

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `agent_key`                                                                                                                                                                                                  | *str*                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                           | The unique key of identifier of the agent to invoke                                                                                                                                                          |
| `message`                                                                                                                                                                                                    | [models.A2AMessage](../../models/a2amessage.md)                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                           | The A2A message to send to the agent (user input or tool results)                                                                                                                                            |
| `task_id`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | Optional task ID to continue an existing agent execution. When provided, the agent will continue the conversation from the existing task state. The task must be in an inactive state to continue.           |
| `variables`                                                                                                                                                                                                  | Dict[str, *Any*]                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Optional variables for template replacement in system prompt, instructions, and messages                                                                                                                     |
| `identity`                                                                                                                                                                                                   | [Optional[models.Identity]](../../models/identity.md)                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                           | Information about the identity making the request. If the identity does not exist, it will be created automatically.                                                                                         |
| `contact`                                                                                                                                                                                                    | [Optional[models.Contact]](../../models/contact.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                           | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>@deprecated Use identity instead. Information about the contact making the request. |
| `thread`                                                                                                                                                                                                     | [Optional[models.CreateAgentResponseRequestThread]](../../models/createagentresponserequestthread.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                           | Thread information to group related requests                                                                                                                                                                 |
| `memory`                                                                                                                                                                                                     | [Optional[models.CreateAgentResponseRequestMemory]](../../models/createagentresponserequestmemory.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                           | Memory configuration for the agent execution. Used to associate memory stores with specific entities like users or sessions.                                                                                 |
| `metadata`                                                                                                                                                                                                   | Dict[str, *Any*]                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Optional metadata for the agent invocation as key-value pairs that will be included in traces                                                                                                                |
| `engine`                                                                                                                                                                                                     | [Optional[models.CreateAgentResponseRequestEngine]](../../models/createagentresponserequestengine.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                           | Override template engine for this invocation. If not provided, uses the agent default.                                                                                                                       |
| `configuration`                                                                                                                                                                                              | [Optional[models.Configuration]](../../models/configuration.md)                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                           | Configuration options for the agent invocation                                                                                                                                                               |
| `background`                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | If true, returns immediately without waiting for completion. If false (default), waits until the agent becomes inactive or errors.                                                                           |
| `stream`                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | If true, returns Server-Sent Events (SSE) streaming response with real-time events. If false (default), returns standard JSON response.                                                                      |
| `conversation`                                                                                                                                                                                               | [Optional[models.Conversation]](../../models/conversation.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                           | Conversation context for chat studio integration                                                                                                                                                             |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[models.CreateAgentResponseRequestResponse](../../models/createagentresponserequestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves the current state of an agent response by task ID. Returns the response output, model information, token usage, and execution status. When the agent is still processing, the output array will be empty and status will be `in_progress`. Once completed, the response includes the full output, usage statistics, and finish reason.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAgentResponse" method="get" path="/v2/agents/{agent_key}/responses/{task_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.responses.get(agent_key="<value>", task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique key identifier of the agent                              |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The agent execution task ID returned from create response           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAgentResponse](../../models/getagentresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |