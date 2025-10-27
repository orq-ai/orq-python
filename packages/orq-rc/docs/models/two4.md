# Two4


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `type`                                                                                     | [models.Deployments2Messages3Content4Type](../models/deployments2messages3content4type.md) | :heavy_check_mark:                                                                         | The type of the content part. Always `file`.                                               |
| `file`                                                                                     | [models.TwoFile](../models/twofile.md)                                                     | :heavy_check_mark:                                                                         | File data for the content part. Must contain either file_data or uri, but not both.        |