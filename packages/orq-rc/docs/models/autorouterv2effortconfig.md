# AutoRouterV2EffortConfig


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `aa_index_is_estimated`                                            | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether the score at this effort is estimated.                     |
| `aa_index_version`                                                 | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Version of the intelligence index measured at this effort.         |
| `aa_is_reasoning`                                                  | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether the model runs as a reasoning model at this effort.        |
| `aa_reasoning_effort`                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Reasoning effort label Artificial Analysis reports for this entry. |
| `aa_slug`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Artificial Analysis slug of the model at this effort.              |
| `intelligence_index`                                               | *float*                                                            | :heavy_check_mark:                                                 | Intelligence index measured at this effort.                        |