# ListProjectsResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | *str*                                                                      | :heavy_check_mark:                                                         | Object discriminator for list responses; always `list`.                    |
| `data`                                                                     | List[[models.Project](../models/project.md)]                               | :heavy_check_mark:                                                         | Page of projects, ordered newest first.                                    |
| `has_more`                                                                 | *bool*                                                                     | :heavy_check_mark:                                                         | Whether more projects are available in the selected pagination<br/> direction. |