# ResponseLifecycleStreamEvent


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `data`                                                                                   | [models.ResponseLifecycleStreamEventData](../models/responselifecyclestreameventdata.md) | :heavy_check_mark:                                                                       | The event payload.                                                                       |
| `event`                                                                                  | [models.Event](../models/event.md)                                                       | :heavy_check_mark:                                                                       | The SSE event name, equal to the payload's `type`.                                       |