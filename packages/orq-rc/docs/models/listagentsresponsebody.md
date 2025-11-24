# ListAgentsResponseBody

Successfully retrieved the list of agents. Returns a paginated response containing agent manifests with complete configurations, including primary and fallback models, tools, knowledge bases, and execution settings.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `object`                                                   | [models.ListAgentsObject](../models/listagentsobject.md)   | :heavy_check_mark:                                         | N/A                                                        |
| `data`                                                     | List[[models.ListAgentsData](../models/listagentsdata.md)] | :heavy_check_mark:                                         | N/A                                                        |
| `has_more`                                                 | *bool*                                                     | :heavy_check_mark:                                         | N/A                                                        |