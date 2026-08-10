# CreatePersonRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `emails`                                                   | List[*str*]                                                | :heavy_check_mark:                                         | Email addresses to invite. At least one email is required. |
| `roles`                                                    | List[*str*]                                                | :heavy_minus_sign:                                         | Roles to assign. Defaults to ["member"] when empty.        |
| `groups`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Group IDs to assign.                                       |