# Data1

Prompt model returned from the API


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `owner`                                                              | [models.DataOwner](../models/dataowner.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `domain_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_by_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `display_name`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_by_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `prompt_config`                                                      | [models.DataPromptConfig](../models/datapromptconfig.md)             | :heavy_check_mark:                                                   | N/A                                                                  |
| `metadata`                                                           | [models.DataMetadata](../models/datametadata.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |
| `versions`                                                           | List[[models.DataVersions](../models/dataversions.md)]               | :heavy_check_mark:                                                   | N/A                                                                  |
| `type`                                                               | [models.DataType](../models/datatype.md)                             | :heavy_check_mark:                                                   | N/A                                                                  |
| `description`                                                        | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was created                           |
| `updated`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was last updated                      |