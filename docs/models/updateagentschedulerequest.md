# UpdateAgentScheduleRequest


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `agent_key`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | The unique routing key of the agent the schedule belongs to.                         |
| `schedule_id`                                                                        | *str*                                                                                | :heavy_check_mark:                                                                   | The schedule's ULID, as returned from create.                                        |
| `request_body`                                                                       | [models.UpdateAgentScheduleRequestBody](../models/updateagentschedulerequestbody.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |