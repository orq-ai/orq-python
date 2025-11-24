# Agents
(*agents*)

## Overview

### Available Operations

* [create](#create) - Create agent
* [delete](#delete) - Delete agent
* [retrieve](#retrieve) - Retrieve agent
* [update](#update) - Update agent
* [~~invoke~~](#invoke) - Execute an agent task :warning: **Deprecated**
* [list](#list) - List agents
* [~~run~~](#run) - Run an agent with configuration :warning: **Deprecated**
* [~~stream_run~~](#stream_run) - Run agent with streaming response :warning: **Deprecated**
* [~~stream~~](#stream) - Stream agent execution in real-time :warning: **Deprecated**

## create

Creates a new agent with the specified configuration, including model selection, instructions, tools, and knowledge bases. Agents are intelligent assistants that can execute tasks, interact with tools, and maintain context through memory stores. The agent can be configured with a primary model and optional fallback models for automatic failover, custom instructions for behavior control, and various settings to control execution limits and tool usage.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAgentRequest" method="post" path="/v2/agents" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.create(request={
        "key": "<key>",
        "role": "<value>",
        "description": "alongside beneath doubtfully behest validity bah after furthermore",
        "instructions": "<value>",
        "path": "Default",
        "model": {
            "id": "<id>",
            "retry": {
                "count": 3,
                "on_codes": [
                    429,
                    500,
                    502,
                    503,
                    504,
                ],
            },
        },
        "settings": {
            "tools": [
                {
                    "type": "mcp",
                    "id": "01KA84ND5J0SWQMA2Q8HY5WZZZ",
                    "tool_id": "01KXYZ123456789",
                    "requires_approval": False,
                },
            ],
        },
        "knowledge_bases": [
            {
                "knowledge_id": "customer-knowledge-base",
            },
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.CreateAgentRequestRequestBody](../../models/createagentrequestrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CreateAgentRequestResponseBody](../../models/createagentrequestresponsebody.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.CreateAgentRequestAgentsResponseBody | 409                                         | application/json                            |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## delete

Permanently removes an agent from the workspace. This operation is irreversible and will delete all associated configuration including model assignments, tools, knowledge bases, memory stores, and cached data. Active agent sessions will be terminated, and the agent key will become available for reuse.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAgent" method="delete" path="/v2/agents/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.agents.delete(agent_key="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the agent to delete                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.DeleteAgentResponseBody | 404                            | application/json               |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## retrieve

Retrieves detailed information about a specific agent identified by its unique key or identifier. Returns the complete agent manifest including configuration settings, model assignments (primary and fallback), tools, knowledge bases, memory stores, instructions, and execution parameters. Use this endpoint to fetch the current state and configuration of an individual agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveAgentRequest" method="get" path="/v2/agents/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.retrieve(agent_key="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the agent to retrieve                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveAgentRequestResponseBody](../../models/retrieveagentrequestresponsebody.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.RetrieveAgentRequestAgentsResponseBody | 404                                           | application/json                              |
| models.APIError                               | 4XX, 5XX                                      | \*/\*                                         |

## update

Modifies an existing agent's configuration with partial updates. Supports updating any aspect of the agent including model assignments (primary and fallback), instructions, tools, knowledge bases, memory stores, and execution parameters. Only the fields provided in the request body will be updated; all other fields remain unchanged. Changes take effect immediately for new agent invocations.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAgent" method="patch" path="/v2/agents/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.update(agent_key="<value>", model="El Camino", settings={
        "tools": [
            {
                "type": "mcp",
                "id": "01KA84ND5J0SWQMA2Q8HY5WZZZ",
                "tool_id": "01KXYZ123456789",
                "requires_approval": False,
            },
        ],
    }, path="Default", knowledge_bases=[
        {
            "knowledge_id": "customer-knowledge-base",
        },
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | The unique key of the agent to update                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                |
| `key`                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `display_name`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `project_id`                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `role`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `description`                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `instructions`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `system_prompt`                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | A custom system prompt template for the agent. If omitted, the default template is used.                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                |
| `model`                                                                                                                                                                                                                                                                                        | [Optional[models.UpdateAgentModelConfiguration]](../../models/updateagentmodelconfiguration.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Model configuration for agent execution. Can be a simple model ID string or a configuration object with optional behavior parameters and retry settings.                                                                                                                                       |                                                                                                                                                                                                                                                                                                |
| `fallback_models`                                                                                                                                                                                                                                                                              | List[[models.UpdateAgentFallbackModelConfiguration](../../models/updateagentfallbackmodelconfiguration.md)]                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Optional array of fallback models used when the primary model fails. Fallbacks are attempted in order. All models must support tool calling.                                                                                                                                                   |                                                                                                                                                                                                                                                                                                |
| `settings`                                                                                                                                                                                                                                                                                     | [Optional[models.UpdateAgentSettings]](../../models/updateagentsettings.md)                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `path`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Entity storage path in the format: `project/folder/subfolder/...`<br/><br/>The first element identifies the project, followed by nested folders (auto-created as needed).<br/><br/>With project-based API keys, the first element is treated as a folder name, as the project is predetermined by the API key. | Default                                                                                                                                                                                                                                                                                        |
| `memory_stores`                                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Array of memory store identifiers. Accepts both memory store IDs and keys.                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                |
| `knowledge_bases`                                                                                                                                                                                                                                                                              | List[[models.UpdateAgentKnowledgeBases](../../models/updateagentknowledgebases.md)]                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `team_of_agents`                                                                                                                                                                                                                                                                               | List[[models.UpdateAgentTeamOfAgents](../../models/updateagentteamofagents.md)]                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The agents that are accessible to this orchestrator. The main agent can hand off to these agents to perform tasks.                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                |
| `variables`                                                                                                                                                                                                                                                                                    | Dict[str, *Any*]                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Extracted variables from agent instructions                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |

### Response

**[models.UpdateAgentResponseBody](../../models/updateagentresponsebody.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.UpdateAgentAgentsResponseBody | 404                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## ~~invoke~~

Invokes an agent to perform a task with the provided input message. The agent will process the request using its configured model and tools, maintaining context through memory stores if configured. Supports automatic model fallback on primary model failure, tool execution, knowledge base retrieval, and continuation of previous conversations. Returns a task response that can be used to track execution status and retrieve results.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="InvokeAgent" method="post" path="/v2/agents/{key}/task" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.invoke(key="<key>", message={
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
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                                                                              | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The key or ID of the agent to invoke                                                                                                                                                               |
| `message`                                                                                                                                                                                          | [models.InvokeAgentA2AMessage](../../models/invokeagenta2amessage.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The A2A message to send to the agent (user input or tool results)                                                                                                                                  |
| `task_id`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Optional task ID to continue an existing agent execution. When provided, the agent will continue the conversation from the existing task state. The task must be in an inactive state to continue. |
| `variables`                                                                                                                                                                                        | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional variables for template replacement in system prompt, instructions, and messages                                                                                                           |
| `contact`                                                                                                                                                                                          | [Optional[models.InvokeAgentContact]](../../models/invokeagentcontact.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                 | Information about the contact making the request. If the contact does not exist, it will be created automatically.                                                                                 |
| `thread`                                                                                                                                                                                           | [Optional[models.InvokeAgentThread]](../../models/invokeagentthread.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Thread information to group related requests                                                                                                                                                       |
| `memory`                                                                                                                                                                                           | [Optional[models.InvokeAgentMemory]](../../models/invokeagentmemory.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Memory configuration for the agent execution. Used to associate memory stores with specific entities like users or sessions.                                                                       |
| `metadata`                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional metadata for the agent invocation as key-value pairs that will be included in traces                                                                                                      |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.InvokeAgentA2ATaskResponse](../../models/invokeagenta2ataskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

Retrieves a comprehensive list of agents configured in your workspace. Supports pagination for large datasets and returns agents sorted by creation date (newest first). Each agent in the response includes its complete configuration: model settings with fallback options, instructions, tools, knowledge bases, memory stores, and execution parameters. Use pagination parameters to efficiently navigate through large collections of agents.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListAgents" method="get" path="/v2/agents/" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.list(limit=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 200. When not provided, returns all agents without pagination.                                                                                                                                                                                           |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListAgentsResponseBody](../../models/listagentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~run~~

Executes an agent using inline configuration or references an existing agent. Supports dynamic agent creation where the system automatically manages agent versioning - reusing existing agents with matching configurations or creating new versions when configurations differ. Ideal for programmatic agent execution with flexible configuration management. The agent processes messages in A2A format with support for memory context, tool execution, and automatic model fallback on failure.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="RunAgent" method="post" path="/v2/agents/run" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.run(request={
        "key": "<key>",
        "model": "F-150",
        "role": "<value>",
        "instructions": "<value>",
        "message": {
            "role": "tool",
            "parts": [
                {
                    "kind": "file",
                    "file": {
                        "uri": "https://front-pecan.info",
                    },
                },
            ],
        },
        "contact": {
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
        },
        "thread": {
            "id": "thread_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "tags": [
                "customer-support",
                "priority-high",
            ],
        },
        "path": "Default",
        "knowledge_bases": [
            {
                "knowledge_id": "customer-knowledge-base",
            },
        ],
        "settings": {},
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RunAgentRequestBody](../../models/runagentrequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RunAgentA2ATaskResponse](../../models/runagenta2ataskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## ~~stream_run~~

Dynamically configures and executes an agent while streaming the interaction in real-time via Server-Sent Events (SSE). Intelligently manages agent versioning by reusing existing agents with matching configurations or creating new versions when configurations differ. Combines the flexibility of inline configuration with real-time streaming, making it ideal for dynamic agent interactions with live feedback. The stream provides continuous updates including message chunks, tool executions, and status changes until completion or timeout.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="StreamRunAgent" method="post" path="/v2/agents/stream-run" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.stream_run(request={
        "key": "<key>",
        "model": "Alpine",
        "role": "<value>",
        "instructions": "<value>",
        "message": {
            "role": "user",
            "parts": [
                {
                    "kind": "file",
                    "file": {
                        "uri": "https://jumbo-zebra.info/",
                    },
                },
            ],
        },
        "contact": {
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
        },
        "thread": {
            "id": "thread_01ARZ3NDEKTSV4RRFFQ69G5FAV",
            "tags": [
                "customer-support",
                "priority-high",
            ],
        },
        "path": "Default",
        "knowledge_bases": [
            {
                "knowledge_id": "customer-knowledge-base",
            },
        ],
        "settings": {},
    })

    assert res is not None

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.StreamRunAgentRequestBody](../../models/streamrunagentrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[Union[eventstreaming.EventStream[models.StreamRunAgentResponseBody], eventstreaming.EventStreamAsync[models.StreamRunAgentResponseBody]]](../../models/.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.StreamRunAgentAgentsResponseBody | 404                                     | application/json                        |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## ~~stream~~

Executes an agent and streams the interaction in real-time using Server-Sent Events (SSE). Provides live updates as the agent processes the request, including message chunks, tool calls, and execution status. Perfect for building responsive chat interfaces and monitoring agent progress. The stream continues until the agent completes its task, encounters an error, or reaches the configured timeout (default 30 minutes, configurable 1-3600 seconds).

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="StreamAgent" method="post" path="/v2/agents/{key}/stream-task" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.stream(key="<key>", message={
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
    })

    assert res is not None

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                                                                              | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The key or ID of the agent to invoke                                                                                                                                                               |
| `message`                                                                                                                                                                                          | [models.StreamAgentA2AMessage](../../models/streamagenta2amessage.md)                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The A2A message to send to the agent (user input or tool results)                                                                                                                                  |
| `task_id`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Optional task ID to continue an existing agent execution. When provided, the agent will continue the conversation from the existing task state. The task must be in an inactive state to continue. |
| `variables`                                                                                                                                                                                        | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional variables for template replacement in system prompt, instructions, and messages                                                                                                           |
| `contact`                                                                                                                                                                                          | [Optional[models.StreamAgentContact]](../../models/streamagentcontact.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                 | Information about the contact making the request. If the contact does not exist, it will be created automatically.                                                                                 |
| `thread`                                                                                                                                                                                           | [Optional[models.StreamAgentThread]](../../models/streamagentthread.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Thread information to group related requests                                                                                                                                                       |
| `memory`                                                                                                                                                                                           | [Optional[models.StreamAgentMemory]](../../models/streamagentmemory.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Memory configuration for the agent execution. Used to associate memory stores with specific entities like users or sessions.                                                                       |
| `metadata`                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional metadata for the agent invocation as key-value pairs that will be included in traces                                                                                                      |
| `stream_timeout_seconds`                                                                                                                                                                           | *Optional[float]*                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                 | Stream timeout in seconds (1-3600). Default: 1800 (30 minutes)                                                                                                                                     |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[Union[eventstreaming.EventStream[models.StreamAgentResponseBody], eventstreaming.EventStreamAsync[models.StreamAgentResponseBody]]](../../models/.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.StreamAgentAgentsResponseBody | 404                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |