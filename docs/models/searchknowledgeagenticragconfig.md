# SearchKnowledgeAgenticRagConfig

Override the agentic RAG configuration for this search. If not provided, will use the knowledge base configured agentic RAG settings.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `model_db_id`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `provider`                                                                               | [models.SearchKnowledgeKnowledgeProvider](../models/searchknowledgeknowledgeprovider.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `integration_id`                                                                         | *OptionalNullable[str]*                                                                  | :heavy_minus_sign:                                                                       | N/A                                                                                      |