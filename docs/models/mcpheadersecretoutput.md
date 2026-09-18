# McpHeaderSecretOutput


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `key`                                               | *Optional[str]*                                     | :heavy_minus_sign:                                  | Header name sent to the upstream server.            | Authorization                                       |
| `masked_value`                                      | *Optional[str]*                                     | :heavy_minus_sign:                                  | Redacted preview of `value`, returned in its place. |                                                     |