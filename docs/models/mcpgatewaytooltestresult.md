# McpGatewayToolTestResult


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `ok`                                                  | *Optional[bool]*                                      | :heavy_minus_sign:                                    | Whether the tool call completed successfully.         |
| `result`                                              | [Optional[models.Result]](../models/result.md)        | :heavy_minus_sign:                                    | Payload returned by the upstream tool.                |
| `latency_ms`                                          | *Optional[int]*                                       | :heavy_minus_sign:                                    | Round trip time of the tool call in milliseconds.     |
| `error_message`                                       | *Optional[str]*                                       | :heavy_minus_sign:                                    | Human-readable reason the call failed.                |
| `errors`                                              | List[*str*]                                           | :heavy_minus_sign:                                    | Additional failure details collected during the call. |