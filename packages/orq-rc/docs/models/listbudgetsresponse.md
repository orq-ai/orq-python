# ListBudgetsResponse


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `object`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | Object discriminator for list responses; always `list`.                   |
| `data`                                                                    | List[[models.BudgetRestResponse](../models/budgetrestresponse.md)]        | :heavy_check_mark:                                                        | Page of budgets, ordered newest first.                                    |
| `has_more`                                                                | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Whether more budgets are available in the selected pagination<br/> direction. |