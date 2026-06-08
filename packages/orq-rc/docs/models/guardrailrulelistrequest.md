# GuardrailRuleListRequest


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `limit`                                                   | *Optional[int]*                                           | :heavy_minus_sign:                                        | N/A                                                       |
| `starting_after`                                          | *Optional[str]*                                           | :heavy_minus_sign:                                        | A cursor for use in pagination.                           |
| `ending_before`                                           | *Optional[str]*                                           | :heavy_minus_sign:                                        | A cursor for use in pagination.                           |
| `project_id`                                              | *Optional[str]*                                           | :heavy_minus_sign:                                        | Optional filter by project ID.                            |
| `search`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Filter by display name or description (case-insensitive). |
| `sort_by`                                                 | [Optional[models.SortBy]](../models/sortby.md)            | :heavy_minus_sign:                                        | Field to sort by. Defaults to created_at (newest first).  |
| `enabled`                                                 | *OptionalNullable[bool]*                                  | :heavy_minus_sign:                                        | Filter by enabled status.                                 |
| `guardrail_id`                                            | List[*str*]                                               | :heavy_minus_sign:                                        | Filter by referenced guardrail ids (comma-separated).     |