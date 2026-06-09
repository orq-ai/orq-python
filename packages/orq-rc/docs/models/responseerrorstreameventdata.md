# ResponseErrorStreamEventData

The event payload.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `error`                                                                          | [models.ResponseError](../models/responseerror.md)                               | :heavy_check_mark:                                                               | N/A                                                                              |
| `sequence_number`                                                                | *int*                                                                            | :heavy_check_mark:                                                               | Monotonically increasing sequence number for ordering events.                    |
| `type`                                                                           | [models.ResponseErrorStreamEventType](../models/responseerrorstreameventtype.md) | :heavy_check_mark:                                                               | The event type. Matches the SSE `event` field.                                   |
| `__pydantic_extra__`                                                             | Dict[str, *Any*]                                                                 | :heavy_minus_sign:                                                               | N/A                                                                              |