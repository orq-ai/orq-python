# People

## Overview

### Available Operations

* [list](#list) - List all people
* [create](#create) - Invite people to a workspace
* [get](#get) - Retrieve a person
* [delete](#delete) - Delete a person
* [update](#update) - Update a person
* [resend_invitation](#resend_invitation) - Resend invitation

## list

Returns a paginated list of people in the current workspace. Use `starting_after` or `ending_before` to page through large collections.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonList" method="get" path="/v2/people" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `limit`                                                                                    | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | Page size, 1-200. Unset uses the server default.                                           |
| `starting_after`                                                                           | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for forward pagination. Set to the `id` of the last<br/> item from the previous page. |
| `ending_before`                                                                            | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Cursor for backward pagination. Set to the `id` of the first<br/> item from the previous page. |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[models.ListPeopleResponse](../../models/listpeopleresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Invites one or more people to the current workspace. If an email is not already registered, a new account is created and an invitation email is sent. Existing accounts are linked directly to the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonCreate" method="post" path="/v2/people" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.create(emails=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `emails`                                                            | List[*str*]                                                         | :heavy_check_mark:                                                  | Email addresses to invite. At least one email is required.          |
| `roles`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | Roles to assign. Defaults to ["member"] when empty.                 |
| `groups`                                                            | List[*str*]                                                         | :heavy_minus_sign:                                                  | Group IDs to assign.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreatePersonResponse](../../models/createpersonresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieves the details of an existing workspace member or invited user by their person ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonGet" method="get" path="/v2/people/{person_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.get(person_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `person_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Person ID to retrieve.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPersonResponse](../../models/getpersonresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Removes a member or invited user from the workspace. API keys owned by the removed user are cascade revoked. The response body is empty when the delete succeeds.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonDelete" method="delete" path="/v2/people/{person_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.delete(person_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `person_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Person ID to delete.                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletePersonResponse](../../models/deletepersonresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## update

Updates the roles and group assignments of a workspace member. Omitted fields keep their current values.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonUpdate" method="patch" path="/v2/people/{person_id}" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.update(person_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `person_id`                                                                  | *str*                                                                        | :heavy_check_mark:                                                           | Person ID to update.                                                         |
| `roles`                                                                      | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Replacement role list. Leave empty to clear all roles.                       |
| `groups`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Replacement group list. Leave empty to clear all groups.                     |
| `clear_roles`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Explicitly clear all roles. Set to true when sending an empty roles array.   |
| `clear_groups`                                                               | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Explicitly clear all groups. Set to true when sending an empty groups array. |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.UpdatePersonResponse](../../models/updatepersonresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |

## resend_invitation

Resends the invitation email to a pending workspace member. Has no effect if the person has already accepted.

### Example Usage

<!-- UsageSnippet language="python" operationID="PersonResendInvitation" method="post" path="/v2/people/{person_id}:resend" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.people.resend_invitation(person_id="<id>", resend_invitation_request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `person_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | Person ID of the pending invite to resend.                                |
| `resend_invitation_request`                                               | [models.ResendInvitationRequest](../../models/resendinvitationrequest.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ResendInvitationResponse](../../models/resendinvitationresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models.APIDefaultError | 4XX, 5XX               | \*/\*                  |