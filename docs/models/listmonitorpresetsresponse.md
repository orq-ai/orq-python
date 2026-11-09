# ListMonitorPresetsResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `object`                                                 | *str*                                                    | :heavy_check_mark:                                       | Object discriminator for list responses; always `list`.  |
| `data`                                                   | List[[models.MonitorPreset](../models/monitorpreset.md)] | :heavy_check_mark:                                       | Built-in presets, dashboards first.                      |