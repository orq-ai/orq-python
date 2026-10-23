# CreateAuditLogDestinationRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `display_name`                                                             | *str*                                                                      | :heavy_check_mark:                                                         | Required. Human-readable destination name, unique within the workspace.    |
| `description`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Optional. Description of the receiving system.                             |
| `url`                                                                      | *str*                                                                      | :heavy_check_mark:                                                         | Required. Absolute HTTPS URL. Private and loopback addresses are rejected. |