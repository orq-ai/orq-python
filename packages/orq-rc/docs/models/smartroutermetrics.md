# SmartRouterMetrics


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `requests`                                                          | *float*                                                             | :heavy_check_mark:                                                  | Total gateway requests served by the router over the window.        |
| `spend`                                                             | *float*                                                             | :heavy_check_mark:                                                  | Total cost in USD attributed to the router over the window.         |
| `traffic`                                                           | Dict[str, *float*]                                                  | :heavy_check_mark:                                                  | Requests per selected model, keyed by the provider/model reference. |