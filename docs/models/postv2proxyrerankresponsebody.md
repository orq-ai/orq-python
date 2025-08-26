# PostV2ProxyRerankResponseBody

Returns the reranked documents.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A unique identifier for the rerank.                                            |
| `object`                                                                       | [models.PostV2ProxyRerankObject](../models/postv2proxyrerankobject.md)         | :heavy_check_mark:                                                             | N/A                                                                            |
| `results`                                                                      | List[[models.PostV2ProxyRerankResults](../models/postv2proxyrerankresults.md)] | :heavy_check_mark:                                                             | An ordered list of ranked documents                                            |
| `usage`                                                                        | [Optional[models.PostV2ProxyRerankUsage]](../models/postv2proxyrerankusage.md) | :heavy_minus_sign:                                                             | N/A                                                                            |