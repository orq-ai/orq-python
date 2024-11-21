# RouterCompletionsUsage

Usage statistics for the completion request.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `completion_tokens`                                               | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Number of tokens in the generated completion.                     |
| `prompt_tokens`                                                   | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Number of tokens in the prompt.                                   |
| `total_tokens`                                                    | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Total number of tokens used in the request (prompt + completion). |