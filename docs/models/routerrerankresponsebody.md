# RouterRerankResponseBody

A response body that follows the official OpenAI schema


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `results`                                    | List[[models.Results](../models/results.md)] | :heavy_check_mark:                           | An ordered list of ranked documents          |
| `id`                                         | *Optional[str]*                              | :heavy_minus_sign:                           | A unique identifier for the rerank.          |
| `meta`                                       | [Optional[models.Meta]](../models/meta.md)   | :heavy_minus_sign:                           | Some information about the response          |