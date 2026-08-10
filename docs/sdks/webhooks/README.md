# Webhooks

## Overview

### Available Operations

* [list](#list) - List webhooks
* [create](#create) - Create a webhook
* [count](#count) - Count webhooks
* [~~query~~](#query) - Query webhooks :warning: **Deprecated**
* [generate_secret](#generate_secret) - Generate a webhook secret
* [get](#get) - Retrieve a webhook
* [delete](#delete) - Delete a webhook
* [update](#update) - Update a webhook

## list

Returns a page of webhooks in the current workspace. By default, the first 20 matching webhooks are ordered by creation time, newest first. Supplied filters are combined, `count` reports the total number of matches before pagination, and `has_more` indicates whether another page is available.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookList" method="get" path="/v2/webhooks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | One-based page number. Defaults to 1 and must be between 1 and 1,000,000.                                                                                                               |
| `limit`                                                                                                                                                                                 | *Optional[int]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Number of webhooks to return per page. Defaults to 20 and must be between<br/> 1 and 200.                                                                                               |
| `search`                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Optional case-insensitive substring matched against display name, content<br/> type, and URL. Maximum length is 200 characters.                                                         |
| `event`                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Optional event slug that must be present in the webhook's event<br/> subscriptions, for example `llm.response`. Maximum length is 200<br/> characters.                                  |
| `sort`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Field used to order results. Allowed values are `created`, `updated`, and<br/> `display_name`. Defaults to `created`.                                                                   |
| `direction`                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Sort direction. Allowed values are `asc` and `desc`. Defaults to `desc`.                                                                                                                |
| `content_type`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                      | Optional comma-separated content types to match, for example<br/> `application/json,application/x-www-form-urlencoded`. A webhook matches<br/> when its content type equals any supplied value. |
| `enabled`                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Optional delivery status filter. When omitted, enabled and disabled<br/> webhooks are returned.                                                                                         |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |

### Response

**[models.ListWebhooksResponse](../../models/listwebhooksresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Creates a webhook that delivers the selected workspace events to an HTTPS endpoint. Generate a signing secret first with `GET /v2/webhooks/secret`.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookCreate" method="post" path="/v2/webhooks" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.create(id="<id>", url="https://outlying-tenement.name/", content_type="application/json", display_name="June.Hand", events=[
        "<value 1>",
        "<value 2>",
    ], secret="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Client-generated webhook ID.                                                                                                                                     |
| `url`                                                                                                                                                            | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | HTTPS endpoint that receives webhook deliveries.                                                                                                                 |
| `content_type`                                                                                                                                                   | [models.CreateWebhookRequestContentType](../../models/createwebhookrequestcontenttype.md)                                                                        | :heavy_check_mark:                                                                                                                                               | Content type sent with webhook deliveries.                                                                                                                       |
| `display_name`                                                                                                                                                   | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Human-readable webhook name.                                                                                                                                     |
| `events`                                                                                                                                                         | List[*str*]                                                                                                                                                      | :heavy_check_mark:                                                                                                                                               | One or more workspace event slugs that trigger a delivery, for example `deployment.invoked` or `llm.response`.                                                   |
| `secret`                                                                                                                                                         | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Signing secret returned by `GET /v2/webhooks/secret`. Deliveries set `X-Orq-Signature` to the lowercase hexadecimal HMAC-SHA256 of the exact request body bytes. |
| `enabled`                                                                                                                                                        | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Whether webhook deliveries are enabled.                                                                                                                          |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[models.Webhook](../../models/webhook.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## count

Returns the total number of enabled and disabled webhooks in the current workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookCount" method="get" path="/v2/webhooks/count" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.count()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountWebhooksResponse](../../models/countwebhooksresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## ~~query~~

**Deprecated.** Returns webhooks matching legacy query filters. Use `GET /v2/webhooks` for pagination, search, event filtering, and sorting.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookQuery" method="post" path="/v2/webhooks/query" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.query()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `pagination`                                                                    | [Optional[models.QueryParamsPagination]](../../models/queryparamspagination.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `sorting_props`                                                                 | List[[models.QueryParamsSort](../../models/queryparamssort.md)]                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `query`                                                                         | [Optional[models.Query]](../../models/query.md)                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `filters`                                                                       | List[[models.Filters](../../models/filters.md)]                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `included_fields`                                                               | Dict[str, *str*]                                                                | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.QueryWebhooksResponse](../../models/querywebhooksresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## generate_secret

Generates a signing secret for verifying webhook deliveries. The secret is not persisted until it is used to create or update a webhook; store it securely.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookGenerateSecret" method="get" path="/v2/webhooks/secret" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.generate_secret()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GenerateWebhookSecretResponse](../../models/generatewebhooksecretresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves a webhook in the current workspace by ID. The response includes its signing secret; treat it as sensitive.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookGet" method="get" path="/v2/webhooks/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Webhook](../../models/webhook.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Deletes a webhook in the current workspace and returns the deleted webhook ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookDelete" method="delete" path="/v2/webhooks/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteWebhookResponse](../../models/deletewebhookresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates the supplied fields on a webhook in the current workspace. Omitted fields are unchanged. The response contains the applied fields rather than the complete webhook.

### Example Usage

<!-- UsageSnippet language="python" operationID="WebhookUpdate" method="patch" path="/v2/webhooks/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.webhooks.update(id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `request_body`                                                              | [models.WebhookUpdateRequestBody](../../models/webhookupdaterequestbody.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.WebhookUpdateResponseBody](../../models/webhookupdateresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |