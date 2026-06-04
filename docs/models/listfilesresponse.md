# ListFilesResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `object`                                                               | *str*                                                                  | :heavy_check_mark:                                                     | Object discriminator for list responses; always `list`.                |
| `data`                                                                 | List[[models.File](../models/file.md)]                                 | :heavy_check_mark:                                                     | Page of files.                                                         |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | Whether more files are available in the selected pagination direction. |