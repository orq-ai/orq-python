# UpsertChunk


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `text`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | The text content of the chunk                                             |
| `embedding`                                                               | List[*float*]                                                             | :heavy_minus_sign:                                                        | N/A                                                                       |
| `metadata`                                                                | Dict[str, [models.UpsertChunkMetadata](../models/upsertchunkmetadata.md)] | :heavy_minus_sign:                                                        | Metadata of the chunk                                                     |