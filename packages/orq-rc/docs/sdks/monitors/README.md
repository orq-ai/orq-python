# Monitors

## Overview

### Available Operations

* [list](#list) - List monitors
* [create](#create) - Create a monitor
* [list_presets](#list_presets) - List monitor presets
* [get](#get) - Retrieve a monitor
* [delete](#delete) - Delete a monitor
* [update](#update) - Update a monitor

## list

Returns the monitors visible to the caller, newest first. A human filtering by project sees that project's monitors plus workspace-wide monitors. A project-scoped API key sees only monitors in its strict project scope. Use `starting_after` or `ending_before` to page.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorList" method="get" path="/v2/monitors" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                        | *Optional[int]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | Page size, 1-200. Unset uses the server default (25).                                                                                          |
| `starting_after`                                                                                                                               | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | Cursor for forward pagination. Set to the `monitor_id` of the last<br/> item from the previous page.                                           |
| `ending_before`                                                                                                                                | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | Cursor for backward pagination. Set to the `monitor_id` of the<br/> first item from the previous page.                                         |
| `project_id`                                                                                                                                   | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | Restrict results to one project. Human callers also see workspace-wide<br/> monitors; a project-scoped API key sees only its strict project scope. |
| `search`                                                                                                                                       | *Optional[str]*                                                                                                                                | :heavy_minus_sign:                                                                                                                             | Case-insensitive substring match on display name and description.                                                                              |
| `workspace_wide`                                                                                                                               | *Optional[bool]*                                                                                                                               | :heavy_minus_sign:                                                                                                                             | Restrict results by scope. Set true for workspace-wide monitors only,<br/> false for project-scoped monitors only; omit to return both.        |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[models.ListMonitorsResponse](../../models/listmonitorsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a monitor (custom observability dashboard) in the workspace. Set `project_id` to scope the monitor to a project; omit it to create a workspace-wide monitor, which requires admin access.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorCreate" method="post" path="/v2/monitors" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.create(display_name="Ava41")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `display_name`                                                                                         | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Workspace-unique display name.                                                                         |
| `description`                                                                                          | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Short human-readable summary of what the monitor tracks.                                               |
| `project_id`                                                                                           | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Project that should own the monitor. Omit to create a<br/> workspace-wide monitor (requires admin access). |
| `widgets`                                                                                              | List[[models.MonitorWidget](../../models/monitorwidget.md)]                                            | :heavy_minus_sign:                                                                                     | Widgets to render on the monitor. Empty creates a valid blank monitor.                                 |
| `default_range`                                                                                        | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Default relative time range applied when the monitor opens.                                            |
| `preset_key`                                                                                           | [Optional[models.PresetKey]](../../models/presetkey.md)                                                | :heavy_minus_sign:                                                                                     | Known preset used to create the monitor. Empty when built from scratch.                                |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[models.CreateMonitorResponse](../../models/createmonitorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## list_presets

Returns the built-in monitor templates (preset dashboards and preset widgets). Presets are defined by the platform and versioned with it; create a monitor from a preset by copying its widgets into a create request and stamping `preset_key`.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorListPresets" method="get" path="/v2/monitors/presets" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.list_presets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMonitorPresetsResponse](../../models/listmonitorpresetsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a monitor by ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorGet" method="get" path="/v2/monitors/{monitor_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.get(monitor_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `monitor_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Monitor ID to retrieve.                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetMonitorResponse](../../models/getmonitorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a monitor. Widgets are stored inline, so no other resources are affected.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorDelete" method="delete" path="/v2/monitors/{monitor_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.delete(monitor_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `monitor_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Monitor ID to delete.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteMonitorResponse](../../models/deletemonitorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates monitor metadata and widgets. With `update_mask`, listed paths are replaced and `widgets` may be explicitly cleared. Without `update_mask`, legacy behavior is preserved: a non-empty `widgets` array replaces the set and an empty or omitted array keeps it. `project_id` is immutable.

### Example Usage

<!-- UsageSnippet language="python" operationID="MonitorUpdate" method="patch" path="/v2/monitors/{monitor_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY"),
) as orq:

    res = orq.monitors.update(monitor_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                  | Description                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `monitor_id`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                        | Monitor ID to update.                                                                                                                                                                                                     |
| `display_name`                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | New workspace-unique display name. Omit to keep the current name.                                                                                                                                                         |
| `description`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | New description. Omit to keep the current description.                                                                                                                                                                    |
| `widgets`                                                                                                                                                                                                                 | List[[models.MonitorWidget](../../models/monitorwidget.md)]                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                        | Replacement widget set. When update_mask contains `widgets`, this value<br/> replaces the full set and may be empty. Without update_mask, a non-empty<br/> array replaces all widgets while an empty or omitted array keeps them. |
| `default_range`                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | New default relative time range. Omit to keep the current value unless<br/> update_mask contains `default_range`, which clears it.                                                                                        |
| `update_mask`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                        | Optional explicit update presence. Listed paths are replaced; omitting<br/> the mask preserves the legacy partial-update behavior.                                                                                        |
| `retries`                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                       |

### Response

**[models.UpdateMonitorResponse](../../models/updatemonitorresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.ErrorResponse   | 401                    | application/json       |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |