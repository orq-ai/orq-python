# CreateEmbeddingResponseBody

Returns the embedding vector.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `data`                                                               | List[[models.PublicEmbeddingData](../models/publicembeddingdata.md)] | :heavy_check_mark:                                                   | List of embedding objects.                                           |
| `model`                                                              | *str*                                                                | :heavy_check_mark:                                                   | ID of the model used.                                                |
| `object`                                                             | [models.CreateEmbeddingObject](../models/createembeddingobject.md)   | :heavy_check_mark:                                                   | Always "list".                                                       |
| `usage`                                                              | [models.PublicEmbeddingUsage](../models/publicembeddingusage.md)     | :heavy_check_mark:                                                   | N/A                                                                  |