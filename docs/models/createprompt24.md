# CreatePrompt24


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [models.CreatePrompt2Type](../models/createprompt2type.md)                           | :heavy_check_mark:                                                                   | The type of the content part. Always `file`.                                         |
| `cache_control`                                                                      | [Optional[models.CreatePrompt2CacheControl]](../models/createprompt2cachecontrol.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `file`                                                                               | [models.FileContentPartSchema](../models/filecontentpartschema.md)                   | :heavy_check_mark:                                                                   | File data for the content part. Must contain either file_data or uri, but not both.  |