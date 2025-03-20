# DeploymentStream2DeploymentsInputAudio


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `data`                                                                                       | *str*                                                                                        | :heavy_check_mark:                                                                           | Base64 encoded audio data.                                                                   |
| `format_`                                                                                    | [models.DeploymentStream2DeploymentsFormat](../models/deploymentstream2deploymentsformat.md) | :heavy_check_mark:                                                                           | The format of the encoded audio data. Currently supports `wav` and `mp3`.                    |