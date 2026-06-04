# ListProjectsResponse


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `object`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Object discriminator for list responses; always `list`.                    |
| `data`                                                                     | List[[models.Project](../models/project.md)]                               | :heavy_minus_sign:                                                         | Page of projects, ordered newest first.                                    |
| `has_more`                                                                 | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Whether more projects are available in the selected pagination<br/> direction. |