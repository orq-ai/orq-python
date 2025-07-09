# TokenChunkerStrategy

Splits text based on token count. Best for ensuring chunks fit within LLM context windows and maintaining consistent chunk sizes for embedding models.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `text`                                                         | *str*                                                          | :heavy_check_mark:                                             | The text content to be chunked                                 |
| `metadata`                                                     | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether to include metadata for each chunk                     |
| `return_type`                                                  | [Optional[models.ReturnType]](../models/returntype.md)         | :heavy_minus_sign:                                             | Return format: chunks (with metadata) or texts (plain strings) |
| `strategy`                                                     | [models.TokenChunker](../models/tokenchunker.md)               | :heavy_check_mark:                                             | N/A                                                            |
| `chunk_size`                                                   | *Optional[int]*                                                | :heavy_minus_sign:                                             | Maximum tokens per chunk                                       |
| `chunk_overlap`                                                | *Optional[int]*                                                | :heavy_minus_sign:                                             | Number of tokens to overlap between chunks                     |