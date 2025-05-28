# Deployments2File


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `file_data`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | The base64 encoded file data, used when passing the file to the model as a string. |
| `filename`                                                                         | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The name of the file, used when passing the file to the model as a string.         |