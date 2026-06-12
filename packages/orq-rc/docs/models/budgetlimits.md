# BudgetLimits

BudgetLimits is the per-period spend and token ceiling. At least one
 of `amount`, `token_limit`, or RateLimit.requests_per_minute MUST be
 set on a Budget; that invariant is enforced by the handler.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `period`                                                   | [Optional[models.BudgetPeriod]](../models/budgetperiod.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `amount`                                                   | *Optional[float]*                                          | :heavy_minus_sign:                                         | N/A                                                        |
| `token_limit`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |