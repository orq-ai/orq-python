# FileGetResponseBody

File details retrieved successfully


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `object_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | path to the file in the storage                                      |
| `purpose`                                                            | [models.FileGetPurpose](../models/filegetpurpose.md)                 | :heavy_check_mark:                                                   | The intended purpose of the uploaded file.                           |
| `bytes_`                                                             | *float*                                                              | :heavy_check_mark:                                                   | N/A                                                                  |
| `file_name`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The id of the resource                                               |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was created                           |