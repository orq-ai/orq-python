# ModelCreateVertexRequestBody


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `benchmark_model`                                              | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |
| `configuration`                                                | [models.VertexConfiguration](../models/vertexconfiguration.md) | :heavy_check_mark:                                             | N/A                                                            |
| `display_name`                                                 | *str*                                                          | :heavy_check_mark:                                             | N/A                                                            |
| `model_id`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | Immutable private-model slug; defaults to display_name.        |