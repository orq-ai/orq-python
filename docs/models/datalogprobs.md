# DataLogprobs

Log probability information for the choice.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `content`                                                                  | List[[models.StreamAgentDataContent](../models/streamagentdatacontent.md)] | :heavy_check_mark:                                                         | A list of message content tokens with log probability information.         |
| `refusal`                                                                  | List[[models.DataRefusal](../models/datarefusal.md)]                       | :heavy_check_mark:                                                         | A list of message refusal tokens with log probability information.         |