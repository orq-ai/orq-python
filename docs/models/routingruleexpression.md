# RoutingRuleExpression


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `config`                                                                    | [Optional[models.Config]](../models/config.md)                              | :heavy_minus_sign:                                                          | N/A                                                                         |
| `cel`                                                                       | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | CEL expression used to match requests. Empty means the rule always matches. |