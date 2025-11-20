# GetAgentTaskTaskState

Current state of the agent task execution. Values: submitted (queued), working (executing), input-required (awaiting user input), completed (finished successfully), failed (error occurred). Note: auth-required, canceled, and rejected statuses are defined for A2A protocol compatibility but are not currently supported in task execution.


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `SUBMITTED`      | submitted        |
| `WORKING`        | working          |
| `INPUT_REQUIRED` | input-required   |
| `AUTH_REQUIRED`  | auth-required    |
| `COMPLETED`      | completed        |
| `FAILED`         | failed           |
| `CANCELED`       | canceled         |
| `REJECTED`       | rejected         |