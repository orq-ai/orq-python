# ResourceCatalog

Get returns the shared catalog. Sync returns the caller's catalog for user-specific credentials or discovery variables. List omits this field.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `resources`                                                            | List[[models.McpResource](../models/mcpresource.md)]                   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `resource_templates`                                                   | List[[models.McpResourceTemplate](../models/mcpresourcetemplate.md)]   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `resources_status`                                                     | [Optional[models.McpDiscoveryStatus]](../models/mcpdiscoverystatus.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `resource_templates_status`                                            | [Optional[models.McpDiscoveryStatus]](../models/mcpdiscoverystatus.md) | :heavy_minus_sign:                                                     | N/A                                                                    |