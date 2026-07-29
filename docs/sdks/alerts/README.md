# Alerts

## Overview

### Available Operations

* [list](#list) - List alerts
* [create](#create) - Create an alert
* [get](#get) - Retrieve an alert
* [delete](#delete) - Delete an alert
* [update](#update) - Update an alert
* [check_now](#check_now) - Run an alert check now
* [list_triggers](#list_triggers) - List alert triggers
* [list_trigger_events](#list_trigger_events) - List alert trigger events

## list

Returns the alerts visible to the caller, newest first. Use `starting_after` or `ending_before` to page.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertList" method="get" path="/v2/alerts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `limit`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | Page size, 1-200. Unset uses the server default (25).                                            |
| `starting_after`                                                                                 | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Cursor for forward pagination. Set to the `alert_id` of the last<br/> item from the previous page. |
| `ending_before`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Cursor for backward pagination. Set to the `alert_id` of the first<br/> item from the previous page. |
| `project_id`                                                                                     | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Restrict results to one project.                                                                 |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.ListAlertsResponse](../../models/listalertsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a threshold alert in a project. The alert's query is validated against the Reporting API metric catalogue and the evaluation schedule starts immediately when `enabled` is true. Plan limits apply to the number of alerts and the minimum evaluation interval.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertCreate" method="post" path="/v2/alerts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.create(display_name="Freeman80", project_id="<id>", query={
        "metric": "<value>",
    }, condition={
        "comparator": "gte",
        "threshold": 7213.05,
        "window": "30m",
        "interval": "5m",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `display_name`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | Workspace-unique display name.                                          |
| `project_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | Project that owns the alert. Required.                                  |
| `query`                                                                 | [models.AlertQuery](../../models/alertquery.md)                         | :heavy_check_mark:                                                      | Metric query evaluated on each tick.                                    |
| `condition`                                                             | [models.AlertCondition](../../models/alertcondition.md)                 | :heavy_check_mark:                                                      | Threshold condition applied to the query result.                        |
| `description`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Short human-readable summary of what the alert watches.                 |
| `signal`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | UI signal preset the alert is created from. Defaults to `custom`.       |
| `notifier_ids`                                                          | List[*str*]                                                             | :heavy_minus_sign:                                                      | Notifiers that receive trigger-open and trigger-resolve<br/> notifications. |
| `enabled`                                                               | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Whether the alert starts evaluating immediately. Defaults to true.      |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.CreateAlertResponse](../../models/createalertresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieves an alert by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertGet" method="get" path="/v2/alerts/{alert_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.get(alert_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `alert_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Alert ID to retrieve.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAlertResponse](../../models/getalertresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Permanently deletes an alert together with its trigger history and events, and stops the evaluation schedule.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertDelete" method="delete" path="/v2/alerts/{alert_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.delete(alert_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `alert_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Alert ID to delete.                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAlertResponse](../../models/deletealertresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates alert metadata, query, condition, notifiers, or enabled state. Query and condition changes restart the evaluation schedule; disabling stops it. `project_id` is immutable.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertUpdate" method="patch" path="/v2/alerts/{alert_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.update(alert_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `alert_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Alert ID to update.                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New workspace-unique display name. Omit to keep the current name.   |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New description. Omit to keep the current description.              |
| `signal`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New UI signal preset. Omit to keep the current value.               |
| `query`                                                             | [Optional[models.AlertQuery]](../../models/alertquery.md)           | :heavy_minus_sign:                                                  | Replacement query. Omit to keep the current query.                  |
| `condition`                                                         | [Optional[models.AlertCondition]](../../models/alertcondition.md)   | :heavy_minus_sign:                                                  | Replacement condition. Omit to keep the current condition.          |
| `notifier_ids`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Replacement notifier set. Omit to keep the current notifiers.       |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | New enabled state. Omit to keep the current state.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateAlertResponse](../../models/updatealertresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## check_now

Schedules one immediate evaluation of the alert (delivered within ~10 seconds), independent of its regular interval. The check runs through the normal evaluation pipeline: it records a run, can open or resolve triggers, and fires notifications. The alert must be enabled.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertCheckNow" method="post" path="/v2/alerts/{alert_id}/check" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.check_now(alert_id="<id>", check_alert_now_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `alert_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Alert to evaluate now.                                              |
| `check_alert_now_request`                                           | [models.CheckAlertNowRequest](../../models/checkalertnowrequest.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CheckAlertNowResponse](../../models/checkalertnowresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_triggers

Returns the trigger history of an alert, newest first. A trigger is one breach incident: it opens when the threshold is first crossed and resolves when the value recovers.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertListTriggers" method="get" path="/v2/alerts/{alert_id}/triggers" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.list_triggers(alert_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `alert_id`                                                                                         | *str*                                                                                              | :heavy_check_mark:                                                                                 | Alert whose triggers to list.                                                                      |
| `limit`                                                                                            | *Optional[int]*                                                                                    | :heavy_minus_sign:                                                                                 | Page size, 1-200. Unset uses the server default (25).                                              |
| `starting_after`                                                                                   | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Cursor for forward pagination. Set to the `trigger_id` of the last<br/> item from the previous page. |
| `ending_before`                                                                                    | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Cursor for backward pagination. Set to the `trigger_id` of the<br/> first item from the previous page. |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[models.ListAlertTriggersResponse](../../models/listalerttriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_trigger_events

Returns the evaluation events recorded while a trigger was open, newest first. Each event carries the observed value and, when available, exemplar traces that contributed to the breach.

### Example Usage

<!-- UsageSnippet language="python" operationID="AlertListTriggerEvents" method="get" path="/v2/alerts/{alert_id}/triggers/{trigger_id}/events" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.alerts.list_trigger_events(alert_id="<id>", trigger_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `alert_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Alert the trigger belongs to.                                                                    |
| `trigger_id`                                                                                     | *str*                                                                                            | :heavy_check_mark:                                                                               | Trigger whose events to list.                                                                    |
| `limit`                                                                                          | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | Page size, 1-200. Unset uses the server default (25).                                            |
| `starting_after`                                                                                 | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Cursor for forward pagination. Set to the `event_id` of the last<br/> item from the previous page. |
| `ending_before`                                                                                  | *Optional[str]*                                                                                  | :heavy_minus_sign:                                                                               | Cursor for backward pagination. Set to the `event_id` of the first<br/> item from the previous page. |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.ListAlertTriggerEventsResponse](../../models/listalerttriggereventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |