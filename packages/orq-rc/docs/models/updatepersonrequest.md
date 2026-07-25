# UpdatePersonRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `roles`                                                                      | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Replacement role list. Leave empty to clear all roles.                       |
| `groups`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | Replacement group list. Leave empty to clear all groups.                     |
| `clear_roles`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Explicitly clear all roles. Set to true when sending an empty roles array.   |
| `clear_groups`                                                               | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Explicitly clear all groups. Set to true when sending an empty groups array. |