# CreateImageResponseBody

Represents an image generation response from the API.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `created`                                                          | *float*                                                            | :heavy_check_mark:                                                 | The Unix timestamp (in seconds) of when the image was created.     |
| `data`                                                             | List[[models.CreateImageData](../models/createimagedata.md)]       | :heavy_check_mark:                                                 | Represents the url or the content of an image generated.           |
| `usage`                                                            | [Optional[models.CreateImageUsage]](../models/createimageusage.md) | :heavy_minus_sign:                                                 | N/A                                                                |