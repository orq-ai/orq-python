# FilePart

File attachment part. Use this to send files (images, documents, etc.) to the agent for processing.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `kind`                                                             | [models.PublicMessagePartKind](../models/publicmessagepartkind.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `file`                                                             | [models.PublicMessagePartFile](../models/publicmessagepartfile.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `metadata`                                                         | Dict[str, *Any*]                                                   | :heavy_minus_sign:                                                 | N/A                                                                |