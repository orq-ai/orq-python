# CreateRouterResponseData

A server-sent event in the response stream.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `sequence_number`                                                        | *int*                                                                    | :heavy_check_mark:                                                       | Monotonically increasing sequence number for ordering events.            |
| `type`                                                                   | [models.CreateRouterResponseType](../models/createrouterresponsetype.md) | :heavy_check_mark:                                                       | The event type.                                                          |