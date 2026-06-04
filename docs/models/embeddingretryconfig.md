# EmbeddingRetryConfig


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `count`                                     | *int*                                       | :heavy_check_mark:                          | Number of retry attempts (1-5).             |
| `on_codes`                                  | List[*int*]                                 | :heavy_check_mark:                          | HTTP status codes that trigger retry logic. |