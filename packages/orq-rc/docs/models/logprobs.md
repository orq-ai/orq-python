# Logprobs

Log probability information for the choice.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `content`                                                                                        | List[[models.AgentThoughtStreamingEventContent](../models/agentthoughtstreamingeventcontent.md)] | :heavy_check_mark:                                                                               | A list of message content tokens with log probability information.                               |
| `refusal`                                                                                        | List[[models.AgentThoughtStreamingEventRefusal](../models/agentthoughtstreamingeventrefusal.md)] | :heavy_check_mark:                                                                               | A list of message refusal tokens with log probability information.                               |