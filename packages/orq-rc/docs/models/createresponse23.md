# CreateResponse23

A file input content part.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type`                                                                                 | [models.CreateResponse2ProxyRequestType](../models/createresponse2proxyrequesttype.md) | :heavy_check_mark:                                                                     | The type of input content part                                                         |
| `file_data`                                                                            | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Base64 encoded file data                                                               |
| `file_id`                                                                              | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | File ID from the Files API                                                             |
| `filename`                                                                             | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | Name of the file                                                                       |
| `file_url`                                                                             | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | URL of the file to fetch                                                               |