# SearchKnowledgeResponseBody

Knowledge successfully retrieved


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `knowledge_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | Unique id of the knowledge base                                                |
| `documents`                                                                    | List[[models.SearchKnowledgeDocuments](../models/searchknowledgedocuments.md)] | :heavy_check_mark:                                                             | The documents returned                                                         |
| `knowledge_key`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | The key of the knowledge base                                                  |
| `query`                                                                        | *str*                                                                          | :heavy_check_mark:                                                             | The query used to search the knowledge base                                    |