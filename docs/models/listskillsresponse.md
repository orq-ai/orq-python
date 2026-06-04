# ListSkillsResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `object`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Object discriminator for list responses; always `list`.                  |
| `data`                                                                   | List[[models.Skill](../models/skill.md)]                                 | :heavy_minus_sign:                                                       | Page of skills, ordered newest first.                                    |
| `has_more`                                                               | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether more skills are available in the selected pagination<br/> direction. |