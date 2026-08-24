# McpTestResult


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `ok`                                                       | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the probe connected and listed tools successfully. |
| `tools`                                                    | List[[models.McpTool](../models/mcptool.md)]               | :heavy_minus_sign:                                         | Tools discovered during the probe; not persisted.          |
| `latency_ms`                                               | *Optional[int]*                                            | :heavy_minus_sign:                                         | Round trip time of the probe in milliseconds.              |
| `error_message`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | Human-readable reason the probe failed.                    |
| `errors`                                                   | List[*str*]                                                | :heavy_minus_sign:                                         | Additional failure details collected during the probe.     |