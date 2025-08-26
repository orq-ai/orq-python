# CreateResponse22

An image input content part.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | [models.CreateResponse2ProxyType](../models/createresponse2proxytype.md)     | :heavy_check_mark:                                                           | The type of input content part                                               |
| `detail`                                                                     | [Optional[models.CreateResponse2Detail]](../models/createresponse2detail.md) | :heavy_minus_sign:                                                           | Level of detail for image analysis                                           |
| `file_id`                                                                    | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | File ID for the image                                                        |
| `image_url`                                                                  | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | URL of the image (can be http URL or data URL)                               |