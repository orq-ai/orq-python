# ListBatchesResponseBody

Batches listed (empty array if none).


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `data`                                               | List[[models.PublicBatch](../models/publicbatch.md)] | :heavy_check_mark:                                   | Batches on the current page.                         |
| `first_id`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | ID of the first batch on the page.                   |
| `has_more`                                           | *bool*                                               | :heavy_check_mark:                                   | Whether further batches exist beyond this page.      |
| `last_id`                                            | *Optional[str]*                                      | :heavy_minus_sign:                                   | ID of the last batch on the page.                    |
| `object`                                             | *str*                                                | :heavy_check_mark:                                   | Object type, always list.                            |