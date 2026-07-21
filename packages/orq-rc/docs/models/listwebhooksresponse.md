# ListWebhooksResponse

A page of webhooks and the total number of matching records.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `count`                                                           | *int*                                                             | :heavy_check_mark:                                                | Total number of webhooks matching the filters, before pagination. |
| `items`                                                           | List[[models.Webhook](../models/webhook.md)]                      | :heavy_check_mark:                                                | Requested page of webhooks.                                       |
| `has_more`                                                        | *bool*                                                            | :heavy_check_mark:                                                | Whether another page of matching webhooks is available.           |