# ListAlertTriggerEventsResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `object`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | Object discriminator for list responses; always `list`.                  |
| `data`                                                                   | List[[models.AlertTriggerEvent](../models/alerttriggerevent.md)]         | :heavy_check_mark:                                                       | Page of events, ordered newest first.                                    |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether more events are available in the selected pagination<br/> direction. |