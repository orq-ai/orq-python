# CreateProjectRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | Project name. Names must be non-empty and at most 128 characters. |
| `teams`                                                           | List[*str*]                                                       | :heavy_minus_sign:                                                | Team identifiers to associate with the project.                   |
| `description`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Optional human-readable description, at most 500 characters.      |