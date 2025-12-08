# ResponseStartedEvent

Emitted when the agent begins processing. Contains identifiers for tracking the response.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | [models.ResponseStartedEventType](../models/responsestartedeventtype.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `timestamp`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | ISO timestamp of when the event occurred                                 |
| `data`                                                                   | [models.Data](../models/data.md)                                         | :heavy_check_mark:                                                       | N/A                                                                      |