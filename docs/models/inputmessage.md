# InputMessage


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `message_id`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `role`                                           | [models.DataRole](../models/datarole.md)         | :heavy_check_mark:                               | Extended A2A message role                        |
| `parts`                                          | List[[models.DataParts](../models/dataparts.md)] | :heavy_check_mark:                               | N/A                                              |
| `metadata`                                       | Dict[str, *Any*]                                 | :heavy_minus_sign:                               | N/A                                              |