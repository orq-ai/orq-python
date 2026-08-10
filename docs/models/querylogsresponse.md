# QueryLogsResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `object`                                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Object discriminator; always "query". Mirrors QueryTracesResponse.     |
| `search`                                                               | [Optional[models.SearchLogsResponse]](../models/searchlogsresponse.md) | :heavy_minus_sign:                                                     | N/A                                                                    |