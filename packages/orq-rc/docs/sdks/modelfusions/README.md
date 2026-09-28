# ModelFusions

## Overview

### Available Operations

* [list](#list) - List Model Fusions
* [create](#create) - Create a Model Fusion
* [get](#get) - Retrieve a Model Fusion
* [update](#update) - Replace a Model Fusion configuration
* [delete](#delete) - Delete a Model Fusion
* [set_enabled](#set_enabled) - Enable or disable a Model Fusion

## list

Returns Model Fusions in the caller's workspace, ordered newest first. Supports cursor pagination, key search, preset filtering, and enabled-state filtering.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionList" method="get" path="/v3/model-fusions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `starting_after`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ending_before`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `preset`                                                            | List[[models.ModelFusionPreset](../../models/modelfusionpreset.md)] | :heavy_minus_sign:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListModelFusionsResponse](../../models/listmodelfusionsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a workspace Model Fusion virtual model. The key becomes the stable model identifier used by gateway requests.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionCreate" method="post" path="/v3/model-fusions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.create(key="<key>", panel_models=[], judge_model="<value>", synthesis_mode="MODEL_FUSION_SYNTHESIS_MODE_JUDGE_WRITES_FINAL", preset="MODEL_FUSION_PRESET_UNSPECIFIED")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `key`                                                                                          | *str*                                                                                          | :heavy_check_mark:                                                                             | Required. Stable lowercase key containing letters, numbers, and hyphens.                       |
| `panel_models`                                                                                 | List[*str*]                                                                                    | :heavy_check_mark:                                                                             | Required. One to eight distinct chat/text model references in provider/model format.           |
| `judge_model`                                                                                  | *str*                                                                                          | :heavy_check_mark:                                                                             | Required. Model reference used for strict structured judge output.                             |
| `synthesis_mode`                                                                               | [models.ModelFusionSynthesisMode](../../models/modelfusionsynthesismode.md)                    | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `preset`                                                                                       | [models.ModelFusionPreset](../../models/modelfusionpreset.md)                                  | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `orchestrator_model`                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | Required for analysis mode and invalid for judge_writes_final mode.                            |
| `web_tools`                                                                                    | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Optional. Defaults to true.                                                                    |
| `max_tool_calls`                                                                               | *Optional[int]*                                                                                | :heavy_minus_sign:                                                                             | Optional. Defaults to 8 and must be between 0 and 20. Zero disables Fusion-managed tool calls. |
| `feed_raw_to_synth`                                                                            | *Optional[bool]*                                                                               | :heavy_minus_sign:                                                                             | Optional. Defaults to true.                                                                    |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.CreateModelFusionResponse](../../models/createmodelfusionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a Model Fusion by ID within the caller's workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionGet" method="get" path="/v3/model-fusions/{model_fusion_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.get(model_fusion_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_fusion_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetModelFusionResponse](../../models/getmodelfusionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Replaces the complete Fusion configuration. The key is immutable.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionUpdate" method="put" path="/v3/model-fusions/{model_fusion_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.update(model_fusion_id="<id>", panel_models=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], judge_model="<value>", synthesis_mode="MODEL_FUSION_SYNTHESIS_MODE_ANALYSIS", preset="MODEL_FUSION_PRESET_QUALITY", web_tools=True, max_tool_calls=769936, feed_raw_to_synth=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `model_fusion_id`                                                            | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `panel_models`                                                               | List[*str*]                                                                  | :heavy_check_mark:                                                           | N/A                                                                          |
| `judge_model`                                                                | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `synthesis_mode`                                                             | [models.ModelFusionSynthesisMode](../../models/modelfusionsynthesismode.md)  | :heavy_check_mark:                                                           | N/A                                                                          |
| `preset`                                                                     | [models.ModelFusionPreset](../../models/modelfusionpreset.md)                | :heavy_check_mark:                                                           | N/A                                                                          |
| `web_tools`                                                                  | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `max_tool_calls`                                                             | *int*                                                                        | :heavy_check_mark:                                                           | Required. Must be between 0 and 20. Zero disables Fusion-managed tool calls. |
| `feed_raw_to_synth`                                                          | *bool*                                                                       | :heavy_check_mark:                                                           | N/A                                                                          |
| `orchestrator_model`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Required for analysis mode and omitted for judge_writes_final mode.          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.UpdateModelFusionResponse](../../models/updatemodelfusionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently deletes a Model Fusion and removes its gateway model configuration.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionDelete" method="delete" path="/v3/model-fusions/{model_fusion_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.delete(model_fusion_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_fusion_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteModelFusionResponse](../../models/deletemodelfusionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## set_enabled

Controls whether a Model Fusion is available to gateway requests in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelFusionSetEnabled" method="post" path="/v3/model-fusions/{model_fusion_id}/enabled" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.model_fusions.set_enabled(model_fusion_id="<id>", enabled=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_fusion_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetModelFusionEnabledResponse](../../models/setmodelfusionenabledresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |