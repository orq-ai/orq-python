# CreateResponseAnnotations1

A citation to a URL


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`                                                                             | [models.CreateResponseAnnotationsType](../models/createresponseannotationstype.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `start_index`                                                                      | *float*                                                                            | :heavy_check_mark:                                                                 | The start index of the citation in the text                                        |
| `end_index`                                                                        | *float*                                                                            | :heavy_check_mark:                                                                 | The end index of the citation in the text                                          |
| `url`                                                                              | *str*                                                                              | :heavy_check_mark:                                                                 | The URL being cited                                                                |
| `title`                                                                            | *str*                                                                              | :heavy_check_mark:                                                                 | The title of the cited resource                                                    |