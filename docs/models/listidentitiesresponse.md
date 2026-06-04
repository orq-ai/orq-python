# ListIdentitiesResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `object`                                                                     | *str*                                                                        | :heavy_check_mark:                                                           | Object discriminator for list responses; always `list`.                      |
| `data`                                                                       | List[[models.Identity](../models/identity.md)]                               | :heavy_check_mark:                                                           | Page of identities.                                                          |
| `has_more`                                                                   | *bool*                                                                       | :heavy_check_mark:                                                           | Whether more identities are available in the selected pagination<br/> direction. |