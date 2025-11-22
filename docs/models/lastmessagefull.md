# LastMessageFull

Full last message in A2A format (for backwards compatibility)


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `message_id`                                                                             | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `role`                                                                                   | [models.StreamRunAgentDataAgentsRole](../models/streamrunagentdataagentsrole.md)         | :heavy_check_mark:                                                                       | Extended A2A message role                                                                |
| `parts`                                                                                  | List[[models.StreamRunAgentDataAgentsParts](../models/streamrunagentdataagentsparts.md)] | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `metadata`                                                                               | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |