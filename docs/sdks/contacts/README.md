# Contacts

## Overview

### Available Operations

* [create](#create) - Update user information

## create

Update or add user information to workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateContact" method="post" path="/v2/contacts" -->
```python
from orq_ai_sdk import Orq
import os


with Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
) as orq:

    res = orq.contacts.create(external_id="user_12345", display_name="Jane Smith", email="jane.smith@example.com", avatar_url="https://example.com/avatars/jane-smith.jpg", tags=[
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

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          | Example                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `external_id`                                                                                                                                        | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | Unique string value to identify the contact user in the customer's system. This should be the same ID you use in your system to reference this user. | user_12345                                                                                                                                           |
| `display_name`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                                   | Display name or nickname of the contact user. This is typically shown in user interfaces.                                                            | Jane Smith                                                                                                                                           |
| `email`                                                                                                                                              | *OptionalNullable[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                                   | Email address of the contact user                                                                                                                    | jane.smith@example.com                                                                                                                               |
| `avatar_url`                                                                                                                                         | *OptionalNullable[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                                   | URL linking to the contact user's avatar image                                                                                                       | https://example.com/avatars/jane-smith.jpg                                                                                                           |
| `tags`                                                                                                                                               | List[*str*]                                                                                                                                          | :heavy_minus_sign:                                                                                                                                   | Array of tags associated with the contact. Useful for organizing and filtering contacts by categories, departments, or custom classifications.       | [<br/>"premium",<br/>"beta-user",<br/>"enterprise"<br/>]                                                                                             |
| `metadata`                                                                                                                                           | Dict[str, *Any*]                                                                                                                                     | :heavy_minus_sign:                                                                                                                                   | Additional custom metadata associated with the contact as key-value pairs. Use this to store any extra information specific to your application.     | {<br/>"department": "Engineering",<br/>"role": "Senior Developer",<br/>"subscription_tier": "premium",<br/>"last_login": "2024-01-15T10:30:00Z"<br/>} |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |                                                                                                                                                      |

### Response

**[models.CreateContactResponseBody](../../models/createcontactresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |