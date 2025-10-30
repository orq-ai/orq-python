# UpdatePromptMessagesToolCalls


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the tool call.                                                         |
| `type`                                                                           | [models.UpdatePromptMessagesType](../models/updatepromptmessagestype.md)         | :heavy_check_mark:                                                               | The type of the tool. Currently, only `function` is supported.                   |
| `function`                                                                       | [models.UpdatePromptMessagesFunction](../models/updatepromptmessagesfunction.md) | :heavy_check_mark:                                                               | N/A                                                                              |