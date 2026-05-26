# RetrieveIdentityRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | Unique identity id or external id                           |
| `include_metrics`                                           | *OptionalNullable[bool]*                                    | :heavy_minus_sign:                                          | Include usage metrics of the last 30 days for the identity. |