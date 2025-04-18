# UpdateDatasetResponseBody

Dataset updated.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The unique identifier of the dataset                                 |
| `display_name`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The display name of the dataset                                      |
| `project_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The unique identifier of the project it belongs to                   |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The unique identifier of the workspace it belongs to                 |
| `created_by_id`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The unique identifier of the user who created the dataset            |
| `updated_by_id`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The unique identifier of the user who last updated the dataset       |
| `metadata`                                                           | [models.UpdateDatasetMetadata](../models/updatedatasetmetadata.md)   | :heavy_check_mark:                                                   | N/A                                                                  |
| `parent_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The unique identifier for the parent of the committed version        |
| `version`                                                            | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The version of the dataset                                           |
| `created`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was created                           |
| `updated`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The date and time the resource was last updated                      |