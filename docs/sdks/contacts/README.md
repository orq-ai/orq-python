# Contacts
(*contacts*)

## Overview

### Available Operations

* [create](#create) - Create a contact
* [list](#list) - List contacts
* [retrieve](#retrieve) - Retrieve a contact
* [update](#update) - Update a contact
* [delete](#delete) - Delete a contact

## create

Creates a new contact with a unique external_id. If a contact with the same external_id already exists, the operation will fail. Use this endpoint to add users from your system to orq.ai for tracking their usage and engagement.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateContact" method="post" path="/v2/contacts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(request={
        "external_id": "user_12345",
        "display_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "avatar_url": "https://example.com/avatars/jane-smith.jpg",
        "tags": [
            "premium",
            "beta-user",
            "enterprise",
        ],
        "metadata": {
            "department": "Engineering",
            "role": "Senior Developer",
            "subscription_tier": "premium",
            "last_login": "2024-01-15T10:30:00Z",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateContactRequestBody](../../models/createcontactrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreateContactResponseBody](../../models/createcontactresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list

Retrieves a paginated list of contacts in your workspace. Use pagination parameters to navigate through large contact lists efficiently.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListContacts" method="get" path="/v2/contacts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.list(limit=10, filter_by={
        "tags": [
            "premium",
            "beta-user",
        ],
    }, include_metrics=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                               | Type                                                                                                                                                                                                                                                                                                                                    | Required                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                 | *Optional[float]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                         |
| `starting_after`                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list.       |                                                                                                                                                                                                                                                                                                                                         |
| `ending_before`                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list. |                                                                                                                                                                                                                                                                                                                                         |
| `filter_by`                                                                                                                                                                                                                                                                                                                             | [Optional[models.QueryParamFilterBy]](../../models/queryparamfilterby.md)                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Filter contacts by tags. Can be provided as JSON object {"tags": ["premium", "beta-user"]} or as query format "tags=premium,beta-user"                                                                                                                                                                                                  | {<br/>"tags": [<br/>"premium",<br/>"beta-user"<br/>]<br/>}                                                                                                                                                                                                                                                                              |
| `include_metrics`                                                                                                                                                                                                                                                                                                                       | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Include usage metrics of the last 30 days for each contact.                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                         |

### Response

**[models.ListContactsResponseBody](../../models/listcontactsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves detailed information about a specific contact using their contact ID or external ID from your system.

### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveContact" method="get" path="/v2/contacts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.retrieve(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Unique contact id or external id                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveContactResponseBody](../../models/retrievecontactresponsebody.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.RetrieveContactContactsResponseBody | 404                                        | application/json                           |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## update

Updates specific fields of an existing contact. Only the fields provided in the request body will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateContact" method="patch" path="/v2/contacts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.update(id="<id>", display_name="Jane Smith", email="jane.smith@example.com", avatar_url="https://example.com/avatars/jane-smith.jpg", tags=[
        "premium",
        "beta-user",
        "enterprise",
    ], metadata={
        "department": "Engineering",
        "role": "Senior Developer",
        "subscription_tier": "premium",
        "last_login": "2024-01-15T10:30:00Z",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      | Example                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                             | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Unique contact id or external id                                                                                                                 |                                                                                                                                                  |
| `display_name`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                               | Display name or nickname of the contact user. This is typically shown in user interfaces.                                                        | Jane Smith                                                                                                                                       |
| `email`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                               | Email address of the contact user                                                                                                                | jane.smith@example.com                                                                                                                           |
| `avatar_url`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                               | URL linking to the contact user's avatar image                                                                                                   | https://example.com/avatars/jane-smith.jpg                                                                                                       |
| `tags`                                                                                                                                           | List[*str*]                                                                                                                                      | :heavy_minus_sign:                                                                                                                               | Array of tags associated with the contact. Useful for organizing and filtering contacts by categories, departments, or custom classifications.   | [<br/>"premium",<br/>"beta-user",<br/>"enterprise"<br/>]                                                                                         |
| `metadata`                                                                                                                                       | Dict[str, *Any*]                                                                                                                                 | :heavy_minus_sign:                                                                                                                               | Additional custom metadata associated with the contact as key-value pairs. Use this to store any extra information specific to your application. | {<br/>"department": "Engineering",<br/>"role": "Senior Developer",<br/>"subscription_tier": "premium",<br/>"last_login": "2024-01-15T10:30:00Z"<br/>} |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |                                                                                                                                                  |

### Response

**[models.UpdateContactResponseBody](../../models/updatecontactresponsebody.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.UpdateContactContactsResponseBody | 404                                      | application/json                         |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## delete

Permanently deletes a contact from your workspace and cleans up associated budget configurations. This action cannot be undone.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteContact" method="delete" path="/v2/contacts/{id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    orq.contacts.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Contact ID or External ID                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.DeleteContactResponseBody | 404                              | application/json                 |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |