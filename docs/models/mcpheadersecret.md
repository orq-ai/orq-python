# McpHeaderSecret


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `key`                                               | *Optional[str]*                                     | :heavy_minus_sign:                                  | Header name sent to the upstream server.            |
| `value`                                             | *Optional[str]*                                     | :heavy_minus_sign:                                  | Header value; accepted on write and never returned. |
| `masked_value`                                      | *Optional[str]*                                     | :heavy_minus_sign:                                  | Redacted preview of `value`, returned in its place. |