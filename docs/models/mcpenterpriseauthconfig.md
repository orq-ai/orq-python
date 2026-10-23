# McpEnterpriseAuthConfig

McpEnterpriseAuthConfig is the client orq registered at the upstream's authorization
 server for enterprise-managed authorization (ID-JAG). Access policy lives in the
 workspace's SSO identity provider; users must sign in through SSO to use the server.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `resource`                                                                            | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | RFC 9728 resource identifier the tokens are bound to; defaults to the connection URL. |
| `client_id`                                                                           | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | OAuth client identifier registered at the upstream authorization server.              |
| `client_secret`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | OAuth client secret; accepted on write and never returned.                            |
| `masked_value`                                                                        | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Redacted preview of `client_secret`, returned in its place.                           |
| `scopes`                                                                              | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Scopes requested when redeeming the identity assertion grant.                         |