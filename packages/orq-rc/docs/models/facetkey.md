# FacetKey

FacetKey is one facetable key inside a group, with its observed volume and
 top values for the requested range. field is the name usable in filters /
 sort (e.g. "attribute.http.method" or "service_name"); it is empty when the
 key is not filterable (the scope group).


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `key`                                              | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `field`                                            | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `log_count`                                        | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `distinct_value_count`                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `top_values`                                       | List[[models.FacetValue](../models/facetvalue.md)] | :heavy_minus_sign:                                 | N/A                                                |
| `filterable`                                       | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |