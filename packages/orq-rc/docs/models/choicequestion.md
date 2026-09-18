# ChoiceQuestion

Picks one of the given options and returns the probability of each.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `criteria`                                                                     | Dict[str, *Nullable[str]*]                                                     | :heavy_check_mark:                                                             | Options keyed by name, each mapped to a description or null.                   |
| `instructions`                                                                 | [models.QuestionsInstructions](../models/questionsinstructions.md)             | :heavy_check_mark:                                                             | The evaluation prompt for this question. A string, an object or an array.      |
| `type`                                                                         | [models.CreateClassifyQuestionsType](../models/createclassifyquestionstype.md) | :heavy_check_mark:                                                             | N/A                                                                            |