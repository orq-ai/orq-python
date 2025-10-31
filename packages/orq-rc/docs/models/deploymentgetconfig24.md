# DeploymentGetConfig24


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `type`                                                                                         | [models.DeploymentGetConfig2DeploymentsType](../models/deploymentgetconfig2deploymentstype.md) | :heavy_check_mark:                                                                             | The type of the content part. Always `file`.                                                   |
| `file`                                                                                         | [models.DeploymentGetConfig2File](../models/deploymentgetconfig2file.md)                       | :heavy_check_mark:                                                                             | File data for the content part. Must contain either file_data or uri, but not both.            |