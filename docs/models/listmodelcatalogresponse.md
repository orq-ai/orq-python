# ListModelCatalogResponse


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `object`                                                                  | *str*                                                                     | :heavy_check_mark:                                                        | Object discriminator for list responses; always `list`.                   |
| `data`                                                                    | List[[models.Model](../models/model.md)]                                  | :heavy_check_mark:                                                        | Page of catalog entries.                                                  |
| `has_more`                                                                | *bool*                                                                    | :heavy_check_mark:                                                        | Whether more entries are available in the selected pagination<br/> direction. |