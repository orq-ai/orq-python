# McpResourceExposure


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `mode`                                                                     | [models.McpToolExposureMode](../models/mcptoolexposuremode.md)             | :heavy_check_mark:                                                         | N/A                                                                        |
| `resource_ids`                                                             | List[*str*]                                                                | :heavy_minus_sign:                                                         | `McpResource.selection_id` values to expose when mode is SELECTED.         |
| `resource_template_ids`                                                    | List[*str*]                                                                | :heavy_minus_sign:                                                         | `McpResourceTemplate.selection_id` values to expose when mode is SELECTED. |