# CreateAgentResponseRequestResponseBody

Agent response successfully created and completed. Returns the full conversation including all messages, tool interactions, model used, and token usage statistics. In background mode, returns immediately with initial task details. In streaming mode, returns Server-Sent Events (SSE) with real-time events.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `data`                                                                                  | [Optional[models.ResponseStreamingEvent]](../models/responsestreamingevent.md)          | :heavy_minus_sign:                                                                      | Union of all possible streaming events. Each event has a type field for discrimination. |