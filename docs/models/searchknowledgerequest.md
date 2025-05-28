# SearchKnowledgeRequest


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `knowledge_id`                                                                         | *str*                                                                                  | :heavy_check_mark:                                                                     | The unique identifier or key of the knowledge base                                     |
| `request_body`                                                                         | [Optional[models.SearchKnowledgeRequestBody]](../models/searchknowledgerequestbody.md) | :heavy_minus_sign:                                                                     | A search request for chunks in a knowledge base                                        |