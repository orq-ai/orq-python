# Tools2

Configuration for web search tool


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `type`                                                                           | [models.CreateResponseToolsProxyType](../models/createresponsetoolsproxytype.md) | :heavy_check_mark:                                                               | The type of tool                                                                 |
| `domains`                                                                        | List[*str*]                                                                      | :heavy_minus_sign:                                                               | List of domains to restrict search to                                            |
| `search_context_size`                                                            | [Optional[models.SearchContextSize]](../models/searchcontextsize.md)             | :heavy_minus_sign:                                                               | Amount of context to retrieve for each search result                             |
| `user_location`                                                                  | [Optional[models.UserLocation]](../models/userlocation.md)                       | :heavy_minus_sign:                                                               | User location for search localization                                            |