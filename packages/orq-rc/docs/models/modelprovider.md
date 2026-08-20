# ModelProvider


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *str*                                                           | :heavy_check_mark:                                              | Catalog provider key (openai, anthropic, aws, ...).             |
| `name`                                                          | *str*                                                           | :heavy_check_mark:                                              | Provider display name.                                          |
| `logo`                                                          | *str*                                                           | :heavy_check_mark:                                              | Absolute URL of the provider logo. Empty when no logo is known. |
| `docs_url`                                                      | *str*                                                           | :heavy_check_mark:                                              | Provider documentation URL.                                     |
| `pricing_url`                                                   | *str*                                                           | :heavy_check_mark:                                              | Provider pricing page URL.                                      |