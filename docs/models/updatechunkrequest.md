# UpdateChunkRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `chunk_id`                                                                     | *str*                                                                          | :heavy_check_mark:                                                             | The unique identifier of the chunk                                             |
| `datasource_id`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | The unique identifier of the data source                                       |
| `knowledge_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | The unique identifier of the knowledge base                                    |
| `request_body`                                                                 | [Optional[models.UpdateChunkRequestBody]](../models/updatechunkrequestbody.md) | :heavy_minus_sign:                                                             | N/A                                                                            |