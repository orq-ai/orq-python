# InvokeEvaluatorResponse

Response wrappers keep each RPC's response type distinct, so a future field
 can be added to one without touching the other.


## Fields

| Field                                                                                                                                          | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `result`                                                                                                                                       | [Optional[models.EvaluationResult]](../models/evaluationresult.md)                                                                             | :heavy_minus_sign:                                                                                                                             | The verdict. Shaped to match WorkflowRunMinifiedEvalSchema, the body the<br/> TypeScript route returned, so existing consumers read the same JSON. |