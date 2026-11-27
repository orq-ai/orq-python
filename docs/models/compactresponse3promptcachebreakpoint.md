# CompactResponse3PromptCacheBreakpoint

An explicit OpenAI cache boundary for GPT-5.6 and later. Omitted ttl inherits prompt_cache_options.ttl.


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `mode`                                                                                                   | [models.CompactResponse3Mode](../models/compactresponse3mode.md)                                         | :heavy_check_mark:                                                                                       | N/A                                                                                                      |
| `ttl`                                                                                                    | [Optional[models.CompactResponse3ResponsesRequestTTL]](../models/compactresponse3responsesrequestttl.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |