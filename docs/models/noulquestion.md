# NoulQuestion

Answers with a probability between 0 and 1 that the statement holds.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `criteria`                                                                | [Optional[models.Criteria]](../models/criteria.md)                        | :heavy_minus_sign:                                                        | Optional descriptions of what true and false mean.                        |
| `instructions`                                                            | [models.Instructions](../models/instructions.md)                          | :heavy_check_mark:                                                        | The evaluation prompt for this question. A string, an object or an array. |
| `type`                                                                    | [models.QuestionsType](../models/questionstype.md)                        | :heavy_check_mark:                                                        | N/A                                                                       |