# ResponseDoneEvent

Emitted when the agent completes processing. Contains the finish reason and usage statistics.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `type`                                                             | [models.ResponseDoneEventType](../models/responsedoneeventtype.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `timestamp`                                                        | *str*                                                              | :heavy_check_mark:                                                 | ISO timestamp of when the event occurred                           |
| `data`                                                             | [models.ResponseDoneEventData](../models/responsedoneeventdata.md) | :heavy_check_mark:                                                 | N/A                                                                |