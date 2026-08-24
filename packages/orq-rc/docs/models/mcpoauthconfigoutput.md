# McpOAuthConfigOutput


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `client_id`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | OAuth client identifier presented to the upstream authorization server. |
| `token_url`                                                             | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Token endpoint the gateway calls to mint upstream access tokens.        |
| `scopes`                                                                | List[*str*]                                                             | :heavy_minus_sign:                                                      | Scopes requested when minting upstream access tokens.                   |
| `masked_value`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Redacted preview of `client_secret`, returned in its place.             |