# PrefixMessagesToolCalls


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of the tool call.                                             |
| `type`                                                               | [models.PrefixMessagesType](../models/prefixmessagestype.md)         | :heavy_check_mark:                                                   | The type of the tool. Currently, only `5` is supported.              |
| `function`                                                           | [models.PrefixMessagesFunction](../models/prefixmessagesfunction.md) | :heavy_check_mark:                                                   | N/A                                                                  |