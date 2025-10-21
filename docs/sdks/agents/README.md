# Agents
(*agents*)

## Overview

### Available Operations

* [retrieve_task](#retrieve_task) - Retrieve a specific agent task
* [create](#create) - Create a new agent
* [list](#list) - List all agents
* [delete](#delete) - Delete an agent
* [retrieve](#retrieve) - Get an agent
* [update](#update) - Update an agent
* [invoke](#invoke) - Invoke an agent
* [list_tasks](#list_tasks) - List all tasks for an agent
* [run](#run) - Run an agent
* [stream_run](#stream_run) - Run and stream agent execution
* [stream](#stream) - Stream agent execution events
* [list_actions](#list_actions) - List all actions
* [retrieve_action](#retrieve_action) - Retrieve an action executed by an agent task.

## retrieve_task

Retrieves detailed information about a specific task for a given agent, including execution status and results.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAgentTask" method="get" path="/v2/agents/{agent_key}/tasks/{task_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.retrieve_task(agent_key="<value>", task_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAgentTaskResponseBody](../../models/getagenttaskresponsebody.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.GetAgentTaskAgentsResponseBody | 404                                   | application/json                      |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## create

Creates a new AI agent with specified configuration. Agents can be configured with a primary model and an optional fallback model that will be used automatically if the primary model fails.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAgent" method="post" path="/v2/agents/" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.create(request={
        "path": "Default",
        "key": "<key>",
        "role": "<value>",
        "description": "neatly unless refine aside platter alarmed shampoo shakily yippee",
        "instructions": "<value>",
        "model": "Camaro",
        "settings": {
            "tools": [
                {
                    "type": "http",
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

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.CreateAgentRequestBody](../../models/createagentrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CreateAgentResponseBody](../../models/createagentresponsebody.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.CreateAgentAgentsResponseBody | 409                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## list

Retrieves a paginated list of all agents in your workspace. Each agent includes its configuration, primary model, and optional fallback model settings.

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
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListAgentsResponseBody](../../models/listagentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes an agent and all its configuration, including primary and fallback model settings.

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

Retrieves a single agent by its unique key, including its full configuration with primary and fallback model settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAgent" method="get" path="/v2/agents/{agent_key}" -->
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

**[models.GetAgentResponseBody](../../models/getagentresponsebody.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GetAgentAgentsResponseBody | 404                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

Updates an existing agent's configuration. You can update various fields including the model configuration and fallback model settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAgent" method="patch" path="/v2/agents/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.update(agent_key="<value>", path="Default", knowledge_bases=[
        {
            "knowledge_id": "customer-knowledge-base",
        },
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | The unique key of the agent to update                                                                                                                                                                                                           |                                                                                                                                                                                                                                                 |
| `key`                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `project_id`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `role`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `description`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `instructions`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `system_prompt`                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | A custom system prompt template for the agent. If omitted, the default template is used.                                                                                                                                                        |                                                                                                                                                                                                                                                 |
| `model`                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The primary language model that powers the agent (e.g., "anthropic/claude-3-sonnet-20240229")                                                                                                                                                   |                                                                                                                                                                                                                                                 |
| `fallback_models`                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                              | Optional array of fallback model IDs to use when the primary model fails. Models are tried in order. All models must support tool calling capabilities.                                                                                         |                                                                                                                                                                                                                                                 |
| `settings`                                                                                                                                                                                                                                      | [Optional[models.UpdateAgentSettings]](../../models/updateagentsettings.md)                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `path`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists. | Default                                                                                                                                                                                                                                         |
| `memory_stores`                                                                                                                                                                                                                                 | List[*str*]                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `knowledge_bases`                                                                                                                                                                                                                               | List[[models.UpdateAgentKnowledgeBases](../../models/updateagentknowledgebases.md)]                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `team_of_agents`                                                                                                                                                                                                                                | List[[models.UpdateAgentTeamOfAgents](../../models/updateagentteamofagents.md)]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The agents that are accessible to this orchestrator. The main agent can hand off to these agents to perform tasks.                                                                                                                              |                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.UpdateAgentResponseBody](../../models/updateagentresponsebody.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.UpdateAgentAgentsResponseBody | 404                                  | application/json                     |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## invoke

Executes an existing agent with the provided input. The agent uses its pre-configured primary model and will automatically fall back to its configured fallback model if the primary model fails. Fallback models are configured at the agent level, not during execution.

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
| `message`                                                                                                                                                                                          | [models.Message](../../models/message.md)                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
| `task_id`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Optional task ID to continue an existing agent execution. When provided, the agent will continue the conversation from the existing task state. The task must be in an inactive state to continue. |
| `variables`                                                                                                                                                                                        | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional variables for template replacement in system prompt, instructions, and messages                                                                                                           |
| `contact`                                                                                                                                                                                          | [Optional[models.Contact]](../../models/contact.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                 | Information about the contact making the request. If the contact does not exist, it will be created automatically.                                                                                 |
| `thread`                                                                                                                                                                                           | [Optional[models.InvokeAgentThread]](../../models/invokeagentthread.md)                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                 | Thread information to group related requests                                                                                                                                                       |
| `memory`                                                                                                                                                                                           | [Optional[models.Memory]](../../models/memory.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                 | Memory configuration for the agent execution. Used to associate memory stores with specific entities like users or sessions.                                                                       |
| `metadata`                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Optional metadata for the agent invocation as key-value pairs that will be included in traces                                                                                                      |
| `retries`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                |

### Response

**[models.InvokeAgentResponseBody](../../models/invokeagentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_tasks

Retrieves a paginated list of all tasks associated with a specific agent, optionally filtered by status.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListAgentTasks" method="get" path="/v2/agents/{agent_key}/tasks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.list_tasks(agent_key="<value>", limit=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | The unique key of the agent                                                                                                                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `status`                                                                                                                                                                                                                                                                                                                                | [Optional[models.Status]](../../models/status.md)                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Comma-separated list of task statuses to filter by. Available values: inactive, approval_required, in_progress, errored                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListAgentTasksResponseBody](../../models/listagenttasksresponsebody.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.ListAgentTasksAgentsResponseBody | 404                                     | application/json                        |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## run

Executes an agent with the provided configuration using A2A message format. If the agent already exists with the same configuration, it will be reused. If the configuration differs, a new version is created. The fallback model is configured at the agent level and will be used automatically if the primary model fails during execution.

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
                    "kind": "text",
                    "text": "<value>",
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
        "settings": {
            "tools": [
                {
                    "type": "write_memory_store",
                    "requires_approval": False,
                },
            ],
        },
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

**[models.RunAgentResponseBody](../../models/runagentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## stream_run

Creates or updates an agent with the provided configuration, then streams execution events via Server-Sent Events (SSE). If the agent already exists with the same configuration, it will be reused. If the configuration differs, a new version is created. The stream will continue until the agent completes, errors, or reaches the configured timeout.

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
        "settings": {
            "tools": [
                {
                    "type": "write_memory_store",
                    "requires_approval": False,
                },
            ],
        },
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

## stream

Executes an agent and streams events via Server-Sent Events (SSE). The stream will continue until the agent completes, errors, or reaches the configured timeout.

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
| `message`                                                                                                                                                                                          | [models.StreamAgentMessage](../../models/streamagentmessage.md)                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                 | N/A                                                                                                                                                                                                |
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

## list_actions

List all actions

### Example Usage

<!-- UsageSnippet language="python" operationID="ListActions" method="get" path="/v2/agents/{agent_key}/tasks/{task_id}/actions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.list_actions(agent_key="<value>", task_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListActionsResponseBody](../../models/listactionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_action

Retrieve an action executed by an agent task.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveAction" method="get" path="/v2/agents/{agent_key}/tasks/{task_id}/actions/{action_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.retrieve_action(agent_key="<value>", task_id="<id>", action_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique key of the agent                                         |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The unique id of the task                                           |
| `action_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique id of the action                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveActionResponseBody](../../models/retrieveactionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |