# ResponseOutputItemStreamEvent


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `data`                                                                                       | [models.ResponseOutputItemStreamEventData](../models/responseoutputitemstreameventdata.md)   | :heavy_check_mark:                                                                           | The event payload.                                                                           |
| `event`                                                                                      | [models.ResponseOutputItemStreamEventEvent](../models/responseoutputitemstreameventevent.md) | :heavy_check_mark:                                                                           | The SSE event name, equal to the payload's `type`.                                           |