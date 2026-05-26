# PublicModelEntry


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `created`                                                       | *int*                                                           | :heavy_check_mark:                                              | Unix timestamp (seconds) when the model was added.              |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | Model identifier in provider/model format (e.g. openai/gpt-4o). |
| `object`                                                        | [models.Object](../models/object.md)                            | :heavy_check_mark:                                              | Always "model".                                                 |
| `owned_by`                                                      | *str*                                                           | :heavy_check_mark:                                              | The provider that owns the model (e.g. openai, anthropic).      |