# Pages


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `index`                                                                  | *float*                                                                  | :heavy_check_mark:                                                       | The page index in a pdf document starting from 0                         |
| `markdown`                                                               | *str*                                                                    | :heavy_check_mark:                                                       | The markdown string response of the page                                 |
| `images`                                                                 | List[[models.PostV2RouterOcrImages](../models/postv2routerocrimages.md)] | :heavy_check_mark:                                                       | N/A                                                                      |
| `dimensions`                                                             | [OptionalNullable[models.Dimensions]](../models/dimensions.md)           | :heavy_minus_sign:                                                       | The dimensions of the PDF Page's screenshot image                        |