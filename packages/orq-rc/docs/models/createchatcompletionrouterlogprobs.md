# CreateChatCompletionRouterLogprobs

Log probability information for the choice.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `content`                                                                                        | List[[models.CreateChatCompletionRouterContent](../models/createchatcompletionroutercontent.md)] | :heavy_check_mark:                                                                               | A list of message content tokens with log probability information.                               |
| `refusal`                                                                                        | List[[models.CreateChatCompletionRouterRefusal](../models/createchatcompletionrouterrefusal.md)] | :heavy_check_mark:                                                                               | A list of message refusal tokens with log probability information.                               |