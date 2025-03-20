# DeploymentStream2InputAudio


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `data`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | Base64 encoded audio data.                                                |
| `format_`                                                                 | [models.DeploymentStream2Format](../models/deploymentstream2format.md)    | :heavy_check_mark:                                                        | The format of the encoded audio data. Currently supports `wav` and `mp3`. |