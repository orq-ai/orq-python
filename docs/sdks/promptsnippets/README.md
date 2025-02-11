# PromptSnippets
(*prompt_snippets*)

## Overview

### Available Operations

* [list](#list) - List all prompts snippets
* [create](#create) - Create a prompt snippet
* [update](#update) - Update a prompt snippet
* [delete](#delete) - Delete a prompt snippet
* [get](#get) - Retrieve a prompt snippet
* [get_by_key](#get_by_key) - Retrieve a prompt snippet by key

## list

List all prompts snippets

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompt_snippets.list()

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

**[models.GetAllPromptSnippetsResponseBody](../../models/getallpromptsnippetsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

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
        "prompt_config": {
            "messages": [
                {
                    "role": "prompt",
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
| `id`                                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | Unique identifier of the prompt                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                 |
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
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the prompt                                     |
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