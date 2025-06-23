# EvalsRagasNoiseSensitivityRequestBody


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `query`                                                           | *str*                                                             | :heavy_check_mark:                                                | Latest user message                                               |
| `output`                                                          | *str*                                                             | :heavy_check_mark:                                                | The generated response from the model                             |
| `model`                                                           | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `reference`                                                       | *str*                                                             | :heavy_check_mark:                                                | The ground truth answer to evaluate noise sensitivity against     |
| `retrievals`                                                      | List[*str*]                                                       | :heavy_minus_sign:                                                | Knowledge base retrievals that may contain irrelevant information |