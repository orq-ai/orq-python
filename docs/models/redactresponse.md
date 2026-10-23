# RedactResponse


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `redacted_text`                                                              | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `mappings`                                                                   | Dict[str, *str*]                                                             | :heavy_minus_sign:                                                           | Maps each placeholder (e.g. "<PERSON_1>") to the original value it replaced. |