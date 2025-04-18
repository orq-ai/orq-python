# ListSessionsRequestBody


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `pagination`                                                         | [Optional[models.Pagination]](../models/pagination.md)               | :heavy_minus_sign:                                                   | N/A                                                                  |
| `sorting_props`                                                      | List[[models.SortingProps](../models/sortingprops.md)]               | :heavy_minus_sign:                                                   | N/A                                                                  |
| `query`                                                              | [Optional[models.Query]](../models/query.md)                         | :heavy_minus_sign:                                                   | N/A                                                                  |
| `filters`                                                            | List[[models.ListSessionsFilters](../models/listsessionsfilters.md)] | :heavy_check_mark:                                                   | N/A                                                                  |
| `included_fields`                                                    | Dict[str, *str*]                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |