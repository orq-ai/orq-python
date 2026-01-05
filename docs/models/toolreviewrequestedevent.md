# ToolReviewRequestedEvent

Emitted when a tool action requires approval before execution. The execution will pause until reviewed.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `type`                                                                           | [models.ToolReviewRequestedEventType](../models/toolreviewrequestedeventtype.md) | :heavy_check_mark:                                                               | N/A                                                                              |
| `timestamp`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | ISO timestamp of when the event occurred                                         |
| `data`                                                                           | [models.ToolReviewRequestedEventData](../models/toolreviewrequestedeventdata.md) | :heavy_check_mark:                                                               | N/A                                                                              |