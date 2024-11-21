# MessagesToolCalls


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | The ID of the tool call.                                         |
| `type`                                                           | [models.MessagesType](../models/messagestype.md)                 | :heavy_check_mark:                                               | The type of the tool. Currently, only **function** is supported. |
| `function`                                                       | [models.MessagesFunction](../models/messagesfunction.md)         | :heavy_check_mark:                                               | The function that the model called.                              |