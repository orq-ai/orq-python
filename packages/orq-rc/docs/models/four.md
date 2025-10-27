# Four


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [models.Deployments2PrefixMessagesType](../models/deployments2prefixmessagestype.md) | :heavy_check_mark:                                                                   | The type of the content part. Always `file`.                                         |
| `file`                                                                               | [models.File](../models/file.md)                                                     | :heavy_check_mark:                                                                   | File data for the content part. Must contain either file_data or uri, but not both.  |