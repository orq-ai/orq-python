# DeleteAnnotationRequestBody


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `keys`                                                                             | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | Unique keys of the reviews to remove                                               |
| `parent_annotation_ids`                                                            | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | Eval ids whose corrections should be removed                                       |
| `metadata`                                                                         | [Optional[models.DeleteAnnotationMetadata]](../models/deleteannotationmetadata.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |