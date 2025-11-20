# ListAgentTasksAgentTasksListResponse

Response format for listing all tasks associated with an agent. Includes paginated task array and total count.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `tasks`                                                                | List[[models.ExtendedTaskResponse](../models/extendedtaskresponse.md)] | :heavy_check_mark:                                                     | Array of agent tasks with full execution details                       |
| `overall_total`                                                        | *float*                                                                | :heavy_check_mark:                                                     | Total count of tasks for this agent (across all pages, unfiltered)     |