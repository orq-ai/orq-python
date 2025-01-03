# FileUploadResponseBody

File uploaded successfully


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `object_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | path to the file in the storage                                      |
| `purpose`                                                            | [models.FileUploadPurpose](../models/fileuploadpurpose.md)           | :heavy_check_mark:                                                   | The intended purpose of the uploaded file.                           |
| `bytes`                                                              | *float*                                                              | :heavy_check_mark:                                                   | N/A                                                                  |
| `file_name`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was created                           |