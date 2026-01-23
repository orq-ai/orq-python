# ListPromptVersionsCache

Cache configuration for the request.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `ttl`                                                                          | *Optional[float]*                                                              | :heavy_minus_sign:                                                             | Time to live for cached responses in seconds. Maximum 259200 seconds (3 days). | 3600                                                                           |
| `type`                                                                         | [models.ListPromptVersionsType](../models/listpromptversionstype.md)           | :heavy_check_mark:                                                             | N/A                                                                            |                                                                                |