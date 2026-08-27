# ListAnnotationQueuesResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `object`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | Object discriminator for list responses; always `list`.                            |
| `data`                                                                             | List[[models.AnnotationQueue](../models/annotationqueue.md)]                       | :heavy_check_mark:                                                                 | Page of annotation queues.                                                         |
| `has_more`                                                                         | *bool*                                                                             | :heavy_check_mark:                                                                 | Whether more annotation queues are available in the selected pagination direction. |