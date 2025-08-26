# PostV2ProxyEmbeddingsResponseBody

Returns the embedding vector.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `object`                                                                               | [models.PostV2ProxyEmbeddingsObject](../models/postv2proxyembeddingsobject.md)         | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `data`                                                                                 | List[[models.PostV2ProxyEmbeddingsData](../models/postv2proxyembeddingsdata.md)]       | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `model`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | ID of the model to used.                                                               |
| `usage`                                                                                | [Optional[models.PostV2ProxyEmbeddingsUsage]](../models/postv2proxyembeddingsusage.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |