# Consumption


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `current_amount`                           | *float*                                    | :heavy_check_mark:                         | Current period consumption in USD          | 125.5                                      |
| `remaining_amount`                         | *float*                                    | :heavy_check_mark:                         | Remaining budget (amount - current_amount) | 124.5                                      |
| `period_start`                             | *Nullable[str]*                            | :heavy_check_mark:                         | When the current period started            | 2024-01-01T00:00:00Z                       |
| `period_end`                               | *Nullable[str]*                            | :heavy_check_mark:                         | When the current period will reset         | 2024-01-31T23:59:59Z                       |