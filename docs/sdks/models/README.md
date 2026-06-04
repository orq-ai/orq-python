# Models

## Overview

### Available Operations

* [create](#create) - Create custom model
* [create_autorouter](#create_autorouter) - Create autorouter custom model
* [update_autorouter](#update_autorouter) - Update autorouter custom model
* [create_aws_bedrock](#create_aws_bedrock) - Create AWS Bedrock custom model
* [validate_aws_bedrock](#validate_aws_bedrock) - Validate AWS Bedrock inference profile
* [update_aws_bedrock](#update_aws_bedrock) - Update AWS Bedrock custom model
* [azure_foundry_deployments](#azure_foundry_deployments) - List Azure Foundry deployments under a resource
* [import_litellm](#import_litellm) - Import models from LiteLLM
* [list_litellm](#list_litellm) - List models from configured LiteLLM instance
* [create_openai_like](#create_openai_like) - Create OpenAI-compatible custom model
* [update_openai_like](#update_openai_like) - Update OpenAI-compatible custom model
* [validate](#validate) - Validate model endpoint
* [create_vertex](#create_vertex) - Create Vertex AI custom model
* [delete](#delete) - Delete custom model
* [update](#update) - Update custom model
* [enable](#enable) - Enable model for workspace
* [disable](#disable) - Disable model for workspace
* [list](#list) - List models

## create

Creates a new custom model for the workspace. Provider credentials in the configuration are encrypted using the workspace encryption key before being persisted.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCreate" method="post" path="/v2/models" -->
```python
import orq_ai_sdk
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.create(configuration={

    }, display_name="Albert_Emmerich25", has_functions=False, id="<id>", input_cost=2127.52, metadata=orq_ai_sdk.ModelMetadata(
        is_private=False,
    ), model_developer="<value>", model_family="<value>", model_id="<id>", model_type="<value>", output_cost=5446, parameters=[
        {
            "config": {

            },
            "name": "<value>",
            "parameter": "<value>",
            "parameter_type": "<value>",
        },
    ], provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `configuration`                                                           | Dict[str, *Any*]                                                          | :heavy_check_mark:                                                        | N/A                                                                       |
| `display_name`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `has_functions`                                                           | *bool*                                                                    | :heavy_check_mark:                                                        | N/A                                                                       |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `input_cost`                                                              | *float*                                                                   | :heavy_check_mark:                                                        | N/A                                                                       |
| `metadata`                                                                | [models.ModelMetadata](../../models/modelmetadata.md)                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `model_developer`                                                         | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `model_family`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `model_id`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `model_type`                                                              | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `output_cost`                                                             | *float*                                                                   | :heavy_check_mark:                                                        | N/A                                                                       |
| `parameters`                                                              | List[[models.CreateModelParameter](../../models/createmodelparameter.md)] | :heavy_check_mark:                                                        | N/A                                                                       |
| `provider`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ModelCreateResponseBody](../../models/modelcreateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_autorouter

Creates an autorouter model that routes between a strong and economical source model based on the requested profile. Both source models must already exist for the workspace and be marked autorouter-eligible in master data.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCreateAutorouter" method="post" path="/v2/models/autorouter" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.create_autorouter(economical_model="<value>", key="<key>", strong_model="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `economical_model`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `strong_model`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `profile`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelCreateAutorouterResponseBody](../../models/modelcreateautorouterresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_autorouter

Re-configures an autorouter model. Each of key/strong_model/economical_model/profile falls back to the existing value when omitted. Changing the key enforces uniqueness and rewrites PRICING_KV.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelUpdateAutorouter" method="patch" path="/v2/models/autorouter/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.update_autorouter(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model                                                 |
| `economical_model`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `key`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `profile`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `strong_model`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelUpdateAutorouterResponseBody](../../models/modelupdateautorouterresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_aws_bedrock

Registers an AWS Bedrock inference profile as a custom model for the workspace. Credentials are resolved at request time via either the integration reference or pod-identity — nothing is stored with the model.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCreateAwsBedrock" method="post" path="/v2/models/aws-bedrock" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.create_aws_bedrock(auth_mode="<value>", display_name="Shanon.Wintheiser", model_developer="<value>", model_id="<id>", region="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `auth_mode`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model_developer`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `region`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `assume_role_arn`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `assume_role_external_id`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `has_reasoning`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `input_cost`                                                        | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `integration_id`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_tokens`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_family`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_type`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `output_cost`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_json_mode`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_json_schema`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_strict_tool`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_tool_calling`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_vision`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `temperature`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelCreateAwsBedrockResponseBody](../../models/modelcreateawsbedrockresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## validate_aws_bedrock

Performs a live Bedrock Converse probe to verify the inference profile ARN and credentials, then best-effort enriches the response from known system models.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelValidateAwsBedrock" method="post" path="/v2/models/aws-bedrock/validate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.models.validate_aws_bedrock(auth_mode="<value>", inference_profile_arn="<value>", region="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `auth_mode`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `inference_profile_arn`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `region`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `assume_role_arn`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `assume_role_external_id`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `integration_id`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_aws_bedrock

Updates an AWS Bedrock custom model. ARN changes are format-validated (live AWS validation lives in the dedicated validate endpoint). Configuration and metadata are spread-merged. Parameters are replaced only when the request produces a non-empty list.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelUpdateAwsBedrock" method="patch" path="/v2/models/aws-bedrock/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.update_aws_bedrock(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model                                                 |
| `assume_role_arn`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `assume_role_external_id`                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `display_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `has_reasoning`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `input_cost`                                                        | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_tokens`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_developer`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_family`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_type`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `output_cost`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `region`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_json_mode`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_json_schema`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_strict_tool`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_tool_calling`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_vision`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `temperature`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelUpdateAwsBedrockResponseBody](../../models/modelupdateawsbedrockresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## azure_foundry_deployments

Lists Azure Foundry deployments under the given base_url and joins each entry with the Orq master-data row. Only OpenAI-developed deployments in succeeded state with chat/completion/embedding/vision model types are returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelAzureFoundryDeployments" method="post" path="/v2/models/azure-foundry/deployments" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.azure_foundry_deployments(api_key="<value>", base_url="https://admired-overcoat.info", provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `base_url`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `api_version`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelAzureFoundryDeploymentsResponseBody](../../models/modelazurefoundrydeploymentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## import_litellm

Bulk-imports a list of LiteLLM model definitions into the workspace model garden.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelLiteLLMImport" method="post" path="/v2/models/litellm/import" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.import_litellm(request=[
        {
            "litellm_params": {
                "merge_reasoning_content_in_choices": False,
                "model": "CX-9",
                "use_in_pass_through": False,
                "use_litellm_proxy": False,
            },
            "model_info": {
                "db_model": True,
                "id": "<id>",
                "key": "<key>",
                "litellm_provider": "<value>",
                "mode": "<value>",
            },
            "model_name": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.LiteLLMModel]](../../models/.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ModelDocument]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_litellm

Fetches the list of models from the LiteLLM instance configured for the workspace. Requires a stored LiteLLM integration.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelListLitellm" method="get" path="/v2/models/litellm/models" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.list_litellm()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[Dict[str, Any]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_openai_like

Creates a custom model backed by any OpenAI-compatible endpoint. The handler probes the target API with the supplied credentials before persisting the model.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCreateOpenAILike" method="post" path="/v2/models/openai-like" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.create_openai_like(api_key="<value>", base_url="https://guilty-cap.org/", display_name="Richard.Beatty45", model_id="<id>", model_type="<value>", region="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `base_url`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model_type`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `region`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `cost_per_image`                                                    | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `has_reasoning`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `input_cost`                                                        | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_tokens`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `output_cost`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_image_edit`                                               | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_strict_tool`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_tool_calling`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_vision`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `temperature`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelCreateOpenAILikeResponseBody](../../models/modelcreateopenailikeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_openai_like

Updates an OpenAI-compatible custom model. Live-re-probes the target API when base_url or model_id changes, using the stored encrypted api_key. Metadata is merged (existing preserved, new overrides).

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelUpdateOpenAILike" method="patch" path="/v2/models/openai-like/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.update_openai_like(id="<id>", display_name="Verlie82", model_type="<value>", region="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model                                                 |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model_type`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `region`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cost_per_image`                                                    | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `has_reasoning`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `input_cost`                                                        | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_tokens`                                                        | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `model_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `output_cost`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_image_edit`                                               | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_strict_tool`                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_tool_calling`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `supports_vision`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `temperature`                                                       | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelUpdateOpenAILikeResponseBody](../../models/modelupdateopenailikeresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## validate

Validates a provider endpoint by performing a minimal live probe. Currently supports Azure OpenAI. Response includes the resolved region, whether the model is known to Orq, and either the full model document or a synthesized default.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelValidate" method="post" path="/v2/models/validate" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.models.validate(api_key="<value>", provider="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `api_version`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `base_url`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `deployment_name`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `endpoint`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `subtype`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_vertex

Registers a Google Vertex AI model as a custom model for the workspace. The service account credentials are probed against Vertex AI with a minimal GenerateContent call before persisting.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelCreateVertex" method="post" path="/v2/models/vertex" -->
```python
import orq_ai_sdk
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.create_vertex(configuration=orq_ai_sdk.VertexConfiguration(
        location="<value>",
        model_configuration=orq_ai_sdk.VertexModelConfiguration(
            capabilities=orq_ai_sdk.VertexCapabilities(
                structured_output=True,
                support_tool_calling=False,
                vision=True,
            ),
            id="<id>",
            input_cost=6100.6,
            output_cost=4860.06,
            parameters=orq_ai_sdk.VertexParameters(
                max_tokens=orq_ai_sdk.VertexParamRangeInt(
                    max=816266,
                    min=370614,
                ),
                temperature=orq_ai_sdk.VertexParamRange(
                    max=1989.61,
                    min=8564.64,
                ),
                top_p=orq_ai_sdk.VertexParamRange(
                    max=3250.24,
                    min=8051.01,
                ),
            ),
        ),
        project_id="<id>",
        service_account={
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
    ), display_name="Birdie_Bailey-Abernathy")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `configuration`                                                     | [models.VertexConfiguration](../../models/vertexconfiguration.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `display_name`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelCreateVertexResponseBody](../../models/modelcreatevertexresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete

Deletes a custom model from the workspace. System models cannot be deleted. Returns 200 with an explanatory message if the model is a system model or is still referenced by experiments.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelDelete" method="delete" path="/v2/models/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.models.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Updates a custom model. Only fields present in the request body are modified, except for `metadata` and `parameters`, which are fully replaced when present (preserved from the legacy handler's behavior).

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelUpdate" method="patch" path="/v2/models/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | The ID of the model                                                       |
| `display_name`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `has_functions`                                                           | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `input_cost`                                                              | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | N/A                                                                       |
| `metadata`                                                                | [Optional[models.ModelMetadata]](../../models/modelmetadata.md)           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `model_type`                                                              | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `output_cost`                                                             | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | N/A                                                                       |
| `parameters`                                                              | List[[models.UpdateModelParameter](../../models/updatemodelparameter.md)] | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ModelUpdateResponseBody](../../models/modelupdateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## enable

Adds the model to the workspace's enabled set. Idempotent — re-enabling an already-enabled model returns 204 with no state change.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelEnable" method="post" path="/v2/workspace-models" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.models.enable(model_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## disable

Removes the model from the workspace's enabled set. Idempotent — disabling an already-disabled model returns 204.

### Example Usage

<!-- UsageSnippet language="python" operationID="ModelDisable" method="delete" path="/v2/workspace-models/{model_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.models.disable(model_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to disable                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

Lists all models available through the AI Router. Returns each model in OpenAI-compatible shape with its provider, ID, and creation timestamp.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-models" method="get" path="/v3/router/models" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.models.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListModelsResponseBody](../../models/listmodelsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |