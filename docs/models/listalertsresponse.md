# ListAlertsResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `object`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | Object discriminator for list responses; always `list`.                  |
| `data`                                                                   | List[[models.Alert](../models/alert.md)]                                 | :heavy_check_mark:                                                       | Page of alerts, ordered newest first.                                    |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether more alerts are available in the selected pagination<br/> direction. |