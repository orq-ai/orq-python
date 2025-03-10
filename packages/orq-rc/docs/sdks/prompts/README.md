# Prompts
(*prompts*)

## Overview

### Available Operations

* [list](#list) - List all prompts
* [retrieve](#retrieve) - Retrieve a prompt
* [update](#update) - Update a prompt
* [delete](#delete) - Delete a prompt
* [create](#create) - Create a prompt
* [list_versions](#list_versions) - List all prompt versions
* [get_version](#get_version) - Retrieve a prompt version

## list

Returns a list of your prompts. The prompts are returned sorted by creation date, with the most recent prompts appearing first

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.list()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort`                                                                                                                                                                                                                                                                                                                                  | [Optional[models.GetAllPromptsQueryParamSort]](../../models/getallpromptsqueryparamsort.md)                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | List sorting preference.                                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |

### Response

**[models.GetAllPromptsResponseBody](../../models/getallpromptsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves a prompt object

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.retrieve(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the prompt                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOnePromptResponseBody](../../models/getonepromptresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a prompt

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.update(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                       | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | Unique identifier of the prompt                                                                                                                            |
| `owner`                                                                                                                                                    | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `domain_id`                                                                                                                                                | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `created`                                                                                                                                                  | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `updated`                                                                                                                                                  | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `created_by_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `updated_by_id`                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `display_name`                                                                                                                                             | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The prompt’s name, meant to be displayable in the UI.                                                                                                      |
| `description`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                    | :heavy_minus_sign:                                                                                                                                         | The prompt’s description, meant to be displayable in the UI. Use this field to optionally store a long form explanation of the prompt for your own purpose |
| `prompt_config`                                                                                                                                            | [Optional[models.PromptConfig]](../../models/promptconfig.md)                                                                                              | :heavy_minus_sign:                                                                                                                                         | A list of messages compatible with the openAI schema                                                                                                       |
| `metadata`                                                                                                                                                 | [Optional[models.UpdatePromptMetadata]](../../models/updatepromptmetadata.md)                                                                              | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |

### Response

**[models.UpdatePromptResponseBody](../../models/updatepromptresponsebody.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.UpdatePromptPromptsResponseBody | 404                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete a prompt

### Example Usage

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a prompt

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.create(request={
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

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreatePromptRequestBody](../../models/createpromptrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreatePromptResponseBody](../../models/createpromptresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_versions

Returns a list of your prompt versions. The prompt versions are returned sorted by creation date, with the most recent prompt versions appearing first

### Example Usage

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.list_versions(prompt_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prompt_id`                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                      | N/A                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                  | [Optional[models.ListPromptVersionsQueryParamSort]](../../models/listpromptversionsqueryparamsort.md)                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | List sorting preference.                                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |
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

```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.prompts.get_version(prompt_id="<id>", version_id="<id>")

    assert res is not None

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