# EvalsRagasContextPrecisionRequestBody


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `query`                                  | *str*                                    | :heavy_check_mark:                       | Latest user message                      |
| `output`                                 | *str*                                    | :heavy_check_mark:                       | The generated response from the model    |
| `model`                                  | *str*                                    | :heavy_check_mark:                       | N/A                                      |
| `reference`                              | *Optional[str]*                          | :heavy_minus_sign:                       | The reference used to compare the output |
| `retrievals`                             | List[*str*]                              | :heavy_minus_sign:                       | Knowledge base retrievals                |