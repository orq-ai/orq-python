# EvalsRagasContextRecallRequestBody


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `query`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | Latest user message                                        |
| `output`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | The generated response from the model                      |
| `model`                                                    | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `reference`                                                | *str*                                                      | :heavy_check_mark:                                         | The ground truth answer to evaluate context recall against |
| `retrievals`                                               | List[*str*]                                                | :heavy_minus_sign:                                         | Knowledge base retrievals                                  |