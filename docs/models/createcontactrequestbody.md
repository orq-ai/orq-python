# CreateContactRequestBody

Update user information payload


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `external_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | Unique string value to identify the contact user in the customer's system |
| `display_name`                                                            | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | Display name or nickname of the user                                      |
| `email`                                                                   | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | Email address of the user                                                 |
| `avatar_url`                                                              | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | URL linking to the user's avatar image                                    |
| `tags`                                                                    | List[*str*]                                                               | :heavy_minus_sign:                                                        | Array of UUIDs representing tags associated with the user                 |
| `metadata`                                                                | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | Additional custom metadata associated with the user as key-value pairs    |