# Output1

An assistant message output


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The unique identifier for this message                   |
| `type`                                                   | [models.OutputType](../models/outputtype.md)             | :heavy_check_mark:                                       | The type of output item                                  |
| `role`                                                   | [models.OutputRole](../models/outputrole.md)             | :heavy_check_mark:                                       | The role of the message author                           |
| `status`                                                 | [models.OutputStatus](../models/outputstatus.md)         | :heavy_check_mark:                                       | The status of the message                                |
| `content`                                                | List[[models.OutputContent](../models/outputcontent.md)] | :heavy_minus_sign:                                       | The content parts of the message                         |