# ResponseLifecycleStreamEventData

The event payload.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `response`                                                                               | [models.PublicResponseResource](../models/publicresponseresource.md)                     | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `sequence_number`                                                                        | *int*                                                                                    | :heavy_check_mark:                                                                       | Monotonically increasing sequence number for ordering events.                            |
| `type`                                                                                   | [models.ResponseLifecycleStreamEventType](../models/responselifecyclestreameventtype.md) | :heavy_check_mark:                                                                       | The event type. Matches the SSE `event` field.                                           |
| `__pydantic_extra__`                                                                     | Dict[str, *Any*]                                                                         | :heavy_minus_sign:                                                                       | N/A                                                                                      |