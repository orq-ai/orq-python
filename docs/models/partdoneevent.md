# PartDoneEvent

Emitted when a part has been fully streamed. Contains the complete part with all content.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `type`                                                     | [models.PartDoneEventType](../models/partdoneeventtype.md) | :heavy_check_mark:                                         | N/A                                                        |
| `timestamp`                                                | *str*                                                      | :heavy_check_mark:                                         | ISO timestamp of when the event occurred                   |
| `data`                                                     | [models.PartDoneEventData](../models/partdoneeventdata.md) | :heavy_check_mark:                                         | N/A                                                        |