# EmbeddingCacheConfig


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `ttl`                                                                          | *Optional[int]*                                                                | :heavy_minus_sign:                                                             | Time to live for cached responses in seconds. Maximum 259200 seconds (3 days). |
| `type`                                                                         | [models.EmbeddingCacheConfigType](../models/embeddingcacheconfigtype.md)       | :heavy_check_mark:                                                             | Cache type.                                                                    |