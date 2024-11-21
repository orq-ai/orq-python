# RouterImageGenerationsRequestBody

A request body that follows the official OpenAI schema


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `prompt`                                                       | *str*                                                          | :heavy_check_mark:                                             | The prompt to generate an image                                |
| `model`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | The model to use for generation                                |
| `n`                                                            | *Optional[float]*                                              | :heavy_minus_sign:                                             | The number of images to generate                               |
| `quality`                                                      | [Optional[models.Quality]](../models/quality.md)               | :heavy_minus_sign:                                             | The quality of the image                                       |
| `response_format`                                              | [Optional[models.ResponseFormat]](../models/responseformat.md) | :heavy_minus_sign:                                             | The format of the image                                        |
| `size`                                                         | [Optional[models.Size]](../models/size.md)                     | :heavy_minus_sign:                                             | The size of the image                                          |
| `style`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | The style of the image                                         |
| `user`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | The user who created the image                                 |