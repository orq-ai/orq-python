# ThreePromptCacheBreakpoint

An explicit OpenAI cache boundary for GPT-5.6 and later. Omitted ttl inherits prompt_cache_options.ttl.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `mode`                                                                   | [models.ThreeMode](../models/threemode.md)                               | :heavy_check_mark:                                                       | N/A                                                                      |
| `ttl`                                                                    | [Optional[models.CompactResponse3TTL]](../models/compactresponse3ttl.md) | :heavy_minus_sign:                                                       | N/A                                                                      |