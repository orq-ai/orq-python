# Usage

Usage statistics to add to the deployment


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `prompt_tokens`                                                   | *float*                                                           | :heavy_check_mark:                                                | Number of tokens in the prompt.                                   |
| `completion_tokens`                                               | *float*                                                           | :heavy_check_mark:                                                | Number of tokens in the generated completion.                     |
| `total_tokens`                                                    | *Optional[float]*                                                 | :heavy_minus_sign:                                                | Total number of tokens used in the request (prompt + completion). |