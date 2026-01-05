# ToolReviewDoneEvent

Emitted after a tool action has been reviewed. Contains the review decision.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [models.ToolReviewDoneEventType](../models/toolreviewdoneeventtype.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `timestamp`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | ISO timestamp of when the event occurred                               |
| `data`                                                                 | [models.ToolReviewDoneEventData](../models/toolreviewdoneeventdata.md) | :heavy_check_mark:                                                     | N/A                                                                    |