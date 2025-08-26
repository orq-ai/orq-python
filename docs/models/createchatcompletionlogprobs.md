# CreateChatCompletionLogprobs

Log probability information for the choice.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `content`                                                                                      | List[[models.CreateChatCompletionProxyContent](../models/createchatcompletionproxycontent.md)] | :heavy_check_mark:                                                                             | A list of message content tokens with log probability information.                             |
| `refusal`                                                                                      | List[[models.CreateChatCompletionRefusal](../models/createchatcompletionrefusal.md)]           | :heavy_check_mark:                                                                             | A list of message refusal tokens with log probability information.                             |