# Four


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `type`                                                                              | [models.TwoType](../models/twotype.md)                                              | :heavy_check_mark:                                                                  | The type of the content part. Always `file`.                                        |
| `cache_control`                                                                     | [Optional[models.TwoCacheControl]](../models/twocachecontrol.md)                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `file`                                                                              | [models.FileContentPartSchema](../models/filecontentpartschema.md)                  | :heavy_check_mark:                                                                  | File data for the content part. Must contain either file_data or uri, but not both. |