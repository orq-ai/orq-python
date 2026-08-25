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

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a schedule that runs the agent on a cron cadence. Only `cron` is accepted, as a 6-field expression firing at most once per hour: hourly `0 0 * * * *`, daily `0 0 9 * * *`, or weekly `0 0 9 * * 1`.

### Example Usage: daily_cron

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="daily_cron" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", display_name="Daily morning briefing", expression="0 0 9 * * *", payload={
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
### Example Usage: hourly_cron

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="hourly_cron" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", display_name="Hourly ticket summary", expression="0 0 * * * *", payload={
        "input": "Summarize new tickets from the last hour",
    }, type_="cron")

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

    res = orq.schedules.create(agent_key="<value>", display_name="Bernie56", expression="@every 1h", payload={
        "input": "Summarize new tickets from the last hour",
    })

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

    res = orq.schedules.create(agent_key="<value>", display_name="Earlene.Hayes", expression="@at 2026-05-01T09:00:00Z", payload={
        "input": "Check in on ticket TICKET-123 and post a status update.",
    })

    # Handle response
    print(res)

```
### Example Usage: weekly_cron

<!-- UsageSnippet language="python" operationID="create-agent-schedule" method="post" path="/v3/agents/{agent_key}/schedules" example="weekly_cron" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.create(agent_key="<value>", display_name="Weekly ticket status update", expression="0 0 9 * * 1", payload={
        "input": "Post the weekly status update for TICKET-123.",
    }, type_="cron")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                               | The unique routing key of the agent the schedule belongs to.                                                                                                                                                                                                                                                                                                                     |
| `display_name`                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                               | Human-readable name of the schedule.                                                                                                                                                                                                                                                                                                                                             |
| `expression`                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                               | 6-field cron expression (sec min hour dom month dow). Seconds and minutes must be 0, day-of-month and month must be '*'. Hour and weekday must each be a single integer or '*'; ranges, lists, steps, and named days are rejected. Accepted shapes: hourly '0 0 * * * *', daily '0 0 9 * * *' (hour 0-23), weekly '0 0 9 * * 1' (weekday 0-6). Minimum firing cadence is 1 hour. |
| `payload`                                                                                                                                                                                                                                                                                                                                                                        | [models.PublicSchedulePayload](../../models/publicschedulepayload.md)                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                                                                                                                                              |
| `type`                                                                                                                                                                                                                                                                                                                                                                           | [models.CreateAgentScheduleType](../../models/createagentscheduletype.md)                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                               | Schedule type. Only cron is accepted; the expression must be a 6-field cron expression firing at most once per hour.                                                                                                                                                                                                                                                             |
| `agent_tag`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                               | Pin this schedule to a specific agent version. Omit to always use the active version.                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                              |

### Response

**[models.CreateAgentScheduleResponseBody](../../models/createagentscheduleresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.CreateAgentScheduleSchedulesResponseBody         | 400                                                     | application/json                                        |
| models.CreateAgentScheduleSchedulesResponseResponseBody | 404                                                     | application/json                                        |
| models.APIDefaultError                                  | 4XX, 5XX                                                | \*/\*                                                   |

## delete

Permanently removes the schedule. It will not run again.

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
| models.APIDefaultError                 | 4XX, 5XX                               | \*/\*                                  |

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
| models.APIDefaultError                            | 4XX, 5XX                                          | \*/\*                                             |

## update

Partially updates a schedule. Any omitted field is left unchanged. Changing `expression` or `type` (or reactivating from inactive) reschedules the next run and bumps `generation`; payload-only and `agent_tag`-only changes leave the firing cadence in place.

### Example Usage: change_cadence

<!-- UsageSnippet language="python" operationID="update-agent-schedule" method="patch" path="/v3/agents/{agent_key}/schedules/{schedule_id}" example="change_cadence" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.update(agent_key="<value>", schedule_id="<id>", expression="0 0 9 * * *")

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
### Example Usage: rename

<!-- UsageSnippet language="python" operationID="update-agent-schedule" method="patch" path="/v3/agents/{agent_key}/schedules/{schedule_id}" example="rename" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.schedules.update(agent_key="<value>", schedule_id="<id>", display_name="Nightly report")

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

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_key`                                                                                                                                 | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | The unique routing key of the agent the schedule belongs to.                                                                                |
| `schedule_id`                                                                                                                               | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | The schedule's ULID, as returned from create.                                                                                               |
| `agent_tag`                                                                                                                                 | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Change the pinned agent version.                                                                                                            |
| `display_name`                                                                                                                              | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Rename the schedule.                                                                                                                        |
| `expression`                                                                                                                                | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Update the schedule expression. Same 6-field cron shapes as create; minimum firing cadence is 1 hour.                                       |
| `is_active`                                                                                                                                 | *Optional[bool]*                                                                                                                            | :heavy_minus_sign:                                                                                                                          | Activate or deactivate the schedule. Deactivating stops future executions; activating schedules future executions using the current values. |
| `payload`                                                                                                                                   | [Optional[models.PublicSchedulePayload]](../../models/publicschedulepayload.md)                                                             | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `type`                                                                                                                                      | [Optional[models.UpdateAgentScheduleType]](../../models/updateagentscheduletype.md)                                                         | :heavy_minus_sign:                                                                                                                          | Change the schedule type. Only cron is accepted. Changing the type or expression reschedules future executions and increments generation.   |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.UpdateAgentScheduleResponseBody](../../models/updateagentscheduleresponsebody.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.UpdateAgentScheduleSchedulesResponseBody         | 400                                                     | application/json                                        |
| models.UpdateAgentScheduleSchedulesResponseResponseBody | 404                                                     | application/json                                        |
| models.APIDefaultError                                  | 4XX, 5XX                                                | \*/\*                                                   |

## trigger

Runs the schedule's payload immediately (approximately 10 seconds after the request). The schedule's regular cadence is unaffected. Inactive schedules return 400.

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
| models.APIDefaultError                                   | 4XX, 5XX                                                 | \*/\*                                                    |