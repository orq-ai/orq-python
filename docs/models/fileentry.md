# FileEntry

The file content messages below mirror the tools-pod JSON contract one for
 one. `path` is always relative to the file system root; an absolute path or a
 `..` segment is refused rather than clamped.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `path`                                             | *str*                                              | :heavy_check_mark:                                 | Path of the entry relative to the file system root |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Final path component                               |
| `type`                                             | [models.FileEntryType](../models/fileentrytype.md) | :heavy_check_mark:                                 | Kind of entry                                      |
| `size_bytes`                                       | *str*                                              | :heavy_check_mark:                                 | Size of the entry in bytes                         |
| `modified`                                         | *str*                                              | :heavy_check_mark:                                 | Last modification time of the entry                |