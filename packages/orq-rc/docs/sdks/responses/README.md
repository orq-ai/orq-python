# Responses
(*agents.responses*)

## Overview

### Available Operations

* [create](#create) - Create an agent response

## create

Creates a new response representing an agent interaction. A response tracks the conversation from the initial message until the agent becomes inactive or errors. Supports both synchronous (waiting) and asynchronous (background) execution modes.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAgentResponse" method="post" path="/v2/agents/{agent_key}/responses" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.responses.create(agent_key="<value>", message={
        "role": "user",
        "parts": [],
    }, contact={
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
    }, background=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                        | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The key or ID of the agent to invoke                                                                                                                                                               |
| `message`                                                                                                                                                                                          | [models.A2AMessage](../../models/a2amessage.md)                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                 | The A2A message to send to the agent (user input or tool results)                                                                                                                                  |
| `task_id`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Optional task ID to continue an existing agent execution. When provided, the agent will continue the conversation from the existing task state. The task must be in an inactive state to continue. |
| `variables`                                                                                                                                                                                        | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional variables for template replacement in system prompt, instructions, and messages                                                                                                           |
| `contact`                                                                                                                                                                                          | [Optional[models.Contact]](../../models/contact.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                 | Information about the contact making the request. If the contact does not exist, it will be created automatically.                                                                                 |
| `thread`                                                                                                                                                                                           | [Optional[models.CreateAgentResponseThread]](../../models/createagentresponsethread.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Thread information to group related requests                                                                                                                                                       |
| `memory`                                                                                                                                                                                           | [Optional[models.Memory]](../../models/memory.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                 | Memory configuration for the agent execution. Used to associate memory stores with specific entities like users or sessions.                                                                       |
| `metadata`                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional metadata for the agent invocation as key-value pairs that will be included in traces                                                                                                      |
| `background`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | If true, returns immediately without waiting for completion. If false (default), waits until the agent becomes inactive or errors.                                                                 |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.CreateAgentResponseResponseBody](../../models/createagentresponseresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |