# CreateClassifyResponseBody

Returns one answer per question.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `answers`                                                           | Dict[str, [models.ClassifyAnswer](../models/classifyanswer.md)]     | :heavy_check_mark:                                                  | Answers keyed by the question identifiers from the request.         |
| `model`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The model that served the request, for example typesafe/jev-latest. |
| `usage`                                                             | [models.ClassifyUsage](../models/classifyusage.md)                  | :heavy_check_mark:                                                  | N/A                                                                 |