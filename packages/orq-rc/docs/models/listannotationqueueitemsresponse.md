# ListAnnotationQueueItemsResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `object`                                                               | *str*                                                                  | :heavy_check_mark:                                                     | Object discriminator for list responses; always `list`.                |
| `data`                                                                 | List[[models.AnnotationQueueItem](../models/annotationqueueitem.md)]   | :heavy_check_mark:                                                     | Page of annotation queue items.                                        |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | Whether more items are available in the selected pagination direction. |