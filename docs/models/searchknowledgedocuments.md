# SearchKnowledgeDocuments


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique identifier for the retrieval                                    |
| `text`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Text content of the document                                           |
| `metadata`                                                             | [models.SearchKnowledgeMetadata](../models/searchknowledgemetadata.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `score`                                                                | *float*                                                                | :heavy_check_mark:                                                     | The score of the document                                              |
| `rerank_score`                                                         | *Optional[float]*                                                      | :heavy_minus_sign:                                                     | The rerank score of the document                                       |