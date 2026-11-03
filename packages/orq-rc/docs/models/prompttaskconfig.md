# PromptTaskConfig


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `prompt_config`                                                 | Dict[str, *Any*]                                                | :heavy_check_mark:                                              | N/A                                                             |
| `messages_source`                                               | [Optional[models.MessagesSource]](../models/messagessource.md)  | :heavy_minus_sign:                                              | N/A                                                             |
| `engine`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `tools`                                                         | List[Dict[str, *Any*]]                                          | :heavy_minus_sign:                                              | N/A                                                             |
| `knowledge_bases`                                               | List[Dict[str, *Any*]]                                          | :heavy_minus_sign:                                              | N/A                                                             |
| `metadata`                                                      | Dict[str, *Any*]                                                | :heavy_minus_sign:                                              | Null when the column was saved without metadata.                |
| `entity_configuration`                                          | Dict[str, *Any*]                                                | :heavy_minus_sign:                                              | Null when the column was saved without an entity configuration. |