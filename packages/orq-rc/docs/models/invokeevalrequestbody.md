# InvokeEvalRequestBody


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `query`                                                                 | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Latest user message                                                     |
| `output`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The generated response from the model                                   |
| `reference`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | The reference used to compare the output                                |
| `retrievals`                                                            | List[*str*]                                                             | :heavy_minus_sign:                                                      | Knowledge base retrievals                                               |
| `messages`                                                              | List[[models.InvokeEvalMessages](../models/invokeevalmessages.md)]      | :heavy_minus_sign:                                                      | The messages used to generate the output, without the last user message |