# CompactResponseResponseBody

Compaction completed successfully.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `created_at`                                                           | *int*                                                                  | :heavy_check_mark:                                                     | Unix timestamp (seconds) when the response was created.                |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the compaction response.                                     |
| `object`                                                               | [models.CompactResponseObject](../models/compactresponseobject.md)     | :heavy_check_mark:                                                     | Always "response.compaction".                                          |
| `output`                                                               | List[[models.PublicCompactionItem](../models/publiccompactionitem.md)] | :heavy_check_mark:                                                     | The compacted list of output items.                                    |
| `usage`                                                                | [models.PublicUsage](../models/publicusage.md)                         | :heavy_check_mark:                                                     | N/A                                                                    |