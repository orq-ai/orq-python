# Nine

Asks a model to choose the boundaries. Slowest and most expensive, best on documents with irregular structure. Makes paid model calls.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | [models.ChunkingConfiguration9Type](../models/chunkingconfiguration9type.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `chunk_size`                                                                 | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Maximum number of tokens per chunk.                                          |
| `model`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Model that chooses the chunk boundaries.                                     |
| `candidate_size`                                                             | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Size of candidate splits offered to the model.                               |
| `min_characters_per_chunk`                                                   | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Minimum number of characters each chunk must contain.                        |
| `system_prompt`                                                              | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Custom system prompt for the boundary model.                                 |