# QuestionsNoulQuestion

Answers with a probability between 0 and 1 that the statement holds.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `criteria`                                                                                       | [Optional[models.QuestionsCriteria]](../models/questionscriteria.md)                             | :heavy_minus_sign:                                                                               | Optional descriptions of what true and false mean.                                               |
| `instructions`                                                                                   | [models.CreateDecisionsQuestionsInstructions](../models/createdecisionsquestionsinstructions.md) | :heavy_check_mark:                                                                               | The evaluation prompt for this question. A string, an object or an array.                        |
| `type`                                                                                           | [models.CreateDecisionsQuestionsType](../models/createdecisionsquestionstype.md)                 | :heavy_check_mark:                                                                               | N/A                                                                                              |