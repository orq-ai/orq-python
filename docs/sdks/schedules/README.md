# Schedules

## Overview

### Available Operations

* [list](#list) - List schedules
* [create](#create) - Create schedule
* [delete](#delete) - Delete schedule
* [retrieve](#retrieve) - Retrieve schedule
* [update](#update) - Update schedule
* [trigger](#trigger) - Trigger schedule execution

## list

Lists all schedules attached to the specified agent, most recent first.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-agent-schedules" method="get" path="/v3/agents/{agent_key}/schedules" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.list(agent_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique routing key of the agent the schedule belongs to.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListAgentSchedulesResponseBody](../../models/listagentschedulesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a schedule that runs the agent on a recurring or one-off cadence. The minimum firing interval is 1 hour for `cron` and `interval`; `once` schedules are exempt.

### Example Usage: daily_cron

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="daily_cron" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", expression="0 0 9 * * mon-fri", payload={
        "input": "Generate the morning briefing for {{region}}",
        "memory_entity_id": "mem_entity_123",
        "metadata": {
            "run_source": "daily-briefing",
        },
        "variables": {
            "region": "EMEA",
        },
    }, type_="cron", agent_tag="v2")

    # Handle response
    print(res)

```
### Example Usage: hourly_interval

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="hourly_interval" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", expression="@every 1h", payload={
        "input": "Summarize new tickets from the last hour",
    }, type_="interval")

    # Handle response
    print(res)

```
### Example Usage: once_future_at

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="once_future_at" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", expression="@at 2026-05-01T09:00:00Z", payload={
        "input": "Check in on ticket TICKET-123 and post a status update.",
    }, type_="once")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `agent_key`                                                                                                                                                                                | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The unique routing key of the agent the schedule belongs to.                                                                                                                               |
| `expression`                                                                                                                                                                               | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Schedule expression. Examples: cron '0 0 9 * * mon-fri' (9am UTC weekdays), interval '@every 1h', once '@at 2026-05-01T09:00:00Z'. Minimum firing cadence is 1 hour for cron and interval. |
| `payload`                                                                                                                                                                                  | [models.PublicSchedulePayload](../../models/publicschedulepayload.md)                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | N/A                                                                                                                                                                                        |
| `type`                                                                                                                                                                                     | [models.CreateAgentScheduleType](../../models/createagentscheduletype.md)                                                                                                                  | :heavy_check_mark:                                                                                                                                                                         | Schedule type. cron uses 6-field cron expressions; interval uses @every <duration>; once uses @at <RFC3339-UTC>.                                                                           |
| `agent_tag`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | Pin this schedule to a specific agent version. Omit to always use the active version.                                                                                                      |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[models.CreateAgentScheduleResponseBody](../../models/createagentscheduleresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.CreateAgentScheduleSchedulesResponseBody         | 400                                                     | application/json                                        |
| models.CreateAgentScheduleSchedulesResponseResponseBody | 404                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## delete

Permanently removes a schedule from NATS, Mongo, and the Redis cache.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-agent-schedule" method="delete" path="/v3/agents/{agent_key}/schedules/{schedule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.schedules.delete(agent_key="<value>", schedule_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique routing key of the agent the schedule belongs to.        |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The schedule's ULID, as returned from create.                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.DeleteAgentScheduleResponseBody | 404                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Retrieves a single schedule by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="retrieve-agent-schedule" method="get" path="/v3/agents/{agent_key}/schedules/{schedule_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.retrieve(agent_key="<value>", schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique routing key of the agent the schedule belongs to.        |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The schedule's ULID, as returned from create.                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveAgentScheduleResponseBody](../../models/retrieveagentscheduleresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.RetrieveAgentScheduleSchedulesResponseBody | 404                                               | application/json                                  |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## update

Partially updates a schedule. Any omitted field is left unchanged. Changing `expression` or `type` (or reactivating from inactive) re-publishes the NATS schedule and bumps `generation`; payload-only and `agent_tag`-only changes leave the firing cadence in place.

### Example Usage: change_cadence

<!-- UsageSnippet language="python" operationID="update-agent-schedule" method="patch" path="/v3/agents/{agent_key}/schedules/{schedule_id}" example="change_cadence" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.update(agent_key="<value>", schedule_id="<id>", expression="@every 6h")

    # Handle response
    print(res)

```
### Example Usage: deactivate

<!-- UsageSnippet language="python" operationID="update-agent-schedule" method="patch" path="/v3/agents/{agent_key}/schedules/{schedule_id}" example="deactivate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.update(agent_key="<value>", schedule_id="<id>", is_active=False)

    # Handle response
    print(res)

```
### Example Usage: update_payload

<!-- UsageSnippet language="python" operationID="update-agent-schedule" method="patch" path="/v3/agents/{agent_key}/schedules/{schedule_id}" example="update_payload" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.update(agent_key="<value>", schedule_id="<id>", payload={
        "input": "Updated input for the next run",
        "variables": {
            "region": "APAC",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                            | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The unique routing key of the agent the schedule belongs to.                                                           |
| `schedule_id`                                                                                                          | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | The schedule's ULID, as returned from create.                                                                          |
| `agent_tag`                                                                                                            | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Change the pinned agent version.                                                                                       |
| `expression`                                                                                                           | *Optional[str]*                                                                                                        | :heavy_minus_sign:                                                                                                     | Update the schedule expression. Minimum firing cadence is 1 hour for cron and interval.                                |
| `is_active`                                                                                                            | *Optional[bool]*                                                                                                       | :heavy_minus_sign:                                                                                                     | Activate or deactivate the schedule. Deactivating removes the NATS entry; activating re-publishes with current values. |
| `payload`                                                                                                              | [Optional[models.PublicSchedulePayload]](../../models/publicschedulepayload.md)                                        | :heavy_minus_sign:                                                                                                     | N/A                                                                                                                    |
| `type`                                                                                                                 | [Optional[models.UpdateAgentScheduleType]](../../models/updateagentscheduletype.md)                                    | :heavy_minus_sign:                                                                                                     | Change the schedule type. Changing type or expression resets the NATS schedule and bumps generation.                   |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[models.UpdateAgentScheduleResponseBody](../../models/updateagentscheduleresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.UpdateAgentScheduleSchedulesResponseBody         | 400                                                     | application/json                                        |
| models.UpdateAgentScheduleSchedulesResponseResponseBody | 404                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## trigger

Runs the schedule's payload immediately (≈10 seconds after the request, to stay above the NATS scheduler's minimum deliver-at margin). The schedule's regular cadence is unaffected. Inactive schedules return 400.

### Example Usage

<!-- UsageSnippet language="python" operationID="trigger-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules/{schedule_id}/execution" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.trigger(agent_key="<value>", schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique routing key of the agent the schedule belongs to.        |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The schedule's ULID, as returned from create.                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerAgentScheduleResponseBody](../../models/triggeragentscheduleresponsebody.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.TriggerAgentScheduleSchedulesResponseBody         | 400                                                      | application/json                                         |
| models.TriggerAgentScheduleSchedulesResponseResponseBody | 404                                                      | application/json                                         |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |