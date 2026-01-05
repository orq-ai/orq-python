# ToolReviewDoneEventData


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `tool_id`                                           | *str*                                               | :heavy_check_mark:                                  | Unique identifier for the tool in the tool registry |
| `tool_call_id`                                      | *str*                                               | :heavy_check_mark:                                  | The tool call ID that was reviewed                  |
| `review`                                            | [models.ReviewOutcome](../models/reviewoutcome.md)  | :heavy_check_mark:                                  | The review decision                                 |