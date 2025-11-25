# ActionReviewedStreamingEvent

Emitted after a tool action has been reviewed. Contains the review decision (approved/rejected), optional mock output for rejected actions, and reviewer information.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `type`                                                                                   | [models.ActionReviewedStreamingEventType](../models/actionreviewedstreamingeventtype.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `timestamp`                                                                              | *str*                                                                                    | :heavy_check_mark:                                                                       | ISO timestamp of the event                                                               |
| `data`                                                                                   | [models.ActionReviewedStreamingEventData](../models/actionreviewedstreamingeventdata.md) | :heavy_check_mark:                                                                       | N/A                                                                                      |