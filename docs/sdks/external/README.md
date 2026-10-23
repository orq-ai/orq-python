# Agents.External

## Overview

### Available Operations

* [list](#list) - List external agents
* [create](#create) - Create external agent
* [retrieve](#retrieve) - Retrieve external agent
* [delete](#delete) - Delete external agent
* [update](#update) - Update external agent
* [refresh_card](#refresh_card) - Refresh external agent card
* [test_connection](#test_connection) - Test external agent connection

## list

Returns the external A2A agents visible to the caller, ordered newest first.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentList" method="get" path="/v2/agents/external" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListExternalAgentsResponse](../../models/listexternalagentsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Registers an external A2A agent after securely fetching and validating its agent card.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentCreate" method="post" path="/v2/agents/external" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.create(key="<key>", display_name="Jabari_Ernser29", path="/lost+found", agent_url="https://responsible-disappointment.net/")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `key`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `display_name`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `path`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `agent_url`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `description`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `project_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `card_url`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `headers`                                                                    | Dict[str, [models.ExternalAgentHeader](../../models/externalagentheader.md)] | :heavy_minus_sign:                                                           | N/A                                                                          |
| `protocol_version`                                                           | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `preferred_transport`                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.CreateExternalAgentResponse](../../models/createexternalagentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## retrieve

Retrieves a registered external A2A agent by key or ID. Encrypted header values are always masked.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentGet" method="get" path="/v2/agents/external/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.retrieve(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetExternalAgentResponse](../../models/getexternalagentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes a registered external A2A agent.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentDelete" method="delete" path="/v2/agents/external/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.delete(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteExternalAgentResponse](../../models/deleteexternalagentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates mutable registry and A2A connection fields. An empty encrypted header value preserves the stored secret.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentUpdate" method="patch" path="/v2/agents/external/{agent_key}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.update(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `agent_key`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `display_name`                                                               | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `description`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `path`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `project_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `agent_url`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `card_url`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `headers`                                                                    | Dict[str, [models.ExternalAgentHeader](../../models/externalagentheader.md)] | :heavy_minus_sign:                                                           | N/A                                                                          |
| `protocol_version`                                                           | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `preferred_transport`                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `clear_headers`                                                              | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.UpdateExternalAgentResponse](../../models/updateexternalagentresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## refresh_card

Securely fetches the current agent card and replaces the cached card metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentRefreshCard" method="post" path="/v2/agents/external/{agent_key}:refreshCard" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.refresh_card(agent_key="<value>", refresh_external_agent_card_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `agent_key`                                                                               | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `refresh_external_agent_card_request`                                                     | [models.RefreshExternalAgentCardRequest](../../models/refreshexternalagentcardrequest.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.RefreshExternalAgentCardResponse](../../models/refreshexternalagentcardresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## test_connection

Validates the stored connection configuration and securely fetches the external agent card without persisting changes.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExternalAgentTestConnection" method="post" path="/v2/agents/external/{agent_key}:testConnection" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.agents.external.test_connection(agent_key="<value>", test_external_agent_connection_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                     | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `test_external_agent_connection_request`                                                        | [models.TestExternalAgentConnectionRequest](../../models/testexternalagentconnectionrequest.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.TestExternalAgentConnectionResponse](../../models/testexternalagentconnectionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |