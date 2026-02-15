# Prompts

## Overview

### Available Operations

* [list](#list) - List all prompts
* [create](#create) - Create a prompt
* [retrieve](#retrieve) - Retrieve a prompt
* [update](#update) - Update a prompt
* [delete](#delete) - Delete a prompt
* [list_versions](#list_versions) - List all prompt versions
* [get_version](#get_version) - Retrieve a prompt version

## list

Returns a list of your prompts. The prompts are returned sorted by creation date, with the most recent prompts appearing first

### Example Usage

<!-- UsageSnippet language="python" operationID="GetAllPrompts" method="get" path="/v2/prompts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.list(limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetAllPromptsResponseBody](../../models/getallpromptsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="CreatePrompt" method="post" path="/v2/prompts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.create(request={
        "display_name": "Raymundo83",
        "prompt": {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant",
                },
                {
                    "role": "user",
                    "content": "What is the weather today?",
                },
            ],
            "model": "openai/gpt-4o",
            "max_tokens": 1000,
            "temperature": 0.7,
        },
        "path": "Default",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreatePromptRequestBody](../../models/createpromptrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreatePromptPrompt](../../models/createpromptprompt.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves a prompt object

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOnePrompt" method="get" path="/v2/prompts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the prompt                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOnePromptPrompt](../../models/getonepromptprompt.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdatePrompt" method="patch" path="/v2/prompts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.update(id="<id>", prompt={
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant",
            },
            {
                "role": "user",
                "content": "Hello!",
            },
        ],
        "model": "anthropic/claude-3-5-sonnet-20241022",
        "temperature": 0.5,
    }, path="Default")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                             | Unique identifier of the prompt                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                |
| `owner`                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `domain_id`                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `created`                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `updated`                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `created_by_id`                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `updated_by_id`                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `display_name`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The prompt’s name, meant to be displayable in the UI.                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                |
| `description`                                                                                                                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose                                                                                                                                     |                                                                                                                                                                                                                                                                                                |
| `prompt`                                                                                                                                                                                                                                                                                       | [Optional[models.UpdatePromptPromptInput]](../../models/updatepromptpromptinput.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Prompt configuration with model and messages. Use this to update the prompt.                                                                                                                                                                                                                   | {<br/>"model": "anthropic/claude-3-5-sonnet-20241022",<br/>"messages": [<br/>{<br/>"role": "system",<br/>"content": "You are a helpful assistant"<br/>},<br/>{<br/>"role": "user",<br/>"content": "Hello!"<br/>}<br/>],<br/>"temperature": 0.5<br/>}                                           |
| `metadata`                                                                                                                                                                                                                                                                                     | [Optional[models.UpdatePromptMetadata]](../../models/updatepromptmetadata.md)                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |
| `path`                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Entity storage path in the format: `project/folder/subfolder/...`<br/><br/>The first element identifies the project, followed by nested folders (auto-created as needed).<br/><br/>With project-based API keys, the first element is treated as a folder name, as the project is predetermined by the API key. | Default                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                |

### Response

**[models.UpdatePromptPrompt](../../models/updatepromptprompt.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.UpdatePromptResponseBody | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## delete

Delete a prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="DeletePrompt" method="delete" path="/v2/prompts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.prompts.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the prompt                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.DeletePromptResponseBody | 404                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## list_versions

Returns a list of your prompt versions. The prompt versions are returned sorted by creation date, with the most recent prompt versions appearing first

### Example Usage

<!-- UsageSnippet language="python" operationID="ListPromptVersions" method="get" path="/v2/prompts/{prompt_id}/versions" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.list_versions(prompt_id="<id>", limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt_id`                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                                                                     |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.ListPromptVersionsResponseBody](../../models/listpromptversionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_version

Retrieves a specific version of a prompt by its ID and version ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetPromptVersion" method="get" path="/v2/prompts/{prompt_id}/versions/{version_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.get_version(prompt_id="<id>", version_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `prompt_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the prompt                                 |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the prompt version                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPromptVersionResponseBody](../../models/getpromptversionresponsebody.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.GetPromptVersionPromptsResponseBody | 404                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |