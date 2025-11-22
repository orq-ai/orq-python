# ModelConfigurationRetry

Retry configuration for model requests. Retries are triggered for specific HTTP status codes (e.g., 500, 429, 502, 503, 504). Supports configurable retry count (1-5) and custom status codes.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `count`                                    | *Optional[float]*                          | :heavy_minus_sign:                         | Number of retry attempts (1-5)             | 3                                          |
| `on_codes`                                 | List[*float*]                              | :heavy_minus_sign:                         | HTTP status codes that trigger retry logic | [<br/>429,<br/>500,<br/>502,<br/>503,<br/>504<br/>] |