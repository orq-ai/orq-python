# ChoicesToolCalls


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `id`                                                           | *str*                                                          | :heavy_check_mark:                                             | The ID of the tool call.                                       |
| `type`                                                         | [models.ChoicesType](../models/choicestype.md)                 | :heavy_check_mark:                                             | The type of the tool. Currently, only `function` is supported. |
| `function`                                                     | [models.ChoicesFunction](../models/choicesfunction.md)         | :heavy_check_mark:                                             | N/A                                                            |