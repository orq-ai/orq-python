# ResponseBodyLogprobs

Log probability information for the choice.


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `content`                                                                                                      | List[[models.RouterChatCompletionsResponseBodyContent](../models/routerchatcompletionsresponsebodycontent.md)] | :heavy_check_mark:                                                                                             | A list of message content tokens with log probability information.                                             |
| `refusal`                                                                                                      | List[[models.ResponseBodyRefusal](../models/responsebodyrefusal.md)]                                           | :heavy_check_mark:                                                                                             | A list of message refusal tokens with log probability information.                                             |