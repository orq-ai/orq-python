# StreamAgentResponseBody

Server-Sent Event stream successfully established. Returns real-time events including agent messages, tool calls, status updates, and completion signals. The stream ends with a [DONE] sentinel value.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `data`                                                 | [models.StreamAgentData](../models/streamagentdata.md) | :heavy_check_mark:                                     | N/A                                                    |