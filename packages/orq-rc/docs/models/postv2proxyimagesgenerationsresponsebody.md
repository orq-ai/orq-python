# PostV2ProxyImagesGenerationsResponseBody

Represents an image generation response from the API.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `created`                                                                                            | *Optional[float]*                                                                                    | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `data`                                                                                               | List[[models.PostV2ProxyImagesGenerationsData](../models/postv2proxyimagesgenerationsdata.md)]       | :heavy_check_mark:                                                                                   | Represents the url or the content of an image generated.                                             |
| `usage`                                                                                              | [Optional[models.PostV2ProxyImagesGenerationsUsage]](../models/postv2proxyimagesgenerationsusage.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |