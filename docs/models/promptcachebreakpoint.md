# PromptCacheBreakpoint

An explicit OpenAI cache boundary for GPT-5.6 and later. Omitted ttl inherits prompt_cache_options.ttl.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `mode`                                                                                     | [models.TwoMode](../models/twomode.md)                                                     | :heavy_check_mark:                                                                         | N/A                                                                                        |
| `ttl`                                                                                      | [Optional[models.CompactResponse2ResponsesTTL]](../models/compactresponse2responsesttl.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |