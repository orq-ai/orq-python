# LLMJury


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `judges`                                                               | List[[models.LLMJudges](../models/llmjudges.md)]                       | :heavy_check_mark:                                                     | N/A                                                                    |
| `replacement_judges`                                                   | List[[models.LLMReplacementJudges](../models/llmreplacementjudges.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `min_successful_judges`                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `tie_value`                                                            | [Optional[models.LLMTieValue]](../models/llmtievalue.md)               | :heavy_minus_sign:                                                     | N/A                                                                    |