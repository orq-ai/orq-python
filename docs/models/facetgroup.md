# FacetGroup

FacetGroup is one attribute family in the facet hierarchy. name is one of
 "native" (promoted columns), "attribute" (log_attributes), "resource"
 (resource_attributes), or "scope" (scope_attributes).


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `name`                                         | *Optional[str]*                                | :heavy_minus_sign:                             | N/A                                            |
| `keys`                                         | List[[models.FacetKey](../models/facetkey.md)] | :heavy_minus_sign:                             | N/A                                            |