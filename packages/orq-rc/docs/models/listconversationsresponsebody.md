# ListConversationsResponseBody

Successfully retrieved the list of conversations. Returns a paginated response containing conversation objects.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `object`                                                               | [models.ListConversationsObject](../models/listconversationsobject.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `data`                                                                 | List[[models.ConversationResponse](../models/conversationresponse.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |