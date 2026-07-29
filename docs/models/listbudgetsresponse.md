# ListBudgetsResponse


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `object`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | Object discriminator for list responses; always `list`.                   |
| `data`                                                                    | List[[models.Budget](../models/budget.md)]                                | :heavy_check_mark:                                                        | Page of budgets, ordered newest first.                                    |
| `has_more`                                                                | *bool*                                                                    | :heavy_check_mark:                                                        | Whether more budgets are available in the selected pagination<br/> direction. |