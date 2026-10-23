# McpSyncState


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `status`                                                         | [Optional[models.SyncStatus]](../models/syncstatus.md)           | :heavy_minus_sign:                                               | N/A                                                              |
| `tools_total`                                                    | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Tools in the catalog after the last sync.                        |
| `tools_added`                                                    | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Tools the last sync discovered for the first time.               |
| `tools_removed`                                                  | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Tools the last sync no longer found upstream and marked MISSING. |
| `last_synced_at`                                                 | *Optional[str]*                                                  | :heavy_minus_sign:                                               | ISO 8601 timestamp of the last sync attempt.                     |
| `errors`                                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | Failures reported by the last sync.                              |