# Configuration


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `file_system_id`                                                       | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The id of the file system to attach.                                   |
| `file_system_key`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The key of the file system to attach.                                  |
| `access_mode`                                                          | [Optional[models.AccessMode]](../models/accessmode.md)                 | :heavy_minus_sign:                                                     | Whether the agent may only read this file system, or also write to it. |