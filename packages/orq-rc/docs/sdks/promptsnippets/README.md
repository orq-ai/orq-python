# PromptSnippets
(*prompt_snippets*)

## Overview

### Available Operations

* [create](#create) - Create a prompt snippet
* [update](#update) - Update a prompt snippet
* [delete](#delete) - Delete a prompt snippet
* [get](#get) - Retrieve a prompt snippet
* [get_by_key](#get_by_key) - Retrieve a prompt snippet by key

## create

Create a prompt snippet

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompt_snippets.create(request={
        "key": "<key>",
        "display_name": "Jed6",
        "prompt_config": {
            "messages": [
                {
                    "role": "system",
                    "content": "<value>",
                },
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": "https://well-worn-formation.biz",
                            },
                        },
                        {
                            "type": "text",
                            "text": "<value>",
                        },
                        {
                            "type": "text",
                            "text": "<value>",
                        },
                    ],
                },
                {
                    "role": "assistant",
                    "content": "<value>",
                },
            ],
        },
        "path": "Customer Service/Billing/Refund",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.CreatePromptSnippetRequestBody](../../models/createpromptsnippetrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.CreatePromptSnippetResponseBody](../../models/createpromptsnippetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a prompt snippet

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompt_snippets.update(id="<id>", path="Customer Service/Billing/Refund")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | Prompt ID                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                 |
| `display_name`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The prompt snippet’s name, meant to be displayable in the UI.                                                                                                                                                                                   |                                                                                                                                                                                                                                                 |
| `description`                                                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                              | The prompt snippet’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose                                                                              |                                                                                                                                                                                                                                                 |
| `prompt_config`                                                                                                                                                                                                                                 | [Optional[models.UpdatePromptSnippetPromptConfig]](../../models/updatepromptsnippetpromptconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                              | A list of messages compatible with the openAI schema                                                                                                                                                                                            |                                                                                                                                                                                                                                                 |
| `metadata`                                                                                                                                                                                                                                      | [Optional[models.UpdatePromptSnippetMetadata]](../../models/updatepromptsnippetmetadata.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                              | N/A                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                 |
| `path`                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | The path where the entity is stored in the project structure. The first element of the path always represents the project name. Any subsequent path element after the project will be created as a folder in the project if it does not exists. | Customer Service/Billing/Refund                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.UpdatePromptSnippetResponseBody](../../models/updatepromptsnippetresponsebody.md)**

### Errors

| Error Type                                           | Status Code                                          | Content Type                                         |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| models.UpdatePromptSnippetPromptSnippetsResponseBody | 404                                                  | application/json                                     |
| models.APIError                                      | 4XX, 5XX                                             | \*/\*                                                |

## delete

Delete a prompt snippet

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.prompt_snippets.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Prompt ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a prompt snippet

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompt_snippets.get(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Prompt ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FindOnePromptSnippetResponseBody](../../models/findonepromptsnippetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_by_key

Retrieve a prompt snippet by key

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompt_snippets.get_by_key(key="<key>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Prompt Key                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FindOneByKeyPromptSnippetResponseBody](../../models/findonebykeypromptsnippetresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |