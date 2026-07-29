# FindLogPatternsResponse


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `object`                                                       | *str*                                                          | :heavy_check_mark:                                             | Object discriminator; always "list".                           |
| `data`                                                         | List[[models.LogPattern](../models/logpattern.md)]             | :heavy_check_mark:                                             | N/A                                                            |
| `meta`                                                         | [models.FindLogPatternsMeta](../models/findlogpatternsmeta.md) | :heavy_check_mark:                                             | N/A                                                            |