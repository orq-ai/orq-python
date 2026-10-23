# UpdateIdentityRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `display_name`                                             | *Optional[str]*                                            | :heavy_minus_sign:                                         | New display name. Omit to keep the current display name.   |
| `email`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | New email address. Omit to keep the current email.         |
| `avatar_url`                                               | *Optional[str]*                                            | :heavy_minus_sign:                                         | New avatar image URL. Omit to keep the current avatar URL. |
| `tags`                                                     | List[*str*]                                                | :heavy_minus_sign:                                         | Replacement tag list. Leave empty to clear tags.           |
| `metadata`                                                 | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | Replacement custom JSON metadata.                          |