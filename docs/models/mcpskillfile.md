# McpSkillFile

A file of an upstream skill, as listed in the skill's manifest.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `uri`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Resource URI of the file on the upstream server.                     |
| `digest`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | SHA-256 digest of the file's raw bytes, formatted as `sha256:{hex}`. |
| `size`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Length in bytes of the file's raw content.                           |