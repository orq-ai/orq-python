# Chunks


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `text`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The text content of the chunk                                        |
| `index`                                                              | *float*                                                              | :heavy_check_mark:                                                   | The position index of this chunk in the sequence                     |
| `metadata`                                                           | [Optional[models.ChunkTextMetadata]](../models/chunktextmetadata.md) | :heavy_minus_sign:                                                   | N/A                                                                  |