# ListModelCatalogOfferingsResponse


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `object`                                                                    | *str*                                                                       | :heavy_check_mark:                                                          | Object discriminator for list responses; always `list`.                     |
| `data`                                                                      | List[[models.Model](../models/model.md)]                                    | :heavy_check_mark:                                                          | Page of catalog offerings, ordered by `offering_of` then `id`.              |
| `has_more`                                                                  | *bool*                                                                      | :heavy_check_mark:                                                          | Whether more offerings are available in the selected pagination<br/> direction. |