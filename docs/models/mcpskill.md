# McpSkill

A skill an upstream server publishes through the MCP Skills extension (`io.modelcontextprotocol/skills`).


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `uri`                                                             | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Resource URI of the skill's `SKILL.md` on the upstream server.    |
| `name`                                                            | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Skill name from the `SKILL.md` frontmatter.                       |
| `description`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Skill description from the `SKILL.md` frontmatter.                |
| `frontmatter`                                                     | [Optional[models.Frontmatter]](../models/frontmatter.md)          | :heavy_minus_sign:                                                | Full `SKILL.md` frontmatter as published upstream.                |
| `files`                                                           | List[[models.McpSkillFile](../models/mcpskillfile.md)]            | :heavy_minus_sign:                                                | Manifest of the skill's files; empty when the skill is dynamic.   |
| `dynamic`                                                         | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Upstream generates the skill's content and publishes no manifest. |