# Performance


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `latency`                                                                 | *float*                                                                   | :heavy_check_mark:                                                        | Total time in milliseconds of the request to the LLM provider API.        |
| `time_to_first_token`                                                     | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | Total time in milliseconds to generate the first token of the completion. |