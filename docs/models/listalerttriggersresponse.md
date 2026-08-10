# ListAlertTriggersResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | *str*                                                                      | :heavy_check_mark:                                                         | Object discriminator for list responses; always `list`.                    |
| `data`                                                                     | List[[models.AlertTrigger](../models/alerttrigger.md)]                     | :heavy_check_mark:                                                         | Page of triggers, ordered newest first.                                    |
| `has_more`                                                                 | *bool*                                                                     | :heavy_check_mark:                                                         | Whether more triggers are available in the selected pagination<br/> direction. |