# BudgetAlertRestResponse

Notifies every listed notifier once current-period consumption on
 `dimension` reaches `threshold_percent` of the matching limit. Each alert
 fires at most once per period, re-arming on rollover or a limit change.
 The dimension must have a limit set, or the write is rejected.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Assigned by ORQ. Supply an existing id to edit that alert in place.        |
| `threshold_percent`                                                        | *int*                                                                      | :heavy_check_mark:                                                         | Percentage of the dimension's limit at which the alert fires, 1–100.       |
| `notifier_ids`                                                             | List[*str*]                                                                | :heavy_check_mark:                                                         | Must be workspace-scoped; project-scoped notifiers are rejected.           |
| `dimension`                                                                | [Optional[models.BudgetAlertDimension]](../models/budgetalertdimension.md) | :heavy_minus_sign:                                                         | N/A                                                                        |