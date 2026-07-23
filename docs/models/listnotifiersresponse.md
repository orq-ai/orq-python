# ListNotifiersResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | *str*                                                                      | :heavy_check_mark:                                                         | Object discriminator for list responses; always `list`.                    |
| `data`                                                                     | List[[models.Notifier](../models/notifier.md)]                             | :heavy_check_mark:                                                         | Page of notifiers.                                                         |
| `has_more`                                                                 | *bool*                                                                     | :heavy_check_mark:                                                         | Whether more notifiers are available in the selected pagination direction. |