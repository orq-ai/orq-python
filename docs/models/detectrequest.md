# DetectRequest

The workspace is resolved from the API key, never sent in the body.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `text`                                                                      | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Text to analyse.                                                            |
| `language`                                                                  | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | BCP-47 language code. Unset means auto-detect.                              |
| `threshold`                                                                 | *Optional[float]*                                                           | :heavy_minus_sign:                                                          | Global minimum recognizer score (0.0-1.0). Unset uses the provider default. |
| `include_entities`                                                          | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | When true, the response includes a per-type entity breakdown.               |