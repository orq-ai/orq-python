# McpHeaderSecret


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `key`                                               | *Optional[str]*                                     | :heavy_minus_sign:                                  | Header name sent to the upstream server.            | Authorization                                       |
| `value`                                             | *Optional[str]*                                     | :heavy_minus_sign:                                  | Header value; accepted on write and never returned. | ghp_xxxxxxxxxxxx                                    |
| `masked_value`                                      | *Optional[str]*                                     | :heavy_minus_sign:                                  | Redacted preview of `value`, returned in its place. |                                                     |