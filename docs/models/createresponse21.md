# CreateResponse21

Represents a message in the conversation, with a role and content (string or rich content parts).


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `role`                                                                   | [models.TwoRole](../models/tworole.md)                                   | :heavy_check_mark:                                                       | The role of the message author                                           |
| `content`                                                                | [models.TwoContent](../models/twocontent.md)                             | :heavy_check_mark:                                                       | The content of the message, either a string or an array of content parts |