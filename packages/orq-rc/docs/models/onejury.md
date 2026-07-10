# OneJury


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `judges`                                                               | List[[models.OneJudges](../models/onejudges.md)]                       | :heavy_check_mark:                                                     | N/A                                                                    |
| `replacement_judges`                                                   | List[[models.OneReplacementJudges](../models/onereplacementjudges.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `min_successful_judges`                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `tie_value`                                                            | [Optional[models.OneTieValue]](../models/onetievalue.md)               | :heavy_minus_sign:                                                     | N/A                                                                    |