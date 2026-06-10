# CreateRouterResponseResponsesResponseBody

Returns a response object or a stream of events.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `data`                                                                                                 | [Optional[models.ResponseStreamEvent]](../models/responsestreamevent.md)                               | :heavy_minus_sign:                                                                                     | A single server-sent event emitted on the response stream. The `type` field discriminates the payload. |