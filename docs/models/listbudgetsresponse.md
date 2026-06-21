# ListBudgetsResponse


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `object`                                                                  | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Object discriminator for list responses; always `list`.                   |
| `data`                                                                    | List[[models.Budget](../models/budget.md)]                                | :heavy_minus_sign:                                                        | Page of budgets, ordered newest first.                                    |
| `has_more`                                                                | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Whether more budgets are available in the selected pagination<br/> direction. |