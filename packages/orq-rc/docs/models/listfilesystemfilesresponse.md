# ListFileSystemFilesResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `path`                                                   | *str*                                                    | :heavy_check_mark:                                       | Folder that was listed, relative to the file system root |
| `depth`                                                  | *int*                                                    | :heavy_check_mark:                                       | Number of folder levels that were walked                 |
| `entries`                                                | List[[models.FileEntry](../models/fileentry.md)]         | :heavy_check_mark:                                       | N/A                                                      |
| `entry_count`                                            | *int*                                                    | :heavy_check_mark:                                       | Number of entries returned                               |
| `truncated`                                              | *bool*                                                   | :heavy_check_mark:                                       | Whether the listing stopped at max_entries               |