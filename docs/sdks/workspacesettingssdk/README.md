# WorkspaceSettings

## Overview

### Available Operations

* [get](#get) - Retrieve workspace settings
* [update](#update) - Update workspace settings

## get

Returns the current settings for the authenticated workspace: its read-only key/slug, display name, the enforce-enabled-models flag, and the workspace-default PII redaction plugin configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSettingsGet" method="get" path="/v2/workspace-settings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_settings.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWorkspaceSettingsResponse](../../models/getworkspacesettingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Partially updates workspace settings. Every field is optional; an omitted field is left unchanged. Provide `display_name` to rename the workspace, `enforce_enabled_models` to toggle model enforcement, or `pii_redaction` to replace the workspace-default PII redaction plugin configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkspaceSettingsUpdate" method="patch" path="/v2/workspace-settings" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.workspace_settings.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | New workspace display name. Omit to keep the current name.                                                                                                                                    |
| `enforce_enabled_models`                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | New value for the enforce-enabled-models flag. Omit to keep the current<br/> value.                                                                                                           |
| `pii_redaction`                                                                                                                                                                               | [Optional[models.PiiRedaction]](../../models/piiredaction.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                            | Replacement workspace-default PII redaction configuration. Omit to leave<br/> the current PII redaction configuration unchanged; when present it fully<br/> replaces the stored pii_redaction object. |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |

### Response

**[models.UpdateWorkspaceSettingsResponse](../../models/updateworkspacesettingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |