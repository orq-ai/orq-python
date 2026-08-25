# McpToolAnnotations

Hints claimed by the upstream server; the gateway does not enforce them.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `read_only`                                                                  | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Upstream claims the tool does not modify state.                              |
| `destructive`                                                                | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Upstream claims the tool can perform destructive updates.                    |
| `idempotent`                                                                 | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Upstream claims repeated calls with the same arguments have no extra effect. |
| `open_world`                                                                 | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Upstream claims the tool reaches systems outside its own domain.             |