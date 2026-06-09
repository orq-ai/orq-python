# ResponseErrorStreamEvent


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `data`                                                                             | [models.ResponseErrorStreamEventData](../models/responseerrorstreameventdata.md)   | :heavy_check_mark:                                                                 | The event payload.                                                                 |
| `event`                                                                            | [models.ResponseErrorStreamEventEvent](../models/responseerrorstreameventevent.md) | :heavy_check_mark:                                                                 | The SSE event name, equal to the payload's `type`.                                 |