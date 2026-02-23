# Jury


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `judges`                                                         | List[[models.Judges](../models/judges.md)]                       | :heavy_check_mark:                                               | N/A                                                              |
| `replacement_judges`                                             | List[[models.ReplacementJudges](../models/replacementjudges.md)] | :heavy_minus_sign:                                               | N/A                                                              |
| `min_successful_judges`                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `tie_value`                                                      | [Optional[models.TieValue]](../models/tievalue.md)               | :heavy_minus_sign:                                               | N/A                                                              |