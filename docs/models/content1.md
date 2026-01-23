# Content1

Text output from the model


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `type`                                               | [models.ContentType](../models/contenttype.md)       | :heavy_check_mark:                                   | The type of content part                             |
| `text`                                               | *str*                                                | :heavy_check_mark:                                   | The text content                                     |
| `annotations`                                        | List[[models.Annotations](../models/annotations.md)] | :heavy_minus_sign:                                   | Annotations in the text such as citations            |
| `logprobs`                                           | List[*Any*]                                          | :heavy_minus_sign:                                   | Log probabilities of the output tokens if requested  |