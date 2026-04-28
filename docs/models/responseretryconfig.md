# ResponseRetryConfig


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `count`                                                             | *int*                                                               | :heavy_check_mark:                                                  | Number of retries (1-5).                                            |
| `on_codes`                                                          | List[*int*]                                                         | :heavy_check_mark:                                                  | HTTP status codes that trigger a retry (e.g. [429, 500, 502, 503]). |