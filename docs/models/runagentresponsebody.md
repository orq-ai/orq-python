# RunAgentResponseBody

A2A Task response format


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | The ID of the created agent execution task           |
| `context_id`                                         | *str*                                                | :heavy_check_mark:                                   | The context ID (workspace ID)                        |
| `kind`                                               | [models.RunAgentKind](../models/runagentkind.md)     | :heavy_check_mark:                                   | A2A entity type                                      |
| `status`                                             | [models.RunAgentStatus](../models/runagentstatus.md) | :heavy_check_mark:                                   | Task status information                              |
| `metadata`                                           | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | Task metadata                                        |