# UpdateSkillRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `skill_id`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Skill ID to update.                                               |
| `display_name`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | New workspace-unique display name. Omit to keep the current name. |
| `description`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | New description. Omit to keep the current description.            |
| `tags`                                                            | List[*str*]                                                       | :heavy_minus_sign:                                                | Replacement tag list. Leave empty to clear tags.                  |
| `path`                                                            | *Optional[str]*                                                   | :heavy_minus_sign:                                                | New project path. Omit to keep the current path.                  |
| `instructions`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | New instruction body. Omit to keep the current instructions.      |
| `project_id`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | New containing project. Omit to keep the current project.         |