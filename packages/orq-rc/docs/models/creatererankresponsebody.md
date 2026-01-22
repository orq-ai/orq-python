# CreateRerankResponseBody

Returns the reranked documents.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A unique identifier for the rerank.                                  |
| `object`                                                             | [models.CreateRerankObject](../models/creatererankobject.md)         | :heavy_check_mark:                                                   | N/A                                                                  |
| `results`                                                            | List[[models.CreateRerankResults](../models/creatererankresults.md)] | :heavy_check_mark:                                                   | An ordered list of ranked documents                                  |
| `usage`                                                              | [Optional[models.CreateRerankUsage]](../models/creatererankusage.md) | :heavy_minus_sign:                                                   | N/A                                                                  |