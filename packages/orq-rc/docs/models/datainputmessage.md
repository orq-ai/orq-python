# DataInputMessage


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `message_id`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `role`                                                                 | [models.StreamAgentDataRole](../models/streamagentdatarole.md)         | :heavy_check_mark:                                                     | Extended A2A message role                                              |
| `parts`                                                                | List[[models.StreamAgentDataParts](../models/streamagentdataparts.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `metadata`                                                             | Dict[str, *Any*]                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |