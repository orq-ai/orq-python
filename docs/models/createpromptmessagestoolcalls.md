# CreatePromptMessagesToolCalls


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the tool call.                                                         |
| `type`                                                                           | [models.CreatePromptMessagesType](../models/createpromptmessagestype.md)         | :heavy_check_mark:                                                               | The type of the tool. Currently, only `function` is supported.                   |
| `function`                                                                       | [models.CreatePromptMessagesFunction](../models/createpromptmessagesfunction.md) | :heavy_check_mark:                                                               | N/A                                                                              |