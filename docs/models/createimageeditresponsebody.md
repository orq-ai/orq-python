# CreateImageEditResponseBody

Represents an image edit response from the API.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `created`                                                                  | *float*                                                                    | :heavy_check_mark:                                                         | The Unix timestamp (in seconds) of when the image was created.             |
| `output_format`                                                            | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The output format of the image generation                                  |
| `size`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The size of the image generated                                            |
| `quality`                                                                  | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The quality of the image generated                                         |
| `data`                                                                     | List[[models.CreateImageEditData](../models/createimageeditdata.md)]       | :heavy_check_mark:                                                         | The list of generated images.                                              |
| `usage`                                                                    | [Optional[models.CreateImageEditUsage]](../models/createimageeditusage.md) | :heavy_minus_sign:                                                         | The token usage information for the image generation.                      |