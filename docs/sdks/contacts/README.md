# Contacts
(*contacts*)

## Overview

### Available Operations

* [create](#create) - Update user information

## create

Update or add user information to workspace

### Example Usage

```python
from orq_ai_sdk import Orq
import os

with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(external_id="<id>")

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `external_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | Unique string value to identify the contact user in the customer's system |
| `display_name`                                                            | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | Display name or nickname of the user                                      |
| `email`                                                                   | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | Email address of the user                                                 |
| `avatar_url`                                                              | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | URL linking to the user's avatar image                                    |
| `tags`                                                                    | List[*str*]                                                               | :heavy_minus_sign:                                                        | Array of UUIDs representing tags associated with the user                 |
| `metadata`                                                                | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | Additional custom metadata associated with the user as key-value pairs    |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateContactResponseBody](../../models/createcontactresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |