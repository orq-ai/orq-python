# RouterEmbeddingRequestBody


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `input`                                                               | [models.Input](../models/input.md)                                    | :heavy_check_mark:                                                    | Input text to embed, encoded as a string or array of tokens.          |
| `model`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | ID of the model to use                                                |
| `encoding_format`                                                     | [Optional[models.EncodingFormat]](../models/encodingformat.md)        | :heavy_minus_sign:                                                    | Type of the document element                                          |
| `dimensions`                                                          | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | The number of dimensions the resulting output embeddings should have. |
| `user`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | A unique identifier representing your end-user                        |