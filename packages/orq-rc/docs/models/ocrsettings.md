# OcrSettings

Optional settings for the OCR run


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `include_image_base64`                                             | *OptionalNullable[bool]*                                           | :heavy_minus_sign:                                                 | Whether to include image Base64 in the response. Null for default. |
| `max_images_to_include`                                            | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Maximum number of images to extract. Null for no limit.            |
| `image_min_size`                                                   | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Minimum height and width of image to extract. Null for no minimum. |