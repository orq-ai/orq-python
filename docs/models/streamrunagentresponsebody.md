# StreamRunAgentResponseBody

Server-Sent Event stream successfully established. Delivers real-time agent execution events including message fragments, tool invocations, intermediate results, and completion status. Stream terminates with [DONE] sentinel upon completion.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `data`                                                       | [models.StreamRunAgentData](../models/streamrunagentdata.md) | :heavy_check_mark:                                           | N/A                                                          |