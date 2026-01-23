# CreateEmbeddingResponseBody

Returns the embedding vector.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `object`                                                             | [models.CreateEmbeddingObject](../models/createembeddingobject.md)   | :heavy_check_mark:                                                   | N/A                                                                  |
| `data`                                                               | List[[models.CreateEmbeddingData](../models/createembeddingdata.md)] | :heavy_check_mark:                                                   | N/A                                                                  |
| `model`                                                              | *str*                                                                | :heavy_check_mark:                                                   | ID of the model to used.                                             |
| `usage`                                                              | [models.CreateEmbeddingUsage](../models/createembeddingusage.md)     | :heavy_check_mark:                                                   | The usage information for the request.                               |