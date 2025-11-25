# ExecutionReviewedStreamingEvent

Emitted after the agent execution has been reviewed. The execution will resume processing after this event.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `type`                                                                                         | [models.ExecutionReviewedStreamingEventType](../models/executionreviewedstreamingeventtype.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `timestamp`                                                                                    | *str*                                                                                          | :heavy_check_mark:                                                                             | ISO timestamp of the event                                                                     |
| `data`                                                                                         | [models.ExecutionReviewedStreamingEventData](../models/executionreviewedstreamingeventdata.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |