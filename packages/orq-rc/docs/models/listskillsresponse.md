# ListSkillsResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `object`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | Object discriminator for list responses; always `list`.                  |
| `data`                                                                   | List[[models.Skill](../models/skill.md)]                                 | :heavy_check_mark:                                                       | Page of skills, ordered newest first.                                    |
| `has_more`                                                               | *bool*                                                                   | :heavy_check_mark:                                                       | Whether more skills are available in the selected pagination<br/> direction. |