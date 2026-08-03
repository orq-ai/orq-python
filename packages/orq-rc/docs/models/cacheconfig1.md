# CacheConfig1

Configuration schema for exact-match cache. Entries are stored and retrieved based on exact input matches.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `type`                                                                         | [models.CacheConfigType](../models/cacheconfigtype.md)                         | :heavy_check_mark:                                                             | N/A                                                                            |                                                                                |
| `ttl`                                                                          | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Time to live for cached responses in seconds. Maximum 259200 seconds (3 days). | 3600                                                                           |